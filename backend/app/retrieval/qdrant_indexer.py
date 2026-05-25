from __future__ import annotations


def run(payload: dict) -> dict:
    return {"component": "qdrant_indexer", "status": "complete", "payload": payload}
