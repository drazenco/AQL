# aql_core/server.py
from fastapi import FastAPI
from pydantic import BaseModel
from .memory import MemoryStore

app = FastAPI(title="AQL API (Draft)")
store = MemoryStore(similarity_threshold=0.2)

class ImprintReq(BaseModel):
    text: str
    context: dict | None = None
    meta: dict | None = None

class SurfaceReq(BaseModel):
    query: str
    k: int = 10
    return_prob: bool = False
    lam: float = 10.0

class DissolveReq(BaseModel):
    id: str

@app.post("/aql/imprint")
def aql_imprint(req: ImprintReq):
    im = store.IMPRINT(req.text, context=req.context, meta=req.meta)
    return {"id": im.id, "t": im.t, "context": im.context}

@app.post("/aql/surface")
def aql_surface(req: SurfaceReq):
    return {"items": store.SURFACE(req.query, return_prob=req.return_prob, lam=req.lam, k=req.k)}

@app.post("/aql/dissolve")
def aql_dissolve(req: DissolveReq):
    store.DISSOLVE(req.id)
    return {"ok": True}
