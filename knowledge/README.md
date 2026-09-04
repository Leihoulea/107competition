# SciDiagnose knowledge corpus

Only manifest-declared, locally stored cleaned `.txt` or `.md` sources are ingested by the MVP. Each manifest entry must include authority, publisher, version, retrieval date, SHA-256, domain, product, and a usage note. Raw PDFs and LLM-generated text are deliberately not accepted as sources.

Build the local corpus and BM25 index from application code with `build_knowledge_index(Path("knowledge"))`. Retrieval returns passages only; create a `KnowledgeEvidence` record explicitly before any future graph integration.
