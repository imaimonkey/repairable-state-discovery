from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

from repairable_diffusion.src.utils.io import ensure_dir


def _read_json(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    ensure_dir(path.parent)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row})
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def export_figure_data(aggregate_report: str | Path, output_dir: str | Path) -> dict[str, int]:
    aggregate = _read_json(aggregate_report)
    out_dir = ensure_dir(output_dir)

    gain_curve_rows: list[dict[str, Any]] = []
    best_step_rows: list[dict[str, Any]] = []
    tradeoff_rows: list[dict[str, Any]] = []

    for row in aggregate.get("diffusion_rows", []):
        report_path = row.get("report_path")
        if not report_path:
            continue
        report = _read_json(report_path)
        base = {
            "run_name": row.get("run_name"),
            "dataset_name": row.get("dataset_name"),
            "model_profile": row.get("model_profile"),
        }

        for curve_row in report.get("repair_gain_curve", []):
            gain_curve_rows.append(
                {
                    **base,
                    "step_index": curve_row.get("step_index"),
                    "mean_correction_rate": curve_row.get("mean_correction_rate"),
                    "count": curve_row.get("count"),
                }
            )

        for hist_row in report.get("repairability_summary", {}).get("best_step_histogram", []):
            best_step_rows.append(
                {
                    **base,
                    "step_index": hist_row.get("step_index"),
                    "count": hist_row.get("count"),
                }
            )

        tradeoff_rows.append(
            {
                **base,
                "base_pass_at_k": row.get("item_pass_at_k"),
                "predictor_repaired_pass_at_k": row.get("predictor_expected_pass_at_k"),
                "predictor_gain_over_base_pass_at_k": row.get("predictor_gain_over_base_pass_at_k"),
                "predictor_negative_repair_rate": row.get("predictor_negative_repair_rate"),
                "oracle_minus_predictor_expected_pass_at_k": row.get("oracle_minus_predictor_expected_pass_at_k"),
                "repairable_failed_rate": row.get("repairable_failed_rate"),
                "peak_step_index": row.get("peak_step_index"),
            }
        )

    _write_csv(out_dir / "repair_gain_curves.csv", gain_curve_rows)
    _write_csv(out_dir / "best_step_histograms.csv", best_step_rows)
    _write_csv(out_dir / "gain_negative_repair_tradeoff.csv", tradeoff_rows)
    return {
        "repair_gain_curve_rows": len(gain_curve_rows),
        "best_step_histogram_rows": len(best_step_rows),
        "tradeoff_rows": len(tradeoff_rows),
    }


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aggregate-report", required=True)
    ap.add_argument("--output-dir", required=True)
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    counts = export_figure_data(args.aggregate_report, args.output_dir)
    print(f"[figure-data] repair gain rows: {counts['repair_gain_curve_rows']}")
    print(f"[figure-data] best-step rows: {counts['best_step_histogram_rows']}")
    print(f"[figure-data] tradeoff rows: {counts['tradeoff_rows']}")


if __name__ == "__main__":
    main()
