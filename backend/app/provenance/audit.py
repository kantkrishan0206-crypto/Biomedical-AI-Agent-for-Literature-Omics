from __future__ import annotations


def build(payload: dict) -> dict:
    return {"component": "audit", "provenance_attached": True, "payload": payload}
