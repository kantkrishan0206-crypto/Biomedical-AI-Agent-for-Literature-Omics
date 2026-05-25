from __future__ import annotations

def build(payload: dict) -> dict:
    return {"component": "execution_log", "payload": payload, "status": "ready"}
