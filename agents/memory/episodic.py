from __future__ import annotations

class MemoryStore:
    def __init__(self) -> None:
        self.records: list[dict] = []
    def add(self, record: dict) -> dict:
        self.records.append(record)
        return record
    def search(self, query: str) -> list[dict]:
        return [r for r in self.records if query.lower() in str(r).lower()]
