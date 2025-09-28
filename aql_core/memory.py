# aql_core/memory.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
import math, time, uuid
from collections import defaultdict

def _tokenize(text: str):
    return [t.lower() for t in "".join(ch if ch.isalnum() else " " for ch in text).split() if t]

class VocabEmbedder:
    """Toy bag-of-words embedder (replace with real provider in adapters)."""
    def __init__(self):
        self.vocab: Dict[str, int] = {}

    def embed(self, text: str) -> List[float]:
        vec = [0.0] * len(self.vocab)
        toks = _tokenize(text)
        # grow vocab
        for tok in toks:
            if tok not in self.vocab:
                self.vocab[tok] = len(self.vocab)
                vec.append(0.0)
        if len(vec) < len(self.vocab):
            vec.extend([0.0] * (len(self.vocab) - len(vec)))
        for tok in toks:
            vec[self.vocab[tok]] += 1.0
        # L2 norm
        norm = math.sqrt(sum(x*x for x in vec)) or 1.0
        return [x / norm for x in vec]

def cosine(a: List[float], b: List[float]) -> float:
    n = min(len(a), len(b))
    if n == 0: return 0.0
    dot = sum(a[i]*b[i] for i in range(n))
    na = math.sqrt(sum(a[i]*a[i] for i in range(n))) or 1.0
    nb = math.sqrt(sum(b[i]*b[i] for i in range(n))) or 1.0
    return dot / (na * nb)

def softmax(xs, lam: float = 10.0):
    if not xs: return []
    scaled = [lam * x for x in xs]
    m = max(scaled)
    exps = [math.exp(x - m) for x in scaled]
    s = sum(exps) or 1.0
    return [e/s for e in exps]

@dataclass
class Imprint:
    id: str
    text: str
    v: List[float]
    t: float
    context: Dict[str, Any] = field(default_factory=dict)
    meta: Dict[str, Any] = field(default_factory=dict)

class MemoryStore:
    def __init__(self, similarity_threshold: float = 0.25):
        self.embedder = VocabEmbedder()
        self.items: Dict[str, Imprint] = {}
        self.edges: Dict[str, List[str]] = defaultdict(list)
        self.similarity_threshold = similarity_threshold

    def IMPRINT(self, text: str, context=None, meta=None) -> Imprint:
        context = context or {}
        meta = meta or {}
        v = self.embedder.embed(text)
        iid = str(uuid.uuid4())
        imp = Imprint(id=iid, text=text, v=v, t=time.time(), context=context, meta=meta)
        self.items[iid] = imp
        # simple linking by user
        user = str(context.get("user",""))
        if user:
            last = self._last_by_user(user, exclude=iid)
            if last:
                self.edges[last].append(iid)
        return imp

    def SURFACE(self, query: str, return_prob=False, lam: float = 10.0, k: int = 10):
        qv = self.embedder.embed(query)
        scored = []
        for iid, imp in self.items.items():
            sim = cosine(qv, imp.v)
            if sim >= self.similarity_threshold:
                scored.append((iid, sim))
        scored.sort(key=lambda x: x[1], reverse=True)
        top = scored[:k]
        if not return_prob:
            return [{"id": iid, "similarity": sim, "text": self.items[iid].text, "context": self.items[iid].context} for iid, sim in top]
        probs = softmax([sim for _, sim in top], lam=lam)
        return [
            {"id": iid, "similarity": sim, "prob": p, "text": self.items[iid].text, "context": self.items[iid].context}
            for (iid, sim), p in zip(top, probs)
        ]

    def DISSOLVE(self, iid: str):
        if iid in self.items:
            del self.items[iid]
        for src in list(self.edges.keys()):
            self.edges[src] = [x for x in self.edges[src] if x != iid]
        if iid in self.edges:
            del self.edges[iid]

    def _last_by_user(self, user: str, exclude: Optional[str] = None) -> Optional[str]:
        xs = [im for im in self.items.values() if str(im.context.get("user","")) == user and im.id != exclude]
        if not xs: return None
        return max(xs, key=lambda im: im.t).id
