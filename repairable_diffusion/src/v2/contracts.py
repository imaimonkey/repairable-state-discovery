from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Any, Iterable


CONTRACT_VERSION = "v2_counterfactual_recoverability"
DECODER_STATE_SCHEMA_VERSION = "v2.0"


@dataclass(frozen=True)
class ProbeOperatorSpec:
    operator_id: str
    position_policy: str
    remask_fraction: float
    min_remask_positions: int
    continuation_temperature: float | str
    schedule_mode: str = "phase_faithful"

    def validate(self) -> None:
        if not self.operator_id:
            raise ValueError("operator_id must be non-empty")
        if not 0.0 <= float(self.remask_fraction) <= 1.0:
            raise ValueError("remask_fraction must lie in [0, 1]")
        if int(self.min_remask_positions) < 0:
            raise ValueError("min_remask_positions must be non-negative")
        if self.schedule_mode not in {"phase_faithful", "native", "recompute_active_phase"}:
            raise ValueError(f"unsupported schedule_mode: {self.schedule_mode}")


@dataclass(frozen=True)
class BranchPlan:
    localization_count: int
    confirmation_count: int
    require_disjoint_seed_sets: bool = True

    def validate(self) -> None:
        if self.localization_count <= 0 or self.confirmation_count <= 0:
            raise ValueError("localization_count and confirmation_count must be positive")


@dataclass(frozen=True)
class MeasurementSpec:
    confirmation_threshold: float = 0.25
    threshold_sensitivity: tuple[float, ...] = (0.125, 0.25, 0.5)

    def validate(self) -> None:
        values = (self.confirmation_threshold, *self.threshold_sensitivity)
        if any(not 0.0 <= value <= 1.0 for value in values):
            raise ValueError("repairability thresholds must lie in [0, 1]")


def deterministic_branch_seed(
    *,
    root_seed: int,
    item_id: int,
    trajectory_id: int,
    step_index: int,
    branch_index: int,
    stage: str,
) -> int:
    """Derive stable, stage-separated branch seeds.

    Localization and confirmation seeds are intentionally in disjoint namespaces.
    The hash construction avoids accidental overlap caused by simple additive formulas.
    """

    if stage not in {"localization", "confirmation", "policy", "compute_control"}:
        raise ValueError(f"unsupported seed stage: {stage}")
    payload = (
        f"{CONTRACT_VERSION}|{root_seed}|{item_id}|{trajectory_id}|"
        f"{step_index}|{branch_index}|{stage}"
    ).encode("utf-8")
    digest = sha256(payload).digest()
    # Keep the result inside the signed 31-bit range accepted by all RNGs we use.
    return int.from_bytes(digest[:8], "big") % (2**31 - 1)


def assert_disjoint(localization_seeds: Iterable[int], confirmation_seeds: Iterable[int]) -> None:
    overlap = set(localization_seeds) & set(confirmation_seeds)
    if overlap:
        raise ValueError(f"localization/confirmation seed overlap: {sorted(overlap)[:5]}")


def validate_contract_dict(cfg: dict[str, Any]) -> None:
    if cfg.get("version") != CONTRACT_VERSION:
        raise ValueError(f"expected version={CONTRACT_VERSION}, got {cfg.get('version')}")
    if cfg.get("artifact_namespace") != "v2_measurement":
        raise ValueError("V2 must use artifact_namespace=v2_measurement")

    branches = cfg.get("branches", {})
    plan = BranchPlan(
        localization_count=int(branches.get("localization_count", 0)),
        confirmation_count=int(branches.get("confirmation_count", 0)),
        require_disjoint_seed_sets=bool(branches.get("require_disjoint_seed_sets", True)),
    )
    plan.validate()
    if branches.get("replicate_semantics") != "stochastic_seed_only":
        raise ValueError("V2 branches must vary stochastic_seed_only")

    measurement = cfg.get("measurement", {})
    spec = MeasurementSpec(
        confirmation_threshold=float(measurement.get("confirmation_threshold", 0.25)),
        threshold_sensitivity=tuple(float(x) for x in measurement.get("threshold_sensitivity", [])),
    )
    spec.validate()

    operator = cfg.get("canonical_operator", {})
    op = ProbeOperatorSpec(
        operator_id=str(operator.get("id", "")),
        position_policy=str(operator.get("position_policy", "")),
        remask_fraction=float(operator.get("remask_fraction", -1.0)),
        min_remask_positions=int(operator.get("min_remask_positions", -1)),
        continuation_temperature=operator.get("continuation_temperature", "match_base"),
        schedule_mode=str(operator.get("schedule_mode", "")),
    )
    op.validate()

    required_controls = {
        "native_continuation",
        "matched_stochastic_continuation",
        "random_position_remask",
        "low_confidence_remask_v2",
        "fresh_sampling_compute_control",
        "core",
    }
    present = set(cfg.get("operator_controls", {}).get("required", []))
    missing = required_controls - present
    if missing:
        raise ValueError(f"missing required V2 operator/control rows: {sorted(missing)}")

    learned = cfg.get("selectors", {}).get("learned", {})
    if not bool(learned.get("require_oof_for_headline", False)):
        raise ValueError("headline learned selector must require grouped OOF scores")
    if learned.get("group_key") != "item_id":
        raise ValueError("V2 cross-fitting must group by item_id")

    compute_cfg = cfg.get("compute", {})
    if not bool(compute_cfg.get("actual_fresh_sampling_required", False)):
        raise ValueError("actual fresh-sampling compute control is required")
    if bool(compute_cfg.get("analytic_extra_sampling_proxy_main_result", True)):
        raise ValueError("analytic extra-sampling proxy cannot be a V2 main result")
