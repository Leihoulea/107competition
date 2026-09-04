"""Lightweight, auditable scientific-knowledge retrieval.

Retrieval is deliberately separate from the diagnosis graph.  A retrieved
passage is not evidence until an explicit KnowledgeEvidence record is made.
"""

from .evidence import knowledge_evidence_from_hit
from .index import KnowledgeIndex, build_bm25_index, load_bm25_index
from .retrieve import retrieve_scientific_knowledge

__all__ = [
    "KnowledgeIndex",
    "build_bm25_index",
    "knowledge_evidence_from_hit",
    "load_bm25_index",
    "retrieve_scientific_knowledge",
]
