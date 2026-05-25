from __future__ import annotations

from prometheus_client import Counter, Gauge, Histogram, generate_latest
from starlette.responses import Response

REQUESTS = Counter("biomed_http_requests_total", "HTTP requests", ["path", "method"])
WORKFLOW_RUNS = Counter("biomed_workflow_runs_total", "Workflow runs", ["status"])
AGENT_STEPS = Counter("biomed_agent_steps_total", "Agent step events", ["agent"])
INFERENCE_LATENCY = Histogram("biomed_inference_latency_seconds", "Ollama inference latency")
QUEUE_DEPTH = Gauge("biomed_queue_depth", "Scientific workflow queue depth")
GPU_UTILIZATION = Gauge("biomed_gpu_utilization_percent", "Reported GPU utilization")


def metrics_response() -> Response:
    return Response(generate_latest(), media_type="text/plain; version=0.0.4")
