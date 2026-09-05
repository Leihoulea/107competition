"""Conservative normalization for text sources before indexing."""
from __future__ import annotations

import re


def clean_scientific_text(raw: str) -> str:
    """Remove simple markup while retaining headings, units, and page labels."""
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    # Preserve provenance markers before removing ordinary markup.  The
    # normalized document retains the HTML comment; the indexer receives this
    # stable bracket form and records it as chunk page metadata.
    text = re.sub(r"<!--\s*source_page:\s*(\d+)\s*-->", r"[page: \1]", text, flags=re.IGNORECASE)
    # Do not use ``<[^>]+>`` here: PDF-extracted mathematical relations such
    # as ``a < b`` can span lines and would erase scientific content.  Remove
    # only conventional, single-line HTML tags.
    text = re.sub(r"</?[A-Za-z][A-Za-z0-9]*(?:\s+[^<>\n]*)?/?>", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
