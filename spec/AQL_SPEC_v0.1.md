# 📜 Agent Query Language (AQL) v0.1 — Spec (Draft)
See also OpenAPI draft in `spec/openapi_aql.yaml`.

## Core
- **IMPRINT(x, c)** → (v, t, c, meta)
- **SURFACE(q)** → ranked set by cosine(f(q), v_i), optionally `PROB` via softmax
- **DISSOLVE(id)** → remove memory + relations

## Math
P(m_i | q) = softmax_lambda(cos(f(q), v_i))

## Extensibility
- Embedding providers
- Ranking providers
- Utility hook U(m, q, a)
