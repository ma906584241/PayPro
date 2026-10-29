#!/bin/sh
# Runs before Java starts; the canonical template is outside the config bind mount.
set -eu

APP_DIRECTORY=${1:-/app/appsystems}
TOOLS_DIRECTORY=${2:-/app/payment-template}
OVERLAY="$APP_DIRECTORY/config/templates/payment.html"

echo "Payment template: preparing the current version before application startup"
python3 "$TOOLS_DIRECTORY/upgrade_payment_template.py" \
    --template "$OVERLAY" \
    --canonical "$TOOLS_DIRECTORY/payment.html" \
    --runtime-template "$APP_DIRECTORY/runtime/templates/payment.html" \
    --apply

echo "Payment template: runtime snapshot is ready"
