#!/usr/bin/env bash
set -euo pipefail
echo "[biomedical-ai] $0"
cd backend && alembic upgrade head
