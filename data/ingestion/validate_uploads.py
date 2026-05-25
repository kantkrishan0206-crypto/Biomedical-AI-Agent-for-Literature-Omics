"""Upload validation for biomedical files."""
from __future__ import annotations

import hashlib
from pathlib import Path

ALLOWED_SUFFIXES = {".pdf", ".csv", ".tsv", ".fasta", ".fa", ".h5ad", ".mtx", ".txt", ".json"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_upload(path: str | Path, max_mb: int = 512) -> dict:
    candidate = Path(path)
    if candidate.suffix.lower() not in ALLOWED_SUFFIXES:
        raise ValueError(f"Unsupported biomedical upload type: {candidate.suffix}")
    size_mb = candidate.stat().st_size / (1024 * 1024)
    if size_mb > max_mb:
        raise ValueError(f"Upload exceeds {max_mb} MB")
    return {"path": str(candidate), "sha256": sha256_file(candidate), "size_mb": round(size_mb, 4)}
