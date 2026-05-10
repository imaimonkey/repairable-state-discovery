from __future__ import annotations

import argparse
import copy
from collections import Counter
from pathlib import Path
from typing import Any

from repairable_diffusion.src.analysis.evaluate import evaluate_repair_selection
from repairable_diffusion.src.analysis.predictor import train_repair_predictor
from repairable_diffusion.src.backends.factory import create_backend
from repairable_diffusion.src.collect.trajectory_logging import collect_trajectories
from repairable_diffusion.src.repair.oracle import run_oracle_repair
from repairable_diffusion.src.utils.io import init_run_dir, load_json, load_pickle, load_yaml, save_json


def build_repairability_summary(oracle_payload: dict[str, Any] | None) -> dict[str, Any]:
    if not oracle_payload:
        return {}

    gain_curve = oracle_payload.get("gain_curve", [])
    peak_row = max(gain_curve, key=lambda row: row.get("mean_correction_rate", 0.0), default=None)
    positive_gain_rows = [row for row in gain_curve if float(row.get("mean_correction_rate", 0.0)) > 0.0]

    failed_results = oracle_payload.get("results", [])
    repairable_results = [
        row
        for row in failed_results
        if row.get("oracle_best_step") is not None and float(row.get("oracle_best_gain", 0.0)) > 0.0
    ]
    best_step_counts = Counter(int(row["oracle_best_step"]) for row in repairable_results if row.get("oracle_best_step") is not None)
    best_step_histogram = [
        {"step_index": step_index, "count": count}
        for step_index, count in sorted(best_step_counts.items())
    ]

    return {
        "repairable_failed_trajectories": len(repairable_results),
        "repairable_failed_rate": len(repairable_results) / max(1, len(failed_results)),
        "peak_step_index": peak_row.get("step_index") if peak_row else None,
        "peak_mean_correction_rate": peak_row.get("mean_correction_rate") if peak_row else 0.0,
        "earliest_positive_step": positive_gain_rows[0]["step_index"] if positive_gain_rows else None,
        "latest_positive_step": positive_gain_rows[-1]["step_index"] if positive_gain_rows else None,
        "best_step_histogram": best_step_histogram,
    }


def build_selector_deltas(evaluation_payload: dict[str, Any] | None) -> dict[str, Any]:
    if not evaluation_payload:
        return {}

    rows = {
        row["selector"]: row
        for row in evaluation_payload.get("selectors", [])
        if isinstance(row, dict) and "selector" in row
    }
    predictor = rows.get("predictor")
    oracle = rows.get("oracle")
    confidence = rows.get("confidence")
    random_row = rows.get("random")
    if not predictor:
        return {}

    out = {}
    out["predictor_gain_over_base_pass_at_k"] = (
        float(predictor["expected_repaired_item_pass_at_k"]) - float(predictor["base_item_pass_at_k"])
    )
    if oracle:
        out["oracle_minus_predictor_expected_pass_at_k"] = (
            float(oracle["expected_repaired_item_pass_at_k"]) - float(predictor["expected_repaired_item_pass_at_k"])
        )
        out["oracle_minus_predictor_expected_newly_solved"] = (
            float(oracle["expected_newly_solved_items"]) - float(predictor["expected_newly_solved_items"])
        )
    if confidence:
        out["predictor_minus_confidence_expected_pass_at_k"] = (
            float(predictor["expected_repaired_item_pass_at_k"]) - float(confidence["expected_repaired_item_pass_at_k"])
        )
    if random_row:
        out["predictor_minus_random_expected_pass_at_k"] = (
            float(predictor["expected_repaired_item_pass_at_k"]) - float(random_row["expected_repaired_item_pass_at_k"])
        )
    return out


def build_report(
    cfg: dict[str, Any],
    trajectories: dict[str, Any],
    oracle_payload: dict[str, Any] | None,
    predictor_payload: dict[str, Any] | None,
    evaluation_payload: dict[str, Any] | None,
) -> dict[str, Any]:
    headline = {}
    if evaluation_payload and evaluation_payload.get("selectors"):
        for selector_row in evaluation_payload["selectors"]:
            if selector_row["selector"] == "predictor":
                headline["predictor_selector"] = selector_row
            if selector_row["selector"] == "oracle":
                headline["oracle_selector"] = selector_row
    report = {
        "dataset": trajectories["meta"],
        "headline": headline,
        "repair_gain_curve": oracle_payload.get("gain_curve", []) if oracle_payload else [],
        "repairability_summary": build_repairability_summary(oracle_payload),
        "oracle_meta": oracle_payload.get("meta", {}) if oracle_payload else {},
        "predictor_metrics": predictor_payload.get("metrics", {}) if predictor_payload else {},
        "selection_eval": evaluation_payload.get("selectors", []) if evaluation_payload else [],
        "selector_deltas": build_selector_deltas(evaluation_payload),
        "artifacts": {
            "trajectories": "trajectories.pkl",
            "oracle_repair": "oracle_repair.json" if oracle_payload else None,
            "repair_predictor": "repair_predictor.json" if predictor_payload else None,
            "repair_selection_eval": "repair_selection_eval.json" if evaluation_payload else None,
        },
    }
    return report


def _load_if_exists(path: Path, loader) -> Any | None:
    if not path.exists():
        return None
    return loader(path)


def run_pipeline(cfg: dict[str, Any], run_dir: Path) -> dict[str, Any]:
    cfg_snapshot = copy.deepcopy(cfg)
    save_json(run_dir / "config.snapshot.json", cfg_snapshot)

    backend = create_backend(cfg["backend"])

    trajectories = _load_if_exists(run_dir / "trajectories.pkl", load_pickle)
    if trajectories is None:
        trajectories = collect_trajectories(cfg, run_dir, backend)

    oracle_payload = _load_if_exists(run_dir / "oracle_repair.json", load_json)
    if oracle_payload is None and bool(cfg["repair"].get("enabled", True)):
        oracle_payload = run_oracle_repair(cfg, run_dir, backend, trajectories)

    predictor_payload = _load_if_exists(run_dir / "repair_predictor.json", load_json)
    if predictor_payload is None and bool(cfg["predictor"].get("enabled", True)) and oracle_payload is not None:
        predictor_payload = train_repair_predictor(cfg, run_dir, trajectories, oracle_payload)

    evaluation_payload = _load_if_exists(run_dir / "repair_selection_eval.json", load_json)
    if evaluation_payload is None and bool(cfg["evaluation"].get("enabled", True)) and oracle_payload is not None:
        evaluation_payload = evaluate_repair_selection(
            cfg,
            run_dir,
            trajectories,
            oracle_payload,
            predictor_payload,
        )

    report = build_report(cfg, trajectories, oracle_payload, predictor_payload, evaluation_payload)
    save_json(run_dir / "report.json", report)
    return report


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-dir", default=None)
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    cfg = load_yaml(args.config)
    run_dir = Path(args.run_dir) if args.run_dir else init_run_dir(cfg)
    run_dir.mkdir(parents=True, exist_ok=True)
    report = run_pipeline(cfg, run_dir)
    print(f"[pipeline] done: {run_dir}")
    print(f"[pipeline] report: {run_dir / 'report.json'}")
    print(f"[pipeline] selection eval rows: {len(report.get('selection_eval', []))}")


if __name__ == "__main__":
    main()
