"""Readiness regression checks using an isolated HTTP server, never the payment app."""
import html
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os
from pathlib import Path
import subprocess
import sys
import threading
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from upgrade_payment_template import version_marker
from verify_payment_template import validate_response
sys.path.pop(0)

CANONICAL = (ROOT / "src/main/resources/templates/payment.html").read_text(encoding="utf-8")


def rendered(name="AI智为工作室", canonical=CANONICAL):
    page = canonical.replace('<div class="value" th:text="${name}">AI智为工作室</div>',
                             '<div class="value">%s</div>' % html.escape(name))
    return page + "\n" + version_marker(canonical)


class VerifyPaymentTemplateTest(unittest.TestCase):
    def test_accepts_rendered_current_version_and_escaped_recipient(self):
        validate_response(rendered(), CANONICAL, "AI智为工作室")
        validate_response(rendered("A & B <工作室>"), CANONICAL, "A & B <工作室>")

    def test_rejects_stale_image_missing_confirmation_wrong_recipient_and_raw_template(self):
        cases = [rendered().replace(version_marker(CANONICAL), ""),
                 rendered(canonical=CANONICAL + "\n<!-- new image -->"),
                 rendered() + "\n" + version_marker(CANONICAL),
                 rendered().replace("confirmPaid", "missingFeature"),
                 rendered("马宵冉"),
                 CANONICAL + "\n" + version_marker(CANONICAL)]
        for page in cases:
            with self.subTest(page=page[-100:]):
                with self.assertRaises(ValueError):
                    validate_response(page, CANONICAL, "AI智为工作室")

    def test_wait_retries_old_response_and_only_requests_the_payment_page(self):
        requests = []
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                requests.append((self.path, self.headers.get("Cache-Control")))
                page = rendered("马宵冉") if len(requests) == 1 else rendered()
                self.send_response(200)
                self.send_header("Content-Type", "text/html;charset=UTF-8")
                self.end_headers()
                self.wfile.write(page.encode("utf-8"))

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            environment = os.environ.copy()
            environment["PAYPRO_NAME"] = "AI智为工作室"
            result = subprocess.run([sys.executable, str(ROOT / "scripts/verify_payment_template.py"),
                                     "--canonical", str(ROOT / "src/main/resources/templates/payment.html"),
                                     "--url", "http://127.0.0.1:%d/payment.html" % server.server_port,
                                     "--wait", "3"], env=environment, capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(requests, [("/payment.html", "no-cache"), ("/payment.html", "no-cache")])
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
