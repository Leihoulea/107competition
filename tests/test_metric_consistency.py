import json
from pathlib import Path

import numpy as np

from remote.run_experiment import metrics


def test_initial_and_candidate_share_valid_region_metric_definition():
    data = Path(__file__).resolve().parents[1] / "cases" / "b02" / "public" / "data"
    initial = json.loads((data.parents[1] / "initial_result.json").read_text())
    observed = metrics(np.load(data / "reference.npy"), np.load(data / "target_faulty.npy"), np.load(data / "target_valid.npy"))
    assert observed["agreement_valid"] == initial["agreement_valid"]
    assert observed["agreement"] == observed["agreement_valid"]
    assert observed["agreement_all"] != observed["agreement_valid"]
