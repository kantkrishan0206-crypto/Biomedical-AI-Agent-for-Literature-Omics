from __future__ import annotations


def process(payload: dict) -> dict:
    return {"component": "exports", "notebook_versioned": True, "payload": payload}
