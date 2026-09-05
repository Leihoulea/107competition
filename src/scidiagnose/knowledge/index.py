"""Small local BM25 index; intentionally no database or embedding dependency."""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from .models import KnowledgeChunk, KnowledgeHit


# Separators may occur within a scientific identifier (e.g. ``L2/3``), but
# trailing sentence punctuation must never become part of a lexical token.
_TOKEN = re.compile(r"[A-Za-z0-9_]+(?:[./+-][A-Za-z0-9_]+)*")
_AUTHORITY_PRIORITY = {"official": 4, "peer_reviewed": 3, "project_documentation": 2, "project_note": 1}


def tokenize(text: str) -> list[str]:
    return [item.lower() for item in _TOKEN.findall(text)]


@dataclass(frozen=True)
class KnowledgeIndex:
    chunks: list[KnowledgeChunk]

    def search(self, query: str, top_k: int = 5, filters: dict[str, str] | None = None) -> list[KnowledgeHit]:
        if top_k < 1:
            raise ValueError("top_k must be positive")
        query_terms = tokenize(query)
        if not query_terms:
            return []
        filters = filters or {}
        eligible = [chunk for chunk in self.chunks if all(str(getattr(chunk, key, "")) == str(value) for key, value in filters.items())]
        if not eligible:
            return []
        tokens = [tokenize(chunk.text) for chunk in eligible]
        document_frequency = Counter(term for document in tokens for term in set(document))
        average_length = sum(len(document) for document in tokens) / len(tokens)
        hits: list[KnowledgeHit] = []
        for chunk, document in zip(eligible, tokens):
            frequencies = Counter(document); score = 0.0
            for term in query_terms:
                if term not in frequencies:
                    continue
                idf = math.log(1 + (len(tokens) - document_frequency[term] + 0.5) / (document_frequency[term] + 0.5))
                score += idf * (frequencies[term] * 2.0) / (frequencies[term] + 1.2 * (1 - 0.75 + 0.75 * len(document) / average_length))
            if score:
                hits.append(KnowledgeHit(chunk.source_id, chunk.title, chunk.section, chunk.page, chunk.text, round(score, 8), chunk.authority, chunk.version, chunk.chunk_id))
        return sorted(hits, key=lambda item: (-item.score, -_AUTHORITY_PRIORITY[item.authority], item.chunk_id))[:top_k]


def build_bm25_index(chunks: list[KnowledgeChunk], output_path: Path | None = None) -> KnowledgeIndex:
    """Persist the searchable chunk store; BM25 statistics are built at search time."""
    index = KnowledgeIndex(chunks=list(chunks))
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps({"schema_version": 1, "chunks": [item.to_dict() for item in chunks]}, indent=2), encoding="utf-8")
    return index


def load_bm25_index(path: Path) -> KnowledgeIndex:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("schema_version") != 1 or not isinstance(value.get("chunks"), list):
        raise ValueError("knowledge index must contain schema_version=1 and chunks")
    return KnowledgeIndex([KnowledgeChunk.from_dict(item) for item in value["chunks"]])
