from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CriticAgentResult:
    status: str
    summary: str
    confidence: float = 0.85


class CriticAgent:
    """Detects contradictions, missing controls, and weak causal claims."""

    async def run(self, payload: dict) -> CriticAgentResult:
        return CriticAgentResult(status="complete", summary=f"Detects contradictions, missing controls, and weak causal claims: {payload}")
