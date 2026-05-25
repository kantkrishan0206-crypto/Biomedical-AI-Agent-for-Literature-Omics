"""Legal PubMed metadata ingestion utilities."""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import httpx


@dataclass
class IngestedRecord:
    source: str
    identifier: str
    title: str
    abstract: str
    source_url: str
    retrieved_at: str
    sha256: str
    license: str = "public metadata or abstract"


def fingerprint(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


async def fetch_metadata(query: str, limit: int = 10) -> list[IngestedRecord]:
    """Fetch public metadata. Network callers can replace params while preserving provenance."""
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.get(url, params={"term": query, "retmax": limit})
        payload = response.text[:2000]
    record = IngestedRecord(
        source="PubMed",
        identifier=f"pubmed:{fingerprint(query)[:12]}",
        title=f"PubMed metadata query: {query}",
        abstract=payload,
        source_url=url,
        retrieved_at=datetime.now(timezone.utc).isoformat(),
        sha256=fingerprint(payload),
    )
    return [record]


def write_records(records: Iterable[IngestedRecord], output: Path) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(asdict(record)) + "\n")
    return output
