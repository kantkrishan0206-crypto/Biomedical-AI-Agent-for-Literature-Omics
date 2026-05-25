#!/usr/bin/env bash
set -euo pipefail
echo "[biomedical-ai] $0"
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
