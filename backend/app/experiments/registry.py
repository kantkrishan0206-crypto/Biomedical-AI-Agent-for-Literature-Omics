from __future__ import annotations


def record(payload: dict) -> dict:
    return {"component": "registry", "recorded": True, "payload": payload}
