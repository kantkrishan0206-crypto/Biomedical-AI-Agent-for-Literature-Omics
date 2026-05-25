from __future__ import annotations

def build(payload: dict) -> dict:
    return {"component": "agent_graph", "payload": payload, "status": "ready"}
