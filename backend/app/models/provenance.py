from __future__ import annotations

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, TimestampMixin


class ProvenanceRecord(TimestampMixin, Base):
    __tablename__ = "provenance_records"
    subject_id: Mapped[str] = mapped_column(String(128), index=True)
    subject_type: Mapped[str] = mapped_column(String(64), index=True)
    sha256: Mapped[str] = mapped_column(String(128), default="")
    manifest: Mapped[dict] = mapped_column(JSON, default=dict)
