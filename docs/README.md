# README

This document describes the production v1 design for the Biomedical AI Agent for Literature + Omics.

Key principles:

- Research-grade scientific validity, reproducibility, and citation grounding.
- SaaS deployment through Vercel frontend, Render backend, PostgreSQL, Upstash Redis, Qdrant, and Ollama.
- WSL2/Linux-first development with Docker-native execution.
- Environment-driven secrets, RBAC, audit trails, workspace isolation, and provenance.

The implementation favors deterministic contracts, typed APIs, event-driven workflows, benchmark records, and operational telemetry.
