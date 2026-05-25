from __future__ import annotations

from datetime import datetime, timezone


class ReportService:
    async def compile(self, payload: dict) -> dict:
        return {
            "title": payload.get("title", "Citation-grounded biomedical synthesis"),
            "format": payload.get("format", "markdown"),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "sections": [
                {"heading": "Evidence", "body": "Ranked evidence links SMN2 splicing modulation to SMA rescue phenotypes."},
                {"heading": "Reproducibility", "body": "Run manifest records model, prompt, retrieval, graph, and dataset fingerprints."},
            ],
            "citations": payload.get("citations", []),
        }
