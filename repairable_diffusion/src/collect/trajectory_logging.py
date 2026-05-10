from __future__ import annotations

from collections import defaultdict
from typing import Any

from tqdm import tqdm

from repairable_diffusion.src.data.math_bench import load_dataset_records
from repairable_diffusion.src.utils.io import save_json, save_jsonl, save_pickle


def collect_trajectories(cfg: dict[str, Any], run_dir, backend) -> dict[str, Any]:
    dataset = load_dataset_records(cfg["dataset"])
    trajectories_per_item = int(cfg["generation"]["trajectories_per_item"])
    records: list[dict[str, Any]] = []
    light_rows: list[dict[str, Any]] = []

    for item in tqdm(dataset, desc="collect-trajectories"):
        for trajectory_id in range(trajectories_per_item):
            record = backend.generate_trajectory(item, trajectory_id=trajectory_id, generation_cfg=cfg["generation"])
            records.append(record)
            light_rows.append(
                {
                    "item_id": record["item_id"],
                    "trajectory_id": record["trajectory_id"],
                    "correct": record["correct"],
                    "final_answer": record["final_answer"],
                    "gold_answer": record["gold_answer"],
                }
            )

    sample_accuracy = sum(1 for r in records if r["correct"]) / max(1, len(records))
    by_item: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_item[record["item_id"]].append(record)

    item_pass_at_1_hits = 0
    item_pass_at_k_hits = 0
    solved_item_ids_pass1 = []
    solved_item_ids_passk = []
    for item_id, rows in sorted(by_item.items()):
        rows = sorted(rows, key=lambda x: x["trajectory_id"])
        hit1 = bool(rows[0]["correct"]) if rows else False
        hitk = any(bool(row["correct"]) for row in rows)
        item_pass_at_1_hits += int(hit1)
        item_pass_at_k_hits += int(hitk)
        if hit1:
            solved_item_ids_pass1.append(item_id)
        if hitk:
            solved_item_ids_passk.append(item_id)

    payload = {
        "meta": {
            "dataset_name": cfg["dataset"]["name"],
            "dataset_path": cfg["dataset"]["path"],
            "dataset_size": len(dataset),
            "trajectories_per_item": trajectories_per_item,
            "num_records": len(records),
            "sample_accuracy": sample_accuracy,
            "item_pass_at_1": item_pass_at_1_hits / max(1, len(dataset)),
            "item_pass_at_k": item_pass_at_k_hits / max(1, len(dataset)),
            "solved_item_ids_pass1": solved_item_ids_pass1,
            "solved_item_ids_passk": solved_item_ids_passk,
        },
        "records": records,
    }
    save_pickle(run_dir / "trajectories.pkl", payload)
    save_jsonl(run_dir / "trajectories.light.jsonl", light_rows)
    save_json(run_dir / "trajectory_summary.json", payload["meta"])
    return payload
