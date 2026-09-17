from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class RecoverabilitySummary:
    observed_correct: bool
    q_native: float
    q_repair: float
    intervention_lift: float
    category: str


def bernoulli_rate(outcomes: Sequence[bool | int]) -> float:
    if not outcomes:
        raise ValueError("at least one branch outcome is required")
    return sum(int(bool(x)) for x in outcomes) / len(outcomes)


def summarize_state(*, observed_correct: bool, native_outcomes: Sequence[bool | int], repair_outcomes: Sequence[bool | int], eps: float = 1e-12) -> RecoverabilitySummary:
    q_native = bernoulli_rate(native_outcomes)
    q_repair = bernoulli_rate(repair_outcomes)
    delta = q_repair - q_native

    if observed_correct:
        category = "transient_correct"
    elif q_native > eps and q_repair > eps:
        category = "native_and_intervention_recoverable"
    elif q_native > eps:
        category = "native_recoverable_only"
    elif q_repair > eps:
        category = "repairable_but_not_native"
    else:
        category = "unconfirmed_recoverable"

    return RecoverabilitySummary(
        observed_correct=bool(observed_correct),
        q_native=q_native,
        q_repair=q_repair,
        intervention_lift=delta,
        category=category,
    )


def last_repairable_step(step_to_rate: Mapping[int, float], *, threshold: float) -> int | None:
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must lie in [0, 1]")
    eligible = [int(step) for step, rate in step_to_rate.items() if float(rate) >= threshold]
    return max(eligible) if eligible else None


def repairability_survival(last_steps: Iterable[int | None], checkpoints: Sequence[int]) -> list[dict[str, float | int]]:
    values = list(last_steps)
    denom = len(values)
    if denom == 0:
        return [{"step_index": int(step), "survival": 0.0, "count": 0} for step in checkpoints]
    rows = []
    for step in sorted(int(x) for x in checkpoints):
        alive = sum(1 for value in values if value is not None and int(value) >= step)
        rows.append({"step_index": step, "survival": alive / denom, "count": alive})
    return rows


def category_rates(categories: Iterable[str]) -> dict[str, float]:
    values = list(categories)
    counts = Counter(values)
    denom = max(1, len(values))
    return {key: value / denom for key, value in sorted(counts.items())}


def paired_branch_item_pass_at_k(items: Mapping[int, Sequence[Sequence[bool | int]]]) -> float:
    """Estimate prospective item pass@k by branch-level simulation.

    `items[item_id][trajectory_index][branch_index]` is the post-policy correctness
    for that trajectory and branch replicate. All trajectories for an item must
    expose the same number of branch replicates. This avoids multiplying marginal
    trajectory probabilities under an independence assumption.
    """

    if not items:
        return 0.0
    item_values = []
    for trajectories in items.values():
        if not trajectories:
            item_values.append(0.0)
            continue
        branch_counts = {len(branches) for branches in trajectories}
        if len(branch_counts) != 1:
            raise ValueError("all trajectories for an item must share branch count")
        branch_count = next(iter(branch_counts))
        if branch_count <= 0:
            raise ValueError("branch count must be positive")
        branch_hits = []
        for branch_index in range(branch_count):
            hit = any(bool(trajectory[branch_index]) for trajectory in trajectories)
            branch_hits.append(float(hit))
        item_values.append(sum(branch_hits) / branch_count)
    return sum(item_values) / len(item_values)
