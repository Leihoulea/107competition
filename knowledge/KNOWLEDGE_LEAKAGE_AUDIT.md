# Knowledge Corpus Leakage Audit

## Scope

The audit searched only corpus-bearing inputs and artifacts:

- `knowledge/manifest.json`
- `knowledge/sources/normalized/*.md`
- `knowledge/corpus/chunks.json`
- `knowledge/index/bm25.json`

Raw retained source files are immutable source records and are not transformed or searched as project-authored corpus content.

## Evaluator/project-term check

| Searched term | Matches | Assessment |
| --- | ---: | --- |
| `rot180` | 0 | No project repair operation present. |
| `known_repair` | 0 | No evaluator decision present. |
| `ground_truth` | 0 | No evaluator truth present. |
| `R01` | 0 | No historical-case identifier present. |
| `validated_repair` | 0 | No validation outcome present. |
| `navigation_error` | 0 | No project diagnosis label present. |

## Result

No project-internal diagnosis, evaluator truth, benchmark identity, or repair outcome is present in the manifest, normalized source corpus, chunk store, or persisted BM25 chunk store. This is also enforced by an automated test.
