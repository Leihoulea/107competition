# SciDiagnose knowledge corpus

The first MSG/SEVIRI batch retains immutable inputs in `sources/raw/` and stores page-marked extraction output in `sources/normalized/`. Every manifest entry includes authority, publisher, version, retrieval date, raw and normalized SHA-256, domain, product, and a usage note. Only manifest-declared cleaned `.txt` or `.md` files are indexed; raw PDFs are processed by the dedicated `pypdf` ingestion script and are never indexed directly. LLM-generated text is not a knowledge source.

Run `python scripts/ingest_meteosat_knowledge.py --normalize`, then `python scripts/run_knowledge_smoke_test.py` to rebuild the first batch's corpus, BM25 index, inventory, and retrieval report. Retrieval returns passages only; create a `KnowledgeEvidence` record explicitly before any future graph integration. The corpus intentionally contains no evaluator ground truth or historical repair label; any repair remains experimental evidence, not knowledge evidence.
