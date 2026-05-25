from __future__ import annotations


def record(payload: dict) -> dict:
    return {"component": "metrics", "recorded": True, "payload": payload}
