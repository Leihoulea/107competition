# v0.3 RAG ablation contract

The B/C comparison changes exactly one capability: C permits the planner to select `retrieve_scientific_knowledge`; B does not expose that action. Both cohorts run the same planner implementation, unchanged scientific system prompt, ordered compute tool specifications, public task inputs, budget/max-steps, evidence/validation gates, model settings, and deterministic seed/temperature settings.

`retrieve_scientific_knowledge` costs one budget unit through the shared `ToolSpec` catalog. It reads only the frozen local `knowledge/index/bm25.json`, returns provenance-rich passages, and does not access case directories, evaluator-private material, repair landscapes, historical validation artifacts, or remote upload code. The remote upload allowlist remains the three public arrays plus the remote runner.

Report B and C separately with: case ID, cohort, model/provider configuration, budget/max-steps, knowledge-query count and cost, compute action count/cost, experimental evidence IDs, knowledge evidence IDs, final decision, and stop reason. Do not compare a C run against a B run with altered prompts, transforms, ordering, cases, thresholds, or validation logic.
