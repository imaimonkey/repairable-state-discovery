from __future__ import annotations

from collections import defaultdict
from typing import Any

import numpy as np

from repairable_diffusion.src.utils.io import save_json


def _predictor_lookup(predictor_payload: dict[str, Any]) -> dict[tuple[int, int, int], float]:
    out = {}
    for row in predictor_payload.get("scores", []):
        out[(row["item_id"], row["trajectory_id"], row["step_index"])] = float(row["score"])
    return out


def _select_step(
    selector: str,
    result: dict[str, Any],
    predictor_scores: dict[tuple[int, int, int], float],
    rng,
) -> dict[str, Any] | None:
    steps = result["step_results"]
    if not steps:
        return None
    if selector == "oracle":
        return max(steps, key=lambda x: x["correction_rate"])
    if selector == "random":
        return steps[int(rng.integers(0, len(steps)))]
    if selector == "confidence":
        return min(steps, key=lambda x: x["state_token_conf_mean"])
    if selector == "predictor":
        return max(
            steps,
            key=lambda x: predictor_scores.get(
                (result["item_id"], result["trajectory_id"], x["step_index"]),
                -1.0,
            ),
        )
    raise ValueError(f"Unsupported selector: {selector}")


def _select_success_step(
    selector: str,
    result: dict[str, Any],
    predictor_scores: dict[tuple[int, int, int], float],
    rng,
) -> dict[str, Any] | None:
    steps = result["step_results"]
    if not steps:
        return None
    if selector == "oracle":
        return min(steps, key=lambda x: x["degradation_rate"])
    if selector == "random":
        return steps[int(rng.integers(0, len(steps)))]
    if selector == "confidence":
        return min(steps, key=lambda x: x["state_token_conf_mean"])
    if selector == "predictor":
        return max(
            steps,
            key=lambda x: predictor_scores.get(
                (result["item_id"], result["trajectory_id"], x["step_index"]),
                -1.0,
            ),
        )
    raise ValueError(f"Unsupported selector: {selector}")


def _net_item_pass_at_k(
    trajectory_payload: dict[str, Any],
    trajectory_success_prob: dict[tuple[int, int], float],
) -> dict[int, float]:
    by_item: dict[int, list[float]] = defaultdict(list)
    for record in trajectory_payload["records"]:
        key = (int(record["item_id"]), int(record["trajectory_id"]))
        probability = trajectory_success_prob[key]
        by_item[int(record["item_id"])].append(float(probability))
    return {
        item_id: 1.0 - float(np.prod([1.0 - probability for probability in probabilities]))
        for item_id, probabilities in by_item.items()
    }


