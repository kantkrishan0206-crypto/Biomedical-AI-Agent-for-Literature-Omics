from __future__ import annotations


def record(payload: dict) -> dict:
    return {"component": "lineage", "recorded": True, "payload": payload}
