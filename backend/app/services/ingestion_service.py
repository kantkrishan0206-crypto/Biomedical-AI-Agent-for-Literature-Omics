from __future__ import annotations

import hashlib
from datetime import datetime, timezone


class IngestionService:
    async def register_upload(self, filename: str, content: bytes, project_id: str) -> dict:
        digest = hashlib.sha256(content).hexdigest()
        return {
            "dataset_id": f"dataset-{digest[:12]}",
            "project_id": project_id,
            "filename": filename,
            "sha256": digest,
            "provenance": {
                "source": "user_upload",
                "created_at": datetime.now(timezone.utc).isoformat(),
                "licensing_status": "user_attested",
            },
        }
