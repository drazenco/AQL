# examples/minimal_python_demo.py
from aql_core.memory import MemoryStore

def main():
    store = MemoryStore(similarity_threshold=0.2)
    a = store.IMPRINT("Genesis v2 is an AI-native memory kernel with GMQL.", context={"user": 42})
    b = store.IMPRINT("GMQL provides STORE, RECALL, FORGET, CONSENT.", context={"user": 42})
    c = store.IMPRINT("AQL treats queries as questions and returns probability distributions.", context={"user": 7})
    print("Imprinted:", a.id, b.id, c.id)
    print("-- SURFACE no-prob --")
    print(store.SURFACE("What is Genesis v2?", return_prob=False, k=3))
    print("-- SURFACE with PROB --")
    print(store.SURFACE("How does GMQL work?", return_prob=True, k=3))

if __name__ == "__main__":
    main()
