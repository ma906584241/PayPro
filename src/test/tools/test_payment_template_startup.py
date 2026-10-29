"""Opt-in Linux container checks of the actual start.sh and template preparation.

Set PAYPRO_DOCKER_STARTUP_TESTS=1. Uses a cached Python image, a fake Java process,
isolated bind mounts and --network none; never starts the payment application.
"""
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("overlay_fixtures", ROOT / "src/test/tools/test_upgrade_payment_template.py")
FIXTURES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FIXTURES)


@unittest.skipUnless(os.environ.get("PAYPRO_DOCKER_STARTUP_TESTS") == "1", "requires opt-in Docker startup checks")
class PaymentTemplateStartupTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="paypro-startup-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.app = self.base / "app"
        self.overlay = self.app / "config/templates/payment.html"
        self.overlay.parent.mkdir(parents=True)
        self.qr = self.app / "qr/alipay/custom.png"
        self.qr.parent.mkdir(parents=True)
        self.qr.write_bytes(b"untouched-test-QR-asset")
        self.tools = self.base / "tools"
        self.tools.mkdir()
        for name in ["upgrade_payment_template.py", "prepare_payment_template.sh"]:
            shutil.copyfile(str(ROOT / "scripts" / name), str(self.tools / name))
        shutil.copyfile(str(ROOT / "src/main/resources/templates/payment.html"), str(self.tools / "payment.html"))
        # Normalize CRLF in a Windows checkout before testing Linux shell files.
        (self.base / "start.sh").write_bytes((ROOT / "src/main/resources/start.sh").read_bytes().replace(b"\r\n", b"\n"))
        prepare = self.tools / "prepare_payment_template.sh"
        prepare.write_bytes(prepare.read_bytes().replace(b"\r\n", b"\n"))
        (self.base / "fake-java").write_bytes(b"#!/bin/sh\necho JAVA_START_REACHED\n")

    def run_startup(self, readonly=False):
        image = os.environ.get("PAYPRO_TEST_PYTHON_IMAGE", "python:3.11-slim")
        command = ["docker", "run", "--rm", "--pull=never", "--network", "none"]
        for source, target, ro in [(self.app, "/app/appsystems", readonly),
                                   (self.tools, "/app/payment-template", True),
                                   (self.base / "start.sh", "/app/start.sh", True),
                                   (self.base / "fake-java", "/fixtures/fake-java", True)]:
            command += ["--mount", "type=bind,source=%s,target=%s%s" % (source, target, ",readonly" if ro else "")]
        command += [image, "/bin/sh", "-c", "mkdir -p /tmp/test-jdk/bin\n"
                    "cp /fixtures/fake-java /tmp/test-jdk/bin/java\n"
                    "chmod +x /tmp/test-jdk/bin/java\n"
                    "export JAVA_HOME=/tmp/test-jdk\n"
                    "exec /bin/sh /app/start.sh"]
        result = subprocess.run(command, capture_output=True, timeout=45)
        self.assertEqual(self.qr.read_bytes(), b"untouched-test-QR-asset")
        return result

    def test_no_override_uses_packaged_template_without_creating_files(self):
        result = self.run_startup()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(b"JAVA_START_REACHED", result.stdout)
        self.assertFalse(self.overlay.exists())
        self.assertFalse((self.app / "config/template-backups").exists())

    def test_old_overlay_restarts_and_later_restores_are_automatically_upgraded(self):
        original = FIXTURES.LEGACY.encode("utf-8")
        self.overlay.write_bytes(original)
        first = self.run_startup()
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertIn(b"JAVA_START_REACHED", first.stdout)
        upgraded = self.overlay.read_bytes()
        self.assertIn("我已完成付款".encode("utf-8"), upgraded)
        self.assertIn('<div class="value" th:text="${name}">AI智为工作室</div>'.encode("utf-8"), upgraded)
        self.assertNotIn("马宵冉".encode("utf-8"), upgraded)
        self.assertIn(b"fallbackToRemark", upgraded)
        backups = self.app / "config/template-backups"
        self.assertEqual(len(list(backups.glob("*.html"))), 1)
        self.assertEqual(next(backups.glob("*.html")).read_bytes(), original)
        second = self.run_startup()
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertEqual(self.overlay.read_bytes(), upgraded)
        self.assertEqual(len(list(backups.glob("*.html"))), 1)
        # Simulate the production deploy process restoring the old aside file.
        self.overlay.write_bytes(original)
        third = self.run_startup()
        self.assertEqual(third.returncode, 0, third.stdout + third.stderr)
        self.assertEqual(self.overlay.read_bytes(), upgraded)
        self.assertEqual(len(list(backups.glob("*.html"))), 2)

    def test_unknown_customizations_stop_before_java_and_leave_original_intact(self):
        original = FIXTURES.LEGACY.replace("data(){ return {}; }", "data(){ return {customSecret:'keep'}; }")
        self.overlay.write_text(original, encoding="utf-8", newline="\n")
        result = self.run_startup()
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn(b"JAVA_START_REACHED", result.stdout)
        self.assertIn(b"preparation failed", result.stderr)
        self.assertEqual(self.overlay.read_text(encoding="utf-8"), original)
        self.assertFalse((self.app / "config/template-backups").exists())

    def test_readonly_old_overlay_stops_before_java(self):
        self.overlay.write_text(FIXTURES.LEGACY, encoding="utf-8", newline="\n")
        result = self.run_startup(readonly=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn(b"JAVA_START_REACHED", result.stdout)
        self.assertEqual(self.overlay.read_text(encoding="utf-8"), FIXTURES.LEGACY)


if __name__ == "__main__":
    unittest.main()
