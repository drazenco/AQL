# AQL Roadmap (v0.1 → v0.3)

## v0.1 (this repo)
- Core primitives: IMPRINT, SURFACE (prob), DISSOLVE
- Minimal in-memory backend (no deps)
- OpenAPI draft for /aql endpoints
- Python & JS SDK skeletons
- Conformance tests (smoke)

## v0.2
- Temporal filters: SINCE/UNTIL/WINDOW
- Context filters: FILTER context.*
- Pluggable embeddings (provider interface)
- pgvector adapter (prod-grade example)

## v0.3
- Federated AQL (HTTP fan-out + merge)
- Utility hook (U) interface & sample re-ranker
- Observability: request-id, latencies, top-k histograms
