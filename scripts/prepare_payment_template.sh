#!/bin/sh
# Runs before Java starts; the canonical template is outside the config bind mount.
set -eu

APP_DIRECTORY=${1:-/app/appsystems}
TOOLS_DIRECTORY=${2:-/app/payment-template}
OVERLAY="$APP_DIRECTORY/config/templates/payment.html"

if [ ! -e "$OVERLAY" ]; then
    echo "Payment template: no external override; using the packaged template"
    exit 0
fi

echo "Payment template: checking the mounted override before application startup"
python3 "$TOOLS_DIRECTORY/upgrade_payment_template.py" \
    --template "$OVERLAY" \
    --canonical "$TOOLS_DIRECTORY/payment.html" \
    --apply

echo "Payment template: mounted override is ready"
