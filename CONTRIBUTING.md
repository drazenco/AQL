# Contributing to AQL
Thanks for considering a contribution!

## Principles
- Neutral core (no app-specific semantics)
- Strict semver
- Conformance-first (tests before features)
- Adapters over forks

## Setup
- Python 3.10+
- Optional: Postgres + pgvector, or Milvus
- `pip install -r requirements.txt`

## Tests
```bash
pytest -q
```

## PR Checklist
- [ ] Tests added/updated
- [ ] Docs updated
- [ ] No breaking changes without semver bump
