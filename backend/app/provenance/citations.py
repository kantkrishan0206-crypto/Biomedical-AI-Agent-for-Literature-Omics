from __future__ import annotations


def build(payload: dict) -> dict:
    return {"component": "citations", "provenance_attached": True, "payload": payload}
