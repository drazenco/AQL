# aql_core/ops.py
from .memory import MemoryStore

def imprint(store: MemoryStore, text: str, context=None, meta=None):
    return store.IMPRINT(text, context=context, meta=meta)

def surface(store: MemoryStore, query: str, return_prob=False, lam: float = 10.0, k: int = 10):
    return store.SURFACE(query, return_prob=return_prob, lam=lam, k=k)

def dissolve(store: MemoryStore, iid: str):
    return store.DISSOLVE(iid)
