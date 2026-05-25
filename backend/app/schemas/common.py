from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class APIMessage(BaseModel):
    message: str


class Page(BaseModel):
    items: list[Any]
    total: int


class Timestamped(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None


class EvidenceItem(BaseModel):
    pmid: str
    title: str
    source: str
    year: int | None = None
    score: float = Field(ge=0, le=1)
    summary: str
