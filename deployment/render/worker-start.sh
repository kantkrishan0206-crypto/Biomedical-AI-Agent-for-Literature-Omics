#!/usr/bin/env bash
set -euo pipefail
echo "[biomedical-ai] $0"
celery -A app.workers.celery_app.celery_app worker --loglevel=INFO
