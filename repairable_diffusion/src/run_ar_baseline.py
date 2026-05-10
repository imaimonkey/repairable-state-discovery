from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from tqdm import tqdm

from repairable_diffusion.src.backends.factory import create_backend
from repairable_diffusion.src.data.math_bench import load_dataset_records
from repairable_diffusion.src.utils.io import init_run_dir, load_json, load_pickle, load_yaml, save_json, save_jsonl, save_pickle


def _final_payload_if_present(run_dir: Path) -> dict[str, Any] | None:
    summary_path = run_dir / "ar_baseline_summary.json"
    payload_path = run_dir / "ar_baseline.pkl"
    if not summary_path.exists():
        return None
    summary = load_json(summary_path)
    if payload_path.exists():
        return load_pickle(payload_path)
    return {"meta": summary, "records": []}


def _progress_payload_if_present(run_dir: Path) -> dict[str, Any] | None:
    progress_path = run_dir / "ar_baseline.progress.pkl"
    if not progress_path.exists():
        return None
    return load_pickle(progress_path)


def _build_summary(rows: list[dict[str, Any]], *, dataset_size: int, sample_count: int, model_path: str) -> dict[str, Any]:
    ordered_rows = sorted(rows, key=lambda row: int(row["item_id"]))
    pass1_hits = 0
    passk_hits = 0
    solved_item_ids_pass1 = []
    solved_item_ids_passk = []
    for result in ordered_rows:
        sample_correct = [bool(sample["correct"]) for sample in result["samples"]]
        hit1 = bool(sample_correct[0]) if sample_correct else False
        hitk = bool(any(sample_correct))
        pass1_hits += int(hit1)
        passk_hits += int(hitk)
        if hit1:
            solved_item_ids_pass1.append(result["item_id"])
        if hitk:
            solved_item_ids_passk.append(result["item_id"])

    return {
        "dataset_size": dataset_size,
        "samples_per_item": sample_count,
        "pass_at_1": pass1_hits / max(1, dataset_size),
        "pass_at_k": passk_hits / max(1, dataset_size),
        "model_path": model_path,
        "solved_item_ids_pass1": solved_item_ids_pass1,
        "solved_item_ids_passk": solved_item_ids_passk,
    }


def _save_progress(
    run_dir: Path,
    *,
    rows: list[dict[str, Any]],
    light_rows: list[dict[str, Any]],
    dataset_size: int,
    sample_count: int,
    model_path: str,
) -> None:
    ordered_rows = sorted(rows, key=lambda row: int(row["item_id"]))
    ordered_light_rows = sorted(light_rows, key=lambda row: int(row["item_id"]))
    completed_items = len(ordered_rows)
    pass1_hits = sum(int(bool(row["correct_at_1"])) for row in ordered_light_rows)
    passk_hits = sum(int(bool(row["correct_at_k"])) for row in ordered_light_rows)
    progress_payload = {
        "meta": {
            "dataset_size": dataset_size,
            "samples_per_item": sample_count,
            "model_path": model_path,
            "completed_items": completed_items,
            "partial_pass_at_1_over_completed": pass1_hits / max(1, completed_items),
            "partial_pass_at_k_over_completed": passk_hits / max(1, completed_items),
        },
        "rows": ordered_rows,
        "light_rows": ordered_light_rows,
    }
    save_pickle(run_dir / "ar_baseline.progress.pkl", progress_payload)
    save_json(run_dir / "ar_baseline.progress.json", progress_payload["meta"])


def run_ar_baseline(cfg: dict[str, Any], run_dir: Path) -> dict[str, Any]:
    run_dir.mkdir(parents=True, exist_ok=True)
    save_json(run_dir / "config.snapshot.json", cfg)

    final_payload = _final_payload_if_present(run_dir)
    if final_payload is not None:
        return final_payload

    backend = create_backend(cfg["backend"])
    dataset = load_dataset_records(cfg["dataset"])
    sample_count = int(cfg["backend"].get("samples_per_item", cfg.get("samples_per_item", 8)))
    base_seed = int(cfg.get("base_seed", 11))
    model_path = cfg["backend"]["model_path"]

    progress_payload = _progress_payload_if_present(run_dir)
    rows = list(progress_payload.get("rows", [])) if progress_payload else []
    light_rows = list(progress_payload.get("light_rows", [])) if progress_payload else []
    completed_item_ids = {int(row["item_id"]) for row in rows}
    pending_items = [item for item in dataset if int(item["item_id"]) not in completed_item_ids]

    for item in tqdm(pending_items, desc="ar-baseline", initial=len(completed_item_ids), total=len(dataset)):
        result = backend.generate_samples(item, sample_count=sample_count, base_seed=base_seed + item["item_id"] * 100)
        rows.append(result)
        sample_correct = [bool(sample["correct"]) for sample in result["samples"]]
        light_rows.append(
            {
                "item_id": result["item_id"],
                "correct_at_1": bool(sample_correct[0]) if sample_correct else False,
                "correct_at_k": bool(any(sample_correct)),
            }
        )
        _save_progress(
            run_dir,
            rows=rows,
            light_rows=light_rows,
            dataset_size=len(dataset),
            sample_count=sample_count,
            model_path=model_path,
        )

    ordered_rows = sorted(rows, key=lambda row: int(row["item_id"]))
    ordered_light_rows = sorted(light_rows, key=lambda row: int(row["item_id"]))
    summary = _build_summary(ordered_rows, dataset_size=len(dataset), sample_count=sample_count, model_path=model_path)
    payload = {"meta": summary, "records": ordered_rows}
    save_pickle(run_dir / "ar_baseline.pkl", payload)
    save_jsonl(run_dir / "ar_baseline.light.jsonl", ordered_light_rows)
    save_json(run_dir / "ar_baseline_summary.json", summary)
    (run_dir / "ar_baseline.progress.pkl").unlink(missing_ok=True)
    (run_dir / "ar_baseline.progress.json").unlink(missing_ok=True)
    return payload


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-dir", default=None)
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    cfg = load_yaml(args.config)
    run_dir = Path(args.run_dir) if args.run_dir else init_run_dir(cfg)
    payload = run_ar_baseline(cfg, run_dir)
    print(f"[ar-baseline] done: {run_dir}")
    print(f"[ar-baseline] summary: {run_dir / 'ar_baseline_summary.json'}")
    print(f"[ar-baseline] pass@1: {payload['meta']['pass_at_1']:.4f}")


if __name__ == "__main__":
    main()
