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


def _select_step(selector: str, result: dict[str, Any], predictor_scores: dict[tuple[int, int, int], float], rng) -> dict[str, Any] | None:
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
            key=lambda x: predictor_scores.get((result["item_id"], result["trajectory_id"], x["step_index"]), -1.0),
        )
    raise ValueError(f"Unsupported selector: {selector}")


def _select_success_step(selector: str, result: dict[str, Any], predictor_scores: dict[tuple[int, int, int], float], rng) -> dict[str, Any] | None:
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
            key=lambda x: predictor_scores.get((result["item_id"], result["trajectory_id"], x["step_index"]), -1.0),
        )
    raise ValueError(f"Unsupported selector: {selector}")


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
    for record in trajectory_payload["records"]:
        if record["trajectory_id"] == 0:
            base_pass1_by_item[record["item_id"]] = bool(record["correct"])
        base_passk_by_item[record["item_id"]] = base_passk_by_item[record["item_id"]] or bool(record["correct"])

    item_ids = sorted(base_passk_by_item.keys())
    success_results_by_key = {
        (row["item_id"], row["trajectory_id"]): row for row in oracle_payload.get("success_results", [])
    }

    selector_rows = []
    for selector in selectors:
        chosen = []
        unsolved_repair_probs: dict[int, list[float]] = defaultdict(list)
        for result in oracle_payload["results"]:
            picked = _select_step(selector, result, predictor_scores, rng)
            if picked is None:
                continue
            chosen.append(
                {
                    "item_id": result["item_id"],
                    "trajectory_id": result["trajectory_id"],
                    "step_index": picked["step_index"],
                    "correction_rate": picked["correction_rate"],
                }
            )
            if not base_passk_by_item[result["item_id"]]:
                unsolved_repair_probs[result["item_id"]].append(float(picked["correction_rate"]))

        correction_rate = float(np.mean([row["correction_rate"] for row in chosen])) if chosen else 0.0
        expected_success_after = {}
        upper_bound_success_after = {}
        for item_id in item_ids:
            base_hit = 1.0 if base_passk_by_item[item_id] else 0.0
            if base_hit >= 1.0:
                expected_success_after[item_id] = 1.0
                upper_bound_success_after[item_id] = 1.0
                continue
            probs = unsolved_repair_probs.get(item_id, [])
            expected_success_after[item_id] = 1.0 - float(np.prod([1.0 - p for p in probs])) if probs else 0.0
            upper_bound_success_after[item_id] = 1.0 if any(p > 0.0 for p in probs) else 0.0

        expected_item_passk = sum(expected_success_after.values()) / max(1, len(item_ids))
        expected_newly_solved = sum(expected_success_after[item_id] for item_id in item_ids if not base_passk_by_item[item_id])
        upper_bound_newly_solved = sum(upper_bound_success_after[item_id] for item_id in item_ids if not base_passk_by_item[item_id])

        negative_repair_rate = None
        success_chosen_count = 0
        if oracle_payload.get("success_results"):
            degradation_values = []
            for key, result in success_results_by_key.items():
                picked = _select_success_step(selector, result, predictor_scores, rng)
                if picked is None:
                    continue
                degradation_values.append(float(picked["degradation_rate"]))
                success_chosen_count += 1
            if degradation_values:
                negative_repair_rate = float(np.mean(degradation_values))

        selector_rows.append(
            {
                "selector": selector,
                "failed_trajectory_correction_rate": correction_rate,
                "base_item_pass_at_1": sum(int(base_pass1_by_item[item_id]) for item_id in item_ids) / max(1, len(item_ids)),
                "base_item_pass_at_k": sum(int(base_passk_by_item[item_id]) for item_id in item_ids) / max(1, len(item_ids)),
                "expected_repaired_item_pass_at_k": expected_item_passk,
                "expected_newly_solved_items": expected_newly_solved,
                "upper_bound_newly_solved_items": upper_bound_newly_solved,
                "negative_repair_rate": negative_repair_rate,
                "num_selected_trajectories": len(chosen),
                "num_selected_success_trajectories": success_chosen_count,
                "repair_branch_count": int(oracle_payload.get("meta", {}).get("branch_count", 0)),
            }
        )

    payload = {"selectors": selector_rows}
    save_json(run_dir / "repair_selection_eval.json", payload)
    return payload
