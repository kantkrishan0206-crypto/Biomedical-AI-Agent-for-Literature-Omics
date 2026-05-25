#!/usr/bin/env bash
set -euo pipefail
echo "[biomedical-ai] $0"
uvicorn app.main:app --host 0.0.0.0 --port "$PORT"
