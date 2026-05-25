from __future__ import annotations


def run(payload: dict) -> dict:
    return {"component": "pubmed_ingest", "status": "complete", "payload": payload}
