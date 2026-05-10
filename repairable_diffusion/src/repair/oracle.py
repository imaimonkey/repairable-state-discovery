from __future__ import annotations

from collections import defaultdict
from typing import Any

from tqdm import tqdm

from repairable_diffusion.src.utils.io import save_json


def _item_lookup(records: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    lookup = {}
    for record in records:
        if record["item_id"] not in lookup:
            lookup[record["item_id"]] = {
                "item_id": record["item_id"],
                "question": record["question"],
                "answer": record["gold_answer"],
            }
    return lookup


def run_oracle_repair(cfg: dict[str, Any], run_dir, backend, payload: dict[str, Any]) -> dict[str, Any]:
    records = payload["records"]
    item_lookup = _item_lookup(records)
    branch_count = len(cfg["repair"]["branch_temperatures"])
    min_step = int(cfg["generation"].get("min_oracle_step", 1))
    branch_seed_stride = int(cfg["repair"].get("branch_seed_stride", 1000))
    measure_negative_repair = bool(cfg.get("evaluation", {}).get("measure_negative_repair", False))
    max_success_trajectories = int(cfg.get("evaluation", {}).get("max_success_trajectories_for_negative_repair", 0))

    results: list[dict[str, Any]] = []
    gain_curve_buckets: dict[int, list[float]] = defaultdict(list)

    failed_records = [r for r in records if not r["correct"]]
    for record in tqdm(failed_records, desc="oracle-repair"):
        step_results = []
        for step in record["steps"]:
            snapshot = step.get("snapshot")
            if snapshot is None or int(step["step_index"]) < min_step:
                continue

            branches = []
            correct_count = 0
            base_seed = int(record["seed"]) + int(step["step_index"]) * branch_seed_stride
            item = item_lookup[record["item_id"]]
            for branch_index in range(branch_count):
                branch = backend.repair_from_snapshot(
                    item=item,
                    snapshot_dict=snapshot,
                    repair_cfg=cfg["repair"],
                    branch_index=branch_index,
                    base_seed=base_seed,
                    generation_cfg=cfg["generation"],
                )
                correct_count += int(branch["correct"])
                branches.append(branch)

            correction_rate = correct_count / max(1, branch_count)
            gain_curve_buckets[int(step["step_index"])].append(correction_rate)
            step_results.append(
                {
                    "step_index": step["step_index"],
                    "masked_ratio": step["masked_ratio"],
                    "state_token_conf_mean": step["state_token_conf_mean"],
                    "masked_entropy_mean": step["masked_entropy_mean"],
                    "answer_candidate": step["answer_candidate"],
                    "correction_rate": correction_rate,
                    "branches": branches,
                }
            )

        best = max(step_results, key=lambda x: x["correction_rate"], default=None)
        results.append(
            {
                "item_id": record["item_id"],
                "trajectory_id": record["trajectory_id"],
                "base_correct": record["correct"],
                "oracle_best_step": best["step_index"] if best else None,
                "oracle_best_gain": best["correction_rate"] if best else 0.0,
                "step_results": step_results,
            }
        )

    success_results: list[dict[str, Any]] = []
    if measure_negative_repair:
        success_records = [r for r in records if r["correct"]]
        if max_success_trajectories > 0:
            success_records = success_records[:max_success_trajectories]
        for record in tqdm(success_records, desc="negative-repair"):
            step_results = []
            for step in record["steps"]:
                snapshot = step.get("snapshot")
                if snapshot is None or int(step["step_index"]) < min_step:
                    continue

                branches = []
                correct_count = 0
                base_seed = int(record["seed"]) + int(step["step_index"]) * branch_seed_stride
                item = item_lookup[record["item_id"]]
                for branch_index in range(branch_count):
                    branch = backend.repair_from_snapshot(
                        item=item,
                        snapshot_dict=snapshot,
                        repair_cfg=cfg["repair"],
                        branch_index=branch_index,
                        base_seed=base_seed,
                        generation_cfg=cfg["generation"],
                    )
                    correct_count += int(branch["correct"])
                    branches.append(branch)

                preservation_rate = correct_count / max(1, branch_count)
                degradation_rate = 1.0 - preservation_rate
                step_results.append(
                    {
                        "step_index": step["step_index"],
                        "masked_ratio": step["masked_ratio"],
                        "state_token_conf_mean": step["state_token_conf_mean"],
                        "masked_entropy_mean": step["masked_entropy_mean"],
                        "answer_candidate": step["answer_candidate"],
                        "preservation_rate": preservation_rate,
                        "degradation_rate": degradation_rate,
                        "branches": branches,
                    }
                )

            safest = min(step_results, key=lambda x: x["degradation_rate"], default=None)
            success_results.append(
                {
                    "item_id": record["item_id"],
                    "trajectory_id": record["trajectory_id"],
                    "base_correct": record["correct"],
                    "oracle_safest_step": safest["step_index"] if safest else None,
                    "oracle_min_degradation": safest["degradation_rate"] if safest else 0.0,
                    "step_results": step_results,
                }
            )

    gain_curve = [
        {
            "step_index": step_index,
            "mean_correction_rate": sum(values) / max(1, len(values)),
            "count": len(values),
        }
        for step_index, values in sorted(gain_curve_buckets.items())
    ]
    payload_out = {
        "meta": {
            "failed_trajectories": len(failed_records),
            "successful_trajectories": sum(1 for r in records if r["correct"]),
            "branch_count": branch_count,
            "negative_repair_measured": measure_negative_repair,
        },
        "results": results,
        "success_results": success_results,
        "gain_curve": gain_curve,
    }
    save_json(run_dir / "oracle_repair.json", payload_out)
    return payload_out
