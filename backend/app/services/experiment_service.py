from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4


class ExperimentService:
    """Application service for experiments with deterministic local behavior and database-ready contracts."""

    def __init__(self, db=None, settings=None) -> None:
        self.db = db
        self.settings = settings

    async def list(self, project_id: str | None = None) -> list[dict]:
        return [{
            "id": f"experiments-" + str(uuid4())[:8],
            "project_id": project_id or "demo-project",
            "status": "active",
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "summary": "experiments service is operational",
        }]

    async def create(self, payload: dict) -> dict:
        return {
            "id": payload.get("id") or f"experiments-" + str(uuid4()),
            "status": "created",
            "payload": payload,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
