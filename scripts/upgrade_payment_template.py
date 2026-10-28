"""Upgrade the mounted payment template without replacing its QR selection logic.

Standard library only. No HTTP requests, payments, email, database or Redis access.
Invoked by image startup after mounts are available and before Java starts.
Can also run manually after restoring a deployment overlay.
"""
import argparse
import hashlib
import os
from pathlib import Path
import re
import shutil
import stat
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = re.compile(r"(<script\b[^>]*>)([\s\S]*?)(</script\s*>)", re.I)
PANEL = re.compile(r'(?m)^ {16}<div class="confirmation-panel"[\s\S]*?^ {16}</div>(?=\n {12}</div>)')


def one(pattern, source, description):
    matches = list(re.finditer(pattern, source)) if isinstance(pattern, str) else list(pattern.finditer(source))
    if len(matches) != 1:
        raise ValueError("Expected one %s; found %d. Original template was not changed." % (description, len(matches)))
    return matches[0]


def component(source):
    candidates = [m for m in SCRIPT.finditer(source) if "createApp({" in m[2] and ".mount('#app')" in m[2]]
    if len(candidates) != 1:
        raise ValueError("Cannot uniquely locate the payment Vue component; original template was not changed.")
    return candidates[0]


def method_block(source, name, following):
    return one(r"(?m)^ {8}(?:async\s+)?" + name + r"\(\)\s*\{[\s\S]*?(?=^ {8}(?:async\s+)?" + following + r"\(\))",
               source, name + " method")


def upgrade(existing, canonical):
    # Normalize text only; QR branch contents, conditions and precedence are preserved.
    existing = existing.replace("\r\n", "\n")
    canonical = canonical.replace("\r\n", "\n")
    old_app, new_app = component(existing), component(canonical)
    old_qr = method_block(old_app[2], "createPaymentOrder", "generateQRCode")[0]
    old_canvas = method_block(old_app[2], "generateQRCode", "startCountdown")[0]
    # Refuse to discard unrelated custom methods in a previously modified overlay.
    method_names = lambda text: set(re.findall(r"(?m)^ {8}(?:async\s+)?(\w+)\(", text))
    unknown = method_names(old_app[2]) - method_names(new_app[2])
    if unknown:
        raise ValueError("Custom component methods require a manual merge: " + ", ".join(sorted(unknown)))
    options = lambda text: set(re.findall(r"(?m)^ {4}(\w+)\s*[:(]", text))
    unknown_options = options(old_app[2]) - options(new_app[2])
    data_fields = lambda text: set(re.findall(r"\b(\w+)\s*:", one(
        r"(?m)^ {4}data\(\)\s*\{[\s\S]*?(?=^ {4}\w+\s*[:(])", text, "component data section")[0]))
    unknown_data = data_fields(old_app[2]) - data_fields(new_app[2])
    if unknown_options or unknown_data:
        raise ValueError("Custom component data/options require a manual merge: " +
                         ", ".join(sorted(unknown_options | unknown_data)))
    new_js = new_app[2]
    for name, following, preserved in [("createPaymentOrder", "generateQRCode", old_qr),
                                       ("generateQRCode", "startCountdown", old_canvas)]:
        match = method_block(new_js, name, following)
        new_js = new_js[:match.start()] + preserved + new_js[match.end():]
    opening = old_app[1]
    if 'th:inline=' not in opening:
        opening = opening[:-1] + ' th:inline="javascript">'
    result = existing[:old_app.start()] + opening + new_js + old_app[3] + existing[old_app.end():]

    countdown = one(r'''(<div\b[^>]*class="countdown"[^>]*v-if=")(?:paymentStatus==='pending'|showCountdown)(")''',
                    result, "pending countdown")
    result = result[:countdown.start()] + countdown[1] + "showCountdown" + countdown[2] + result[countdown.end():]
    qr = one(r'<div\b[^>]*\bclass="qr-wrap(?:\s+[^\"]*)?"[^>]*>', result, "QR container")
    qr_tag = qr[0]
    if "hasConfirmToken" not in qr_tag:
        if 'v-if=' in qr_tag:
            raise ValueError("Custom QR visibility requires a manual merge; original template was not changed.")
        qr_tag = qr_tag[:-1] + ' v-if="!hasConfirmToken || confirmationInfo">'
    result = result[:qr.start()] + qr_tag + result[qr.end():]

    panel = one(PANEL, canonical, "canonical confirmation panel")[0]
    if 'class="confirmation-panel"' in result:
        match = one(PANEL, result, "existing confirmation panel")
        result = result[:match.start()] + panel + result[match.end():]
    else:
        boundary = one(r'(?m)^ {12}</div>\n\n(?= {12}<div\b[^>]*v-if="showInfoPanel")', result, "payment card boundary")
        result = result[:boundary.start()] + panel + "\n" + result[boundary.start():]
    if ".confirmation-panel {" not in result:
        css = one(r"(?m)^ {8}\.confirmation-panel \{[\s\S]*?(?=^ {8}\.badge \{)", canonical, "confirmation styles")[0]
        boundary = one(r"(?m)^ {8}\.badge \{", result, "badge style insertion point")
        result = result[:boundary.start()] + css + result[boundary.start():]

    assert method_block(component(result)[2], "createPaymentOrder", "generateQRCode")[0] == old_qr
    assert method_block(component(result)[2], "generateQRCode", "startCountdown")[0] == old_canvas
    for marker in ["paymentConfirmToken", "refreshConfirmationStatus", "confirmPaid", "我已完成付款", "showCountdown"]:
        if marker not in result:
            raise ValueError("Missing confirmation contract: " + marker)
    return result


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", type=Path, default=ROOT / "config/templates/payment.html")
    parser.add_argument("--canonical", type=Path, default=ROOT / "src/main/resources/templates/payment.html")
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--check", action="store_true", help="read-only: exit 1 if the overlay needs upgrading")
    actions.add_argument("--apply", action="store_true", help="backup then atomically update the overlay")
    actions.add_argument("--output", type=Path, help="write a preview to a separate file without changing the overlay")
    args = parser.parse_args()
    try:
        target = args.template.resolve(strict=True)
        original = target.read_bytes()
        merged = upgrade(original.decode("utf-8-sig"), args.canonical.read_text(encoding="utf-8-sig")).encode("utf-8")
        changed = original.replace(b"\r\n", b"\n") != merged
        print("Overlay: %s\nBefore SHA-256: %s\nAfter SHA-256: %s" % (target, sha(original), sha(merged)))
        print("QR selection and canvas generation: preserved")
        if args.check:
            print("Upgrade required" if changed else "Confirmation workflow is current")
            return 1 if changed else 0
        if args.output:
            output = args.output.resolve()
            if output == target:
                raise ValueError("Use --apply to update the original with a backup")
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(merged)
            print("Preview: " + str(output))
        elif changed:
            backups = target.parent.parent / "template-backups"
            backups.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup = backups / ("payment-" + stamp + "-" + sha(original)[:12] + ".html")
            shutil.copy2(str(target), str(backup))
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(prefix=".payment-upgrade-", dir=str(target.parent), delete=False) as handle:
                    temporary = handle.name
                    handle.write(merged)
                os.chmod(temporary, stat.S_IMODE(target.stat().st_mode))
                os.replace(temporary, str(target))
            finally:
                if temporary and os.path.exists(temporary):
                    os.unlink(temporary)
            print("Backup: %s\nOverlay upgraded" % backup)
        else:
            print("Already current; no file or backup was written")
        return 0
    except (ValueError, OSError, UnicodeError) as error:
        print("ERROR: " + str(error))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
