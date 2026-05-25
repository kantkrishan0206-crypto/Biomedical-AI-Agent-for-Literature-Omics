from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ExperimentRequest(BaseModel):
    name: str | None = None
    query: str | None = None
    project_id: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


class ExperimentResponse(BaseModel):
    id: str
    status: str = "ok"
    data: dict[str, Any] = Field(default_factory=dict)
