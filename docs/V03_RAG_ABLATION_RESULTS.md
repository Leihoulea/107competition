# v0.3 frozen RAG ablation results

## Freeze and common contract

All completed runs used frozen commit `015fe10d35d256c344a1affa656ce55391c8905f`, case `R01`, public-input SHA-256 set recorded in each `run_metadata.json`, provider `manual`, model `deepseek-v4-flash`, temperature `0`, budget `30`, and `max_steps` `8`.

The B/C distinction is only the action-space gate: B disables `retrieve_scientific_knowledge`; C enables the same action at the shared ToolSpec cost of one budget unit. The planner, scientific prompt, compute ToolSpecs and ordering, public case inputs, validation/evidence semantics, and execution backend are otherwise the shared contract captured in each run's metadata.

The frozen knowledge-manifest SHA-256 for C is `04c27565b2e30a7c19495406c89626d1fb6ab580d313201b1945c897c3624bf5`. B intentionally has no corpus access and records `knowledge_manifest_sha256: null`.

## Completed runs

| Cohort | Run ID | Compute actions / cost | Knowledge queries / cost | Experimental / knowledge evidence | Decision | Stop reason |
|---|---|---:|---:|---:|---|---|
| B | `R01_V03_B_01` | 8 / 29 | 0 / 0 | 8 / 0 | inconclusive | `max_steps_reached` |
| B | `R01_V03_B_02` | 7 / 28 | 0 / 0 | 7 / 0 | inconclusive | `budget_exhausted` |
| B | `R01_V03_B_03` | 8 / 26 | 0 / 0 | 8 / 0 | inconclusive | `max_steps_reached` |
| C | `R01_V03_C_01_RETRY1` | 5 / 20 | 3 / 3 | 5 / 13 | inconclusive | `max_steps_reached` |
| C | `R01_V03_C_02` | 5 / 20 | 3 / 3 | 5 / 15 | inconclusive | `max_steps_reached` |
| C | `R01_V03_C_03` | 5 / 20 | 1 / 1 | 5 / 3 | fault (0.90) | decision reached |

`R01_V03_C_03` is supported by experimental evidence `E005`: `rot180` changed `agreement_valid` from `0.5368982307227642` to `0.7982679671660752`, exceeding the `0.75` threshold. Its knowledge query addressed whether the baseline agreement might be a normal Meteosat/EPIC range; the retrieved chunks did not support that no-fault hypothesis. The final result keeps experimental evidence (`E001`–`E005`) and knowledge evidence (`K001`–`K003`) separately; it does not claim that any document prescribed a 180-degree rotation.

## Failure accounting

`R01_V03_C_01` ended before a plan was produced with the explicit artifact `run_failure.json`: `AgentAPIError: School LLM API transport failed: Remote end closed connection without response`. It is excluded from the six completed-run comparison and preserved alongside the successful retry `R01_V03_C_01_RETRY1`; no code, prompt, case, budget, or model setting changed for the retry.

## Interpretation boundary

This is a three-run-per-cohort observation, not a causal performance claim. B produced zero fault decisions (0/3); C produced one (1/3). The successful C decision is computationally supported, but the small sample and one recorded provider failure mean the result should not be reported as proof that RAG caused the repair discovery. The run traces and state snapshots are included under `artifacts/v03_rag_ablation_freeze/runs/` for independent audit.
