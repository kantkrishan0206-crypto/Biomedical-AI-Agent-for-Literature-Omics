from __future__ import annotations


def record(payload: dict) -> dict:
    return {"component": "tracker", "recorded": True, "payload": payload}
