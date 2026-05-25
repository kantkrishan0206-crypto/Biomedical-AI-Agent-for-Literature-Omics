from __future__ import annotations


def process(payload: dict) -> dict:
    return {"component": "notebook_service", "notebook_versioned": True, "payload": payload}
