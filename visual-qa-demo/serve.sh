#!/usr/bin/env bash
# Serve the storefront on http://127.0.0.1:4173 (PORT overrides).
set -euo pipefail
cd "$(dirname "$0")"
exec python3 -m http.server "${PORT:-4173}" --bind 127.0.0.1