def evaluate_repair_selection(
    cfg: dict[str, Any],
    run_dir,
    trajectory_payload: dict[str, Any],
    oracle_payload: dict[str, Any],
    predictor_payload: dict[str, Any] | None,
) -> dict[str, Any]:
    predictor_scores = _predictor_lookup(predictor_payload or {})
    rng = np.random.default_rng(int(cfg["predictor"].get("random_state", 7)))
    selectors = cfg["evaluation"].get("selectors", [])

    base_pass1_by_item: dict[int, bool] = defaultdict(bool)
    base_passk_by_item: dict[int, bool] = defaultdict(bool)
    original_correct: dict[tuple[int, int], bool] = {}
    for record in trajectory_payload["records"]:
        item_id = int(record["item_id"])
        trajectory_id = int(record["trajectory_id"])
        correct = bool(record["correct"])
        original_correct[(item_id, trajectory_id)] = correct
        if trajectory_id == 0:
            base_pass1_by_item[item_id] = correct
        base_passk_by_item[item_id] = base_passk_by_item[item_id] or correct

    item_ids = sorted(base_passk_by_item.keys())
    failed_results_by_key = {
        (int(row["item_id"]), int(row["trajectory_id"])): row
        for row in oracle_payload.get("results", [])
    }
    success_results_by_key = {
        (int(row["item_id"]), int(row["trajectory_id"])): row
        for row in oracle_payload.get("success_results", [])
    }
    original_failed_keys = {key for key, correct in original_correct.items() if not correct}
    original_success_keys = {key for key, correct in original_correct.items() if correct}
    failed_probe_complete = set(failed_results_by_key) == original_failed_keys
    success_probe_complete = set(success_results_by_key) == original_success_keys
    net_metric_complete = failed_probe_complete and success_probe_complete

    selector_rows = []
    for selector in selectors:
        chosen = []
        unsolved_repair_probs: dict[int, list[float]] = defaultdict(list)
        trajectory_success_prob = {
            key: 1.0 if correct else 0.0 for key, correct in original_correct.items()
        }

        for result in oracle_payload.get("results", []):
            picked = _select_step(selector, result, predictor_scores, rng)
            if picked is None:
                continue
            key = (int(result["item_id"]), int(result["trajectory_id"]))
            correction_rate = float(picked["correction_rate"])
            trajectory_success_prob[key] = correction_rate
            chosen.append(
                {
                    "item_id": result["item_id"],
                    "trajectory_id": result["trajectory_id"],
                    "step_index": picked["step_index"],
                    "correction_rate": correction_rate,
                }
            )
            if not base_passk_by_item[int(result["item_id"])]:
                unsolved_repair_probs[int(result["item_id"])].append(correction_rate)

        correction_rate = (
            float(np.mean([row["correction_rate"] for row in chosen])) if chosen else 0.0
        )
        recovery_only_success_after = {}
        upper_bound_success_after = {}
        for item_id in item_ids:
            base_hit = 1.0 if base_passk_by_item[item_id] else 0.0
            if base_hit >= 1.0:
                recovery_only_success_after[item_id] = 1.0
                upper_bound_success_after[item_id] = 1.0
                continue
            probs = unsolved_repair_probs.get(item_id, [])
            recovery_only_success_after[item_id] = (
                1.0 - float(np.prod([1.0 - p for p in probs])) if probs else 0.0
            )
            upper_bound_success_after[item_id] = (
                1.0 if any(p > 0.0 for p in probs) else 0.0
            )

        recovery_only_item_passk = sum(recovery_only_success_after.values()) / max(
            1, len(item_ids)
        )
        expected_newly_solved = sum(
            recovery_only_success_after[item_id]
            for item_id in item_ids
            if not base_passk_by_item[item_id]
        )
        upper_bound_newly_solved = sum(
            upper_bound_success_after[item_id]
            for item_id in item_ids
            if not base_passk_by_item[item_id]
        )

        degradation_values = []
        success_chosen_count = 0
        for key, result in success_results_by_key.items():
            picked = _select_success_step(selector, result, predictor_scores, rng)
            if picked is None:
                continue
            degradation_rate = float(picked["degradation_rate"])
            trajectory_success_prob[key] = 1.0 - degradation_rate
            degradation_values.append(degradation_rate)
            success_chosen_count += 1

        base_item_pass_at_k = sum(
            int(base_passk_by_item[item_id]) for item_id in item_ids
        ) / max(1, len(item_ids))
        net_expected_item_pass_at_k = None
        net_policy_gain_over_base = None
        expected_lost_solved_items = None
        if net_metric_complete:
            net_item_values = _net_item_pass_at_k(
                trajectory_payload,
                trajectory_success_prob,
            )
            net_expected_item_pass_at_k = sum(net_item_values.values()) / max(
                1, len(item_ids)
            )
            net_policy_gain_over_base = net_expected_item_pass_at_k - base_item_pass_at_k
            expected_lost_solved_items = sum(
                1.0 - net_item_values[item_id]
                for item_id in item_ids
                if base_passk_by_item[item_id]
            )

        selector_rows.append(
            {
                "selector": selector,
                "failed_trajectory_correction_rate": correction_rate,
                "base_item_pass_at_1": sum(
                    int(base_pass1_by_item[item_id]) for item_id in item_ids
                )
                / max(1, len(item_ids)),
                "base_item_pass_at_k": base_item_pass_at_k,
                "expected_repaired_item_pass_at_k": recovery_only_item_passk,
                "recovery_only_expected_item_pass_at_k": recovery_only_item_passk,
                "expected_newly_solved_items": expected_newly_solved,
                "upper_bound_newly_solved_items": upper_bound_newly_solved,
                "negative_repair_rate": (
                    float(np.mean(degradation_values)) if degradation_values else None
                ),
                "net_metric_complete": net_metric_complete,
                "failed_probe_complete": failed_probe_complete,
                "success_probe_complete": success_probe_complete,
                "probed_success_trajectories": len(success_results_by_key),
                "total_success_trajectories": len(original_success_keys),
                "net_expected_item_pass_at_k": net_expected_item_pass_at_k,
                "net_policy_gain_over_base_pass_at_k": net_policy_gain_over_base,
                "expected_lost_solved_items": expected_lost_solved_items,
                "num_selected_trajectories": len(chosen),
                "num_selected_success_trajectories": success_chosen_count,
                "repair_branch_count": int(
                    oracle_payload.get("meta", {}).get("branch_count", 0)
                ),
            }
        )

    payload = {
        "evaluation_protocol": "crossfit_selector_with_net_damage_accounting",
        "selectors": selector_rows,
    }
    save_json(run_dir / "repair_selection_eval.json", payload)
    return payload
