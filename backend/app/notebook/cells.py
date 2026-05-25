from __future__ import annotations


def process(payload: dict) -> dict:
    return {"component": "cells", "notebook_versioned": True, "payload": payload}
