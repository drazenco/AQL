# sdk/python/aql/client.py
import requests

class AQLClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url.rstrip("/")

    def imprint(self, text: str, context=None, meta=None):
        return requests.post(f"{self.base_url}/aql/imprint", json={"text": text, "context": context, "meta": meta}).json()

    def surface(self, query: str, k: int = 10, return_prob: bool = False, lam: float = 10.0):
        return requests.post(f"{self.base_url}/aql/surface", json={"query": query, "k": k, "return_prob": return_prob, "lam": lam}).json()

    def dissolve(self, id: str):
        return requests.post(f"{self.base_url}/aql/dissolve", json={"id": id}).json()
