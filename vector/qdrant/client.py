from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ComponentRecord:
    name: str = "vector/qdrant/client"
    status: str = "ready"
    metadata: dict = field(default_factory=dict)
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


def run(payload: dict | None = None) -> dict:
    record = ComponentRecord(metadata=payload or {})
    return record.__dict__
