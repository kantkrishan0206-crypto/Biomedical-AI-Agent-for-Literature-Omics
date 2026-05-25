#!/usr/bin/env bash
set -euo pipefail
echo "[biomedical-ai] $0"
for bin in git node pnpm python3 pip docker kubectl helm psql redis-cli; do command -v "$bin" >/dev/null 2>&1 && echo "ok $bin" || echo "missing $bin"; done
