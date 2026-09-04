"""Section-aware deterministic text chunking."""
from __future__ import annotations

import re

from .models import KnowledgeChunk, KnowledgeSource


_HEADING = re.compile(r"^#{1,6}\s+(.+)$")
_PAGE = re.compile(r"^\[page:\s*(.+?)\s*\]$", re.IGNORECASE)


def chunk_scientific_text(source: KnowledgeSource, text: str, max_chars: int = 1200) -> list[KnowledgeChunk]:
    if max_chars < 200:
        raise ValueError("max_chars must be at least 200")
    section, page, buffer, chunks = "Document", None, [], []

    def flush() -> None:
        nonlocal buffer
        paragraph = "\n".join(buffer).strip()
        buffer = []
        if not paragraph:
            return
        for offset in range(0, len(paragraph), max_chars):
            body = paragraph[offset:offset + max_chars].strip()
            if body:
                chunks.append((section, page, body))

    for line in text.splitlines():
        heading = _HEADING.match(line)
        page_match = _PAGE.match(line)
        if heading:
            flush(); section = heading.group(1).strip(); continue
        if page_match:
            flush(); page = page_match.group(1).strip(); continue
        buffer.append(line)
    flush()
    return [
        KnowledgeChunk(
            chunk_id=f"{source.source_id}:{index:04d}", source_id=source.source_id,
            title=source.title, section=item_section, page=item_page, version=source.version,
            authority=source.authority, domain=source.domain, product=source.product, text=body,
        )
        for index, (item_section, item_page, body) in enumerate(chunks, 1)
    ]
