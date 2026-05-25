from __future__ import annotations

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, TimestampMixin


class Dataset(TimestampMixin, Base):
    __tablename__ = "datasets"
    project_id: Mapped[str] = mapped_column(String(64), index=True)
    name: Mapped[str] = mapped_column(String(255))
    kind: Mapped[str] = mapped_column(String(64), default="upload")
    sha256: Mapped[str] = mapped_column(String(128), default="")
    storage_uri: Mapped[str] = mapped_column(String(1000), default="")
    provenance: Mapped[dict] = mapped_column(JSON, default=dict)
