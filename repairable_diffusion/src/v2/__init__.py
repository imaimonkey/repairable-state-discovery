"""V2 counterfactual state-level recoverability utilities.

This package is intentionally isolated from the legacy V1 pipeline. V1 artifacts
remain historical evidence; V2 code should write only into the v2_measurement
namespace declared by the scientific contract.
"""

from .contracts import (
    CONTRACT_VERSION,
    DECODER_STATE_SCHEMA_VERSION,
    BranchPlan,
    MeasurementSpec,
    ProbeOperatorSpec,
    deterministic_branch_seed,
    validate_contract_dict,
)
from .metrics import (
    RecoverabilitySummary,
    bernoulli_rate,
    last_repairable_step,
    paired_branch_item_pass_at_k,
    repairability_survival,
    summarize_state,
)

__all__ = [
    "CONTRACT_VERSION",
    "DECODER_STATE_SCHEMA_VERSION",
    "BranchPlan",
    "MeasurementSpec",
    "ProbeOperatorSpec",
    "RecoverabilitySummary",
    "bernoulli_rate",
    "deterministic_branch_seed",
    "last_repairable_step",
    "paired_branch_item_pass_at_k",
    "repairability_survival",
    "summarize_state",
    "validate_contract_dict",
]
