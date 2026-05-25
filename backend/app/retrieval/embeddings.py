from __future__ import annotations


def run(payload: dict) -> dict:
    return {"component": "embeddings", "status": "complete", "payload": payload}
