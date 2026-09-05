"""Section-aware deterministic text chunking."""
from __future__ import annotations

import re

from .models import KnowledgeChunk, KnowledgeSource


_HEADING = re.compile(r"^#{1,6}\s+(.+)$")
_PAGE = re.compile(r"^\[page:\s*(.+?)\s*\]$", re.IGNORECASE)
_NUMBERED_HEADING = re.compile(r"^\s*\d+(?:\.\d+){0,4}\s+[A-Z][A-Za-z0-9 ,:/()_+\-]{2,}$")


def chunk_scientific_text(source: KnowledgeSource, text: str, max_chars: int = 4000) -> list[KnowledgeChunk]:
    if max_chars < 800:
        raise ValueError("max_chars must be at least 800")
    section, page, buffer, chunks = "Document", None, [], []

    def flush() -> None:
        nonlocal buffer
        paragraph = "\n".join(buffer).strip()
        buffer = []
        if not paragraph:
            return
        # The normalized preamble is manifest-backed document metadata, not
        # scientific source content.  Do not create an unpaged PDF chunk from
        # it: every indexed PDF passage must retain its source page.
        if section == "Document metadata" and page is None:
            return
        paragraphs = [item.strip() for item in re.split(r"\n\s*\n", paragraph) if item.strip()]
        group: list[str] = []
        size = 0
        for item in paragraphs:
            if group and size + len(item) + 2 > max_chars:
                chunks.append((section, page, "\n\n".join(group)))
                group, size = [], 0
            if len(item) > max_chars:
                if group:
                    chunks.append((section, page, "\n\n".join(group)))
                    group, size = [], 0
                chunks.extend((section, page, item[offset:offset + max_chars].strip()) for offset in range(0, len(item), max_chars))
            else:
                group.append(item); size += len(item) + 2
        if group:
            chunks.append((section, page, "\n\n".join(group)))

    for line in text.splitlines():
        heading = _HEADING.match(line)
        page_match = _PAGE.match(line)
        if heading:
            flush(); section = heading.group(1).strip(); continue
        if page_match:
            flush(); page = page_match.group(1).strip(); continue
        if _NUMBERED_HEADING.match(line):
            flush(); section = line.strip(); continue
        buffer.append(line)
    flush()
    return [
        KnowledgeChunk(
            chunk_id=f"{source.source_id}:{index:04d}", source_id=source.source_id,
            title=source.title, section=item_section, page=item_page, version=source.version,
            authority=source.authority, domain=source.domain, product=source.product, text=body,
            page_start=int(item_page) if item_page and item_page.isdigit() else None,
            page_end=int(item_page) if item_page and item_page.isdigit() else None,
        )
        for index, (item_section, item_page, body) in enumerate(chunks, 1)
    ]
