# Data Architecture

The data layer separates legal source material, processed artifacts, caches, samples, and metadata.

- `raw/`: user-provided uploads and legally retrieved public metadata. Large files stay out of Git.
- `processed/`: normalized matrices, manifests, and analysis outputs.
- `cache/`: temporary downloads, embedding caches, and workflow caches.
- `samples/`: tiny legal fixtures used by tests and local demos.
- `metadata/`: source registry, refresh rules, licensing, provenance schemas, and dataset manifest templates.

The platform does not bundle copyrighted full text. Public ingestion uses metadata, abstracts, legal APIs, open datasets, and user-provided files. Every dataset is fingerprinted with SHA256 and linked to provenance before it can be used by retrieval, agents, reports, or notebooks.
