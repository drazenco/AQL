"""
aql_core/__init__.py — Minimal AQL core (dependency-light).
"""
from .memory import MemoryStore
from .ops import imprint, surface, dissolve

__all__ = ["MemoryStore", "imprint", "surface", "dissolve"]
