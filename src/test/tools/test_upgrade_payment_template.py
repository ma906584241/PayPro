"""Regression checks for upgrading a mounted template, without a running service."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "scripts/upgrade_payment_template.py"
SPEC = importlib.util.spec_from_file_location("upgrade_payment_template", SCRIPT)
UPGRADE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(UPGRADE)
CANONICAL = (ROOT / "src/main/resources/templates/payment.html").read_text(encoding="utf-8")
LEGACY = '''<!DOCTYPE html>
<html lang="zh-CN" xmlns:th="http://www.thymeleaf.org">
<head><title th:text="${indexTitle}">Custom deployment</title><style>
        .qr-image { width: 247px; }
        .badge { color: white; }
</style></head><body>
        <div class="content">
            <div class="glass card">
                <div class="summary-item">
                    <div class="label">收款人</div>
                    <div class="value">马宵冉</div>
                </div>
                <div class="qr-wrap"><img :src="qrImageUrl" alt="二维码"></div>
                <div class="countdown" v-if="paymentStatus==='pending'">Time</div>
                <p>Existing customized footer and content</p>
            </div>

            <div class="glass card" v-if="showInfoPanel">Information</div>
        </div>
<script th:inline="javascript">
const { createApp } = Vue;
createApp({
    data(){ return {}; },
    methods:{
        async createPaymentOrder(){
            if(this.orderInfo.fallbackToRemark){
                this.qrImageUrl = `assets/qr/${this.orderInfo.payType}/${this.orderInfo.money}/${this.orderInfo.actualAmount}/${this.orderInfo.payQrNum}.png`;
            }else if(this.orderInfo.customerQr === 'true'){
                this.qrImageUrl = `assets/qr/${this.orderInfo.payType}/custom.png`;
            }else{
                const site = /*[[${site}]]*/ '';
                this.qrCodeUrl = site + '/openAlipay';
            }
        },
        async generateQRCode(){
            if(this.qrCodeUrl){ await QRCode.toCanvas(null, this.qrCodeUrl, {width:247}); }
        },
        startCountdown(){ return 'old'; }
    }
}).mount('#app');
</script></body></html>
'''


class UpgradePaymentTemplateTest(unittest.TestCase):
    def test_restored_hardcoded_recipient_uses_configuration_binding(self):
        original = LEGACY.replace("Existing customized footer and content", "Existing footer: 马宵冉")
        merged = UPGRADE.upgrade(original, CANONICAL)
        recipient = UPGRADE.one(UPGRADE.RECIPIENT, merged, "recipient summary")
        self.assertEqual(recipient[2], '<div class="value" th:text="${name}">AI智为工作室</div>')
        self.assertIn("Existing footer: 马宵冉", merged)

    def test_bound_recipient_with_old_fallback_is_also_updated(self):
        original = LEGACY.replace('<div class="value">马宵冉</div>',
                                  '<div class="value" th:text="${name}">马宵冉</div>')
        merged = UPGRADE.upgrade(original, CANONICAL)
        self.assertIn('<div class="value" th:text="${name}">AI智为工作室</div>', merged)
        self.assertNotIn("马宵冉", merged)

    def test_qr_branches_precedence_canvas_and_thymeleaf_are_preserved(self):
        merged = UPGRADE.upgrade(LEGACY, CANONICAL)
        for name, following in [("createPaymentOrder", "generateQRCode"), ("generateQRCode", "startCountdown")]:
            self.assertEqual(UPGRADE.method_block(UPGRADE.component(LEGACY)[2], name, following)[0],
                             UPGRADE.method_block(UPGRADE.component(merged)[2], name, following)[0])
        self.assertIn('th:text="${indexTitle}"', merged)
        self.assertIn(".qr-image { width: 247px; }", merged)
        self.assertIn("Existing customized footer and content", merged)
        self.assertIn('v-if="showCountdown"', merged)
        self.assertIn("我已完成付款", merged)
        self.assertIn("X-Payment-Confirm-Token", merged)
        self.assertIn("beforeUnmount()", merged)

    def test_repeat_upgrades_are_identical(self):
        merged = UPGRADE.upgrade(LEGACY, CANONICAL)
        self.assertEqual(merged, UPGRADE.upgrade(merged, CANONICAL))
        self.assertEqual(merged.count('class="confirmation-panel"'), 1)

    def test_unknown_custom_methods_are_rejected(self):
        customized = LEGACY.replace("        startCountdown()", "        customAnalytics(){},\n        startCountdown()")
        with self.assertRaisesRegex(ValueError, "customAnalytics"):
            UPGRADE.upgrade(customized, CANONICAL)

    def test_unrecognized_html_and_custom_visibility_are_rejected(self):
        for html in [LEGACY.replace('v-if="showInfoPanel"', 'v-if="customInfo"'),
                     LEGACY.replace('收款人', '自定义摘要'),
                     LEGACY.replace('<div class="label">收款人</div>',
                                    '<div class="label">收款人</div><div class="value">重复</div>'
                                    '<div class="label">收款人</div>'),
                     LEGACY.replace('class="qr-wrap"', 'class="qr-wrap" v-if="customVisibility"'),
                     LEGACY.replace("data(){ return {}; }", "data(){ return {customData:'preserve me'}; }"),
                     LEGACY.replace("    methods:{", "    watch:{},\n    methods:{"),
                     LEGACY + UPGRADE.component(LEGACY)[0]]:
            with self.assertRaises(ValueError):
                UPGRADE.upgrade(html, CANONICAL)

    def test_apply_backs_up_exact_original_bytes_and_is_idempotent(self):
        with tempfile.TemporaryDirectory(prefix="paypro-overlay-test-") as tmp:
            target = Path(tmp) / "config/templates/payment.html"
            target.parent.mkdir(parents=True)
            original = b'\xef\xbb\xbf' + LEGACY.replace("\n", "\r\n").encode("utf-8")
            target.write_bytes(original)
            command = [sys.executable, str(SCRIPT), "--template", str(target), "--apply"]
            first = subprocess.run(command, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stdout)
            backups = list((target.parent.parent / "template-backups").glob("*.html"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_bytes(), original)
            merged = target.read_bytes()
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
            self.assertEqual(target.read_bytes(), merged)
            self.assertEqual(len(list(backups[0].parent.glob("*.html"))), 1)
            check = subprocess.run(command[:-1] + ["--check"], capture_output=True)
            self.assertEqual(check.returncode, 0, check.stdout)

    def test_check_never_writes_or_creates_backups(self):
        with tempfile.TemporaryDirectory(prefix="paypro-overlay-test-") as tmp:
            target = Path(tmp) / "config/templates/payment.html"
            target.parent.mkdir(parents=True)
            target.write_text(LEGACY, encoding="utf-8")
            original = target.read_bytes()
            result = subprocess.run([sys.executable, str(SCRIPT), "--template", str(target), "--check"], capture_output=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(target.read_bytes(), original)
            self.assertFalse((target.parent.parent / "template-backups").exists())


if __name__ == "__main__":
    unittest.main()
