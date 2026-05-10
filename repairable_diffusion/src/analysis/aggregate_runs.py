from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

from repairable_diffusion.src.utils.io import ensure_dir, load_yaml, save_json


def _read_json(path: str | Path) -> dict[str, Any]:
    import json

    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _collect_protocol_reports(paths: list[str]) -> list[dict[str, Any]]:
    rows = []
    for path in paths:
        payload = _read_json(path)
        rows.append({"path": str(path), "payload": payload})
    return rows


def _diffusion_rows(protocol_reports: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for protocol in protocol_reports:
        for row in protocol["payload"].get("runs", []):
            if row.get("family") != "diffusion":
                continue
            predictor = row.get("predictor_selector", {})
            oracle = row.get("oracle_selector", {})
            repairability = row.get("repairability_summary", {})
            selector_deltas = row.get("selector_deltas", {})
            rows.append(
                {
                    "protocol_report": protocol["path"],
                    "dataset_name": row.get("dataset_name"),
                    "run_name": row.get("run_name"),
                    "model_profile": row.get("model_profile"),
                    "sample_accuracy": row.get("sample_accuracy"),
                    "item_pass_at_1": row.get("item_pass_at_1"),
                    "item_pass_at_k": row.get("item_pass_at_k"),
                    "predictor_expected_pass_at_k": predictor.get("expected_repaired_item_pass_at_k"),
                    "predictor_expected_newly_solved_items": predictor.get("expected_newly_solved_items"),
                    "predictor_negative_repair_rate": predictor.get("negative_repair_rate"),
                    "oracle_expected_pass_at_k": oracle.get("expected_repaired_item_pass_at_k"),
                    "oracle_expected_newly_solved_items": oracle.get("expected_newly_solved_items"),
                    "peak_step_index": repairability.get("peak_step_index"),
                    "peak_mean_correction_rate": repairability.get("peak_mean_correction_rate"),
                    "repairable_failed_rate": repairability.get("repairable_failed_rate"),
                    "predictor_gain_over_base_pass_at_k": selector_deltas.get("predictor_gain_over_base_pass_at_k"),
                    "oracle_minus_predictor_expected_pass_at_k": selector_deltas.get("oracle_minus_predictor_expected_pass_at_k"),
                    "predictor_minus_random_expected_pass_at_k": selector_deltas.get("predictor_minus_random_expected_pass_at_k"),
                    "predictor_minus_confidence_expected_pass_at_k": selector_deltas.get("predictor_minus_confidence_expected_pass_at_k"),
                    "run_dir": row.get("run_dir"),
                    "report_path": row.get("report_path"),
                }
            )
    return rows


def _ar_rows(protocol_reports: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for protocol in protocol_reports:
        for row in protocol["payload"].get("runs", []):
            if row.get("family") != "ar":
                continue
            rows.append(
                {
                    "protocol_report": protocol["path"],
                    "dataset_name": row.get("dataset_name"),
                    "run_name": row.get("run_name"),
                    "model_profile": row.get("model_profile"),
                    "pass_at_1": row.get("pass_at_1"),
                    "pass_at_k": row.get("pass_at_k"),
                    "run_dir": row.get("run_dir"),
                    "summary_path": row.get("summary_path"),
                }
            )
    return rows


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    ensure_dir(path.parent)
    if not rows:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write("")
        return
    fieldnames = list(rows[0].keys())
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def aggregate(protocol_report_paths: list[str], output_dir: str | Path) -> dict[str, Any]:
    protocol_reports = _collect_protocol_reports(protocol_report_paths)
    diffusion_rows = _diffusion_rows(protocol_reports)
    ar_rows = _ar_rows(protocol_reports)
    payload = {
        "protocol_reports": [row["path"] for row in protocol_reports],
        "diffusion_rows": diffusion_rows,
        "ar_rows": ar_rows,
    }

    out_dir = ensure_dir(output_dir)
    save_json(out_dir / "aggregate_report.json", payload)
    _write_csv(out_dir / "diffusion_summary.csv", diffusion_rows)
    _write_csv(out_dir / "ar_summary.csv", ar_rows)
    return payload


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--protocol-report", action="append", required=True, dest="protocol_reports")
    ap.add_argument("--output-dir", required=True)
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    payload = aggregate(args.protocol_reports, args.output_dir)
    print(f"[aggregate] protocol reports: {len(payload['protocol_reports'])}")
    print(f"[aggregate] diffusion rows: {len(payload['diffusion_rows'])}")
    print(f"[aggregate] ar rows: {len(payload['ar_rows'])}")


if __name__ == "__main__":
    main()
