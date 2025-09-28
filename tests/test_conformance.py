# tests/test_conformance.py
from aql_core.memory import MemoryStore

def test_imprint_surface_dissolve_smoke():
    s = MemoryStore(similarity_threshold=0.0)
    a = s.IMPRINT("alpha memory", context={"user":1})
    b = s.IMPRINT("beta memory", context={"user":1})
    res = s.SURFACE("alpha", return_prob=False, k=2)
    assert any(r["id"] == a.id for r in res)
    s.DISSOLVE(a.id)
    res2 = s.SURFACE("alpha", return_prob=False, k=2)
    assert all(r["id"] != a.id for r in res2)
