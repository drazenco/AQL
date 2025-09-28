# AQL — Agent Query Language (v0.1, Draft)
**Status:** Developer Preview · **Scope:** Neutral, AI-native memory query layer built on *questions*, not imperative commands.

AQL treats every query as a **question** and returns a **distribution** of relevant memories (imprints). It is designed to sit **above** GMQL/Genesis (or any memory kernel) via clean adapters.

---

## ✨ Why AQL?
- **Interrogative form:** Agents think in *questions*.
- **Probabilistic retrieval:** Distributions > deterministic rows.
- **Pluggable backends:** pgvector, Milvus/Weaviate, SQLite (demo).
- **Privacy-first hooks:** consent/audit come from the kernel, AQL respects them.
- **Federation-ready:** fan-out to multiple memory kernels, merge by ranking.

> AQL is *neutral*. It does not include app-specific semantics.

---

## 📦 Packages
- `aql-core/` — core primitives, ranking, query model
- `adapters/` — storage and kernel adapters (pgvector, milvus, http-federation)
- `sdk/python/`, `sdk/js/` — client SDKs
- `examples/` — runnable demos
- `spec/` — language spec & OpenAPI
- `tests/` — conformance & smoke tests

---

## 🚀 Quickstart
```bash
# 1) Run Python demo (no external deps)
python examples/minimal_python_demo.py

# 2) Run API server (FastAPI, optional)
uvicorn aql_core.server:app --reload

# 3) Query (curl)
curl -s http://localhost:8000/aql/surface -X POST -H 'Content-Type: application/json' -d '{
  "query": "What is Genesis v2?",
  "k": 3,
  "return_prob": true
}'
```

---

## 🧠 Concepts
- **IMPRINT** — store memory with context → (vector, time, meta)
- **SURFACE** — surface relevant imprints (cosine → softmax dist.)
- **DISSOLVE** — forget + remove relations
- **Utility hook (U)** — optional re-ranking interface (kept neutral)

See `spec/AQL_SPEC_v0.1.md`

---

## 🧪 Conformance
- `tests/` includes minimal checks for: imprint → surface → prob → dissolve.
- Backends must pass **AQL Conformance v0.1** to use the badge.

---

## 🗺️ Roadmap
See `ROADMAP.md` for v0.1 → v0.3 and AQL API stabilization milestones.

---

## 📚 Draft Papers
- [AQL ↔ GMQL Manifest (draft)](./AQL_GMQL_Manifest_Draft.pdf)
- [Seed Ideas Library](./Seed_Ideas_Library.pdf)

---

## 📜 License
MIT. See `LICENSE`.
