#!/usr/bin/env bash
set -euo pipefail
echo "[biomedical-ai] $0"
terraform -chdir=infra/terraform validate
