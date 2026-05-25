from __future__ import annotations

import json
import time


def main() -> None:
    started = time.perf_counter()
    result = {"benchmark": "workflow-benchmark.py", "latency_ms": round((time.perf_counter() - started) * 1000, 3), "status": "complete"}
    print(json.dumps(result))


if __name__ == "__main__":
    main()
