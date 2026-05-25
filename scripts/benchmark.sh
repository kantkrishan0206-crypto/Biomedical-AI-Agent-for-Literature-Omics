#!/usr/bin/env bash
set -euo pipefail
echo "[biomedical-ai] $0"
python3 tests/benchmarks/retrieval-benchmark.py
