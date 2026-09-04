"""Conservative normalization for text sources before indexing."""
from __future__ import annotations

import re


def clean_scientific_text(raw: str) -> str:
    """Remove simple markup while retaining headings, units, and page labels."""
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
