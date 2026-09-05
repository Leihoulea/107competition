"""Local-only scientific knowledge action; it never contacts a compute host."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from ..tool_specs import TOOL_SPECS
from .retrieve import retrieve_scientific_knowledge


_FORBIDDEN_PATH_PARTS = {"evaluator_private", "hidden", "repair_landscape", "historical_validation", "ground_truth"}


class ScientificKnowledgeTool:
    def __init__(self, corpus_root: Path | None = None) -> None:
        self.corpus_root = (corpus_root or Path.cwd() / "knowledge").resolve()
        if any(part.lower() in _FORBIDDEN_PATH_PARTS for part in self.corpus_root.parts):
            raise ValueError("knowledge corpus path may not be evaluator-private material")
        self.index_path = self.corpus_root / "index" / "bm25.json"
        if not self.index_path.is_file():
            raise FileNotFoundError(f"knowledge index not found: {self.index_path}")

    @staticmethod
    def _arguments(arguments: dict[str, Any]) -> tuple[str, int]:
        query = arguments.get("query")
        top_k = arguments.get("top_k", 5)
        if not isinstance(query, str) or not query.strip():
            raise ValueError("knowledge query must be a non-empty string")
        if type(top_k) is not int or not 1 <= top_k <= 5:
            raise ValueError("knowledge top_k must be an integer in [1, 5]")
        return query.strip(), top_k

    def execute(self, arguments: dict[str, Any]) -> dict[str, Any]:
        query, top_k = self._arguments(arguments)
        hits = retrieve_scientific_knowledge(query, top_k=top_k, index_path=self.index_path)
        return {
            "tool": "retrieve_scientific_knowledge",
            "category": "knowledge_query",
            "cost": TOOL_SPECS["retrieve_scientific_knowledge"].cost,
            "query": query,
            "top_k": top_k,
            "hits": [
                {
                    "source_id": hit.source_id,
                    "title": hit.title,
                    "authority": hit.authority,
                    "version": hit.version,
                    "section": hit.section,
                    "page": hit.page,
                    "chunk_id": hit.chunk_id,
                    "excerpt": hit.text,
                    "retrieval_score": hit.score,
                }
                for hit in hits
            ],
        }
