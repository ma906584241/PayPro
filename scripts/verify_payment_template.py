"""Read-only readiness check of the served payment template; never loads an order."""
import argparse
import html
import os
from pathlib import Path
import re
import time
from urllib.error import URLError
from urllib.request import Request, urlopen

from upgrade_payment_template import RECIPIENT, one, version_marker


def validate_response(page, canonical, expected_name=None):
    if page.count(version_marker(canonical)) != 1:
        raise ValueError("The served payment template is not the version prepared by this image")
    for marker in ("paymentConfirmToken", "refreshConfirmationStatus", "confirmPaid", "我已完成付款"):
        if marker not in page:
            raise ValueError("Missing payment confirmation feature: " + marker)
    recipient = one(RECIPIENT, page, "served recipient summary")[2]
    if "th:text=" in recipient:
        raise ValueError("Payment recipient was not rendered by Thymeleaf")
    if expected_name is not None:
        value = re.sub(r"<[^>]+>", "", recipient)
        if html.unescape(value).strip() != expected_name.strip():
            raise ValueError("The served recipient does not match PAYPRO_NAME")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--canonical", type=Path, default=Path(__file__).with_name("payment.html"))
    parser.add_argument("--url", default="http://127.0.0.1:%s/payment.html" % os.environ.get("SERVER_PORT", "8889"))
    parser.add_argument("--wait", type=float, default=0, help="seconds to wait for the current template to be served")
    args = parser.parse_args()
    if args.wait < 0:
        parser.error("--wait must be nonnegative")
    try:
        canonical = args.canonical.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as error:
        print("Payment template readiness failed: " + str(error))
        return 1
    deadline = time.monotonic() + args.wait
    while True:
        try:
            request = Request(args.url, headers={"Cache-Control": "no-cache"})
            with urlopen(request, timeout=5) as response:
                page = response.read().decode("utf-8")
            validate_response(page, canonical, os.environ.get("PAYPRO_NAME"))
            print("Payment template ready: current image version and recipient verified")
            return 0
        except (URLError, OSError, UnicodeError, ValueError) as error:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                print("Payment template readiness failed: " + str(error))
                return 1
            time.sleep(min(2, remaining))


if __name__ == "__main__":
    raise SystemExit(main())
