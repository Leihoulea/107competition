"""Named truth-blind baseline adapters used by the benchmark harness."""
from __future__ import annotations

from typing import Any, Callable

from .harness import BenchmarkHarness, PublicCase


class DirectLLMBaseline:
    """One public-context model call, with no fabricated experiment records."""
    name = "direct_llm"
    def __init__(self, llm: Callable[[dict[str, Any]], dict[str, Any]]) -> None: self.llm = llm
    def run(self, case: PublicCase, repeat: int) -> dict[str, Any]: return BenchmarkHarness(self.llm).direct_llm(case, repeat)


class OneShotLLMBaseline:
    """Model chooses one allowed operation; its observed public metric is retained."""
    name = "one_shot_llm"
    def __init__(self, llm: Callable[[dict[str, Any]], dict[str, Any]]) -> None: self.llm = llm
    def run(self, case: PublicCase, repeat: int) -> dict[str, Any]: return BenchmarkHarness(self.llm).one_shot_llm(case, repeat)


class DeterministicTransformSweepBaseline:
    """Enumerates the fixed public transform set without a model."""
    name = "deterministic_transform_sweep"
    def run(self, case: PublicCase, repeat: int) -> dict[str, Any]: return BenchmarkHarness().deterministic_transform_sweep(case, repeat)


class DeterministicFullSearchBaseline:
    """Enumerates the public transform-plus-shift search space without a model."""
    name = "deterministic_full_search"
    def run(self, case: PublicCase, repeat: int) -> dict[str, Any]: return BenchmarkHarness().deterministic_full_search(case, repeat)


# Kept as an import-compatible name for existing downstream scripts.
DeterministicExhaustiveBaseline = DeterministicTransformSweepBaseline
