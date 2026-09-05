# R01 no-RAG baseline report

## Frozen benchmark identity

- Integration commit: `c90b87d6166679b0f107693da5a9cbe7f6b50bc8` (`benchmark: integrate and freeze R01 historical case`).
- Freeze tag: `r01-no-rag-baseline-freeze`.
- Case level: `historical_real_reconstructed`; provenance and historical-evidence boundary are in `cases_real/r01/evaluator_private/provenance.json` and `docs/R01_HISTORICAL_AUDIT.md`.
- Public case SHA-256: `8eec34174a6911c5078771bcb0ec400aaa6cb26c9d88894989acaef78494cfa3`.
- Public array SHA-256 values: reference `1d0498087227a63908b2207208e31d4796a3f68b2844590d7ac4657baedf7951`; target `798efef55c73a5635c264ad17bee1665ab8d8e84a47121b81ad94fbf7650c2a4`; valid mask `d68a32fca5b06ac815707bd9beb34e98e6f239a856883d54dbfebc4602fdd498`.
- Evaluator ground-truth SHA-256: `9e42f733c16abf26a64753f64c902cfb6647aeb721a6a91ffff1f5dcf7a2be3e`.
- Frozen remote runner SHA-256: `0498e8d88ec4d54a35e10a990108772176caa05d3d740cde135bf02126f55083`.

## Case and deterministic validation

The public initial agreement is `0.5368982307` on `9,515,524` valid pixels (`0.6905844` of the native grid). The evaluator-private validator recomputed every frozen single-transform control from the public arrays. The diagnostic candidate scored `0.7982679672`; the second-best control scored `0.5605946661`, a separation of `0.2376733010`. Every control retained `9,515,524` valid pixels. Reconstructed before/after values are within `0.01` of the historical references.

The transform label is an executable benchmark diagnostic, not a claim about a production product mutation. The historical production remediation remains evaluator-private navigation handling evidence.

## Deterministic baselines

| Method | Candidates | Best public candidate | Agreement | Budget equivalent | Wall time | CPU / remote jobs |
|---|---:|---|---:|---:|---:|---|
| Transform Sweep | 7 | single diagnostic transform | 0.7982679672 | 28 | 0.409774 s | not instrumented / 0 |
| Full Search | 847 | diagnostic transform then shift `(4, 1)` | 0.8094529529 | 4235 | 70.373104 s | not instrumented / 0 |

The deterministic artifacts are in `benchmark/results/R01_TRANSFORM_SWEEP/` and `benchmark/results/R01_FULL_SEARCH/`. The full-search action space is the frozen 7 transforms × 11 row shifts × 11 column shifts; it was not changed for R01.

## Frozen SciDiagnose no-RAG cohort

### Protocol

Every attempt used the same frozen commit, public case, school OpenAI-compatible API configuration (`deepseek-v4-flash`, `temperature=0`), SSH Direct on `server-114`, `budget=30`, and `max_steps=8`. No RAG data, evaluator-private artifact, corrected target, or deterministic-search result was presented to the Agent or uploaded remotely.

The protocol allowed at most eight attempts and targeted three attempts with a completed final diagnosis. The target was reached at attempt 06, so attempts 07–08 were not started. All six attempts, including failures, are retained below.

### A. End-to-end operational reliability (all attempts)

| Run | Operational status | Experiments | Budget used | Remote jobs | Remote wall | Remote CPU | Peak memory |
|---|---|---:|---:|---:|---:|---:|---:|
| `R01_V022_NORAG_01` | failed: API connection reset after `EXP_001` | 1 | 1 | 1 | 0.666664 s | 0.654129 s | 191.8125 MB |
| `R01_V022_NORAG_02` | failed: hypothesis count violated the 2–5 schema before execution | 0 | 0 | 0 | — | — | — |
| `R01_V022_NORAG_03` | completed: final `inconclusive` | 8 | 26 | 8 | 2.433613 s | 3.455024 s | 191.8125 MB |
| `R01_V022_NORAG_04` | completed: final `inconclusive` | 8 | 26 | 8 | 2.011874 s | 2.897798 s | 191.785156 MB |
| `R01_V022_NORAG_05` | failed: reflection response used unsupported `response` wrapper after `EXP_004` | 4 | 16 | 4 | 0.784797 s | 1.312831 s | 157.027344 MB |
| `R01_V022_NORAG_06` | completed: final `inconclusive` | 8 | 26 | 8 | 2.065500 s | 2.745305 s | 191.808594 MB |

Operational completion is **3 / 6 = 50.0%**. Failures 01, 02, and 05 remain in the denominator: API transport, structured-output non-compliance, and response-wrapper incompatibility are all end-to-end reliability outcomes, not network-only exclusions.

### B. Conditional scientific performance (completed final diagnoses only)

| Run | Final decision | Fault family | Evidence reaching 0.75 | Evaluator total |
|---|---|---|---|---:|
| `R01_V022_NORAG_03` | `inconclusive` | `null` | none | 0.0 / 100 |
| `R01_V022_NORAG_04` | `inconclusive` | `null` | none | 0.0 / 100 |
| `R01_V022_NORAG_06` | `inconclusive` | `null` | none | 0.0 / 100 |

Conditional fault detection, fault-family identification, and validated repair are each **0 / 3**. This is not a claim that the three attempts were operational failures; it is the no-RAG scientific baseline result under the frozen policy.

### Trace interpretation

Run 03 tested small shifts, `flip_x`, identity comparison, `rot90`, and transpose, but never tested `rot180` (the deterministic sweep's clearly separated single-transform candidate). Its reflection inferred that the masks were correctly oriented because `rot90` and transpose reduced agreement. That inference is unsupported: without testing `rot180`, those negative results cannot establish that orientation is correct. This is retained as an observed experiment-selection/evidence-interpretation failure, not repaired by prompt tuning.

Runs 04 and 06 also used eight real remote experiments without producing a validated repair. All three completed runs stopped at the eight-step limit with 4 budget units remaining. The frozen graph reports this state as `budget_exhausted` / “available budget ended”, although the operative constraint was `max_steps=8`, not exhausted budget. This is recorded only as a v0.3 generic semantics backlog: `stop_reason = budget_exhausted | max_steps_reached | no_affordable_novel_action`. It was not changed in the R01 baseline.

The deterministic full search finding of `rot180` followed by shift `(4, 1)` at `0.8094529529` does not invalidate the historical orientation/navigation root-cause family: it shows that the reconstructed comparison grid can retain a small registration residual. Future evaluation should distinguish root-cause family from metric-optimal repair pipeline rather than require an exact `rot180`-only answer.

Each attempt directory contains its trace and compute summary; completed attempts contain `state.json`, `final.json`, and a scored `evaluator.json`; failed attempts contain `run_failure.json` and an explicitly `not_scored` evaluator artifact.

## Failure analysis and frozen-Agent proof

The cohort records provider transport instability (01), provider schema non-compliance (02), reflection-wrapper incompatibility (05), and repeated hypothesis generation / experiment-selection / evidence-interpretation failures in the completed runs (03, 04, 06). These are benchmark observations, not targets for prompt tuning. `git diff v0.2.2-agent-freeze..c90b87d -- src/scidiagnose/agent.py src/scidiagnose/diagnosis_graph.py` is empty: no frozen Agent prompt, planner, reflection, validation, search policy, or experiment-selection policy was modified for R01.

No RAG implementation, new scientific tool, or UI work was started. The no-RAG cohort is complete and ready for integration review.
