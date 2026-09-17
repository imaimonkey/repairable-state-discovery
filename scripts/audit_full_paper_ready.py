from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]

PROTOCOLS = {
    "math500_full": ("repairable_diffusion/configs/final/protocol_math500_full.yaml", "results/generated_configs/protocol_math500_full_report.json", 1, 2),
    "gsm8k_full": ("repairable_diffusion/configs/final/protocol_gsm8k_full.yaml", "results/generated_configs/protocol_gsm8k_full_report.json", 1, 2),
    "math500_full_robustness": ("repairable_diffusion/configs/final/protocol_math500_full_robustness.yaml", "results/generated_configs/protocol_math500_full_robustness_report.json", 3, 0),
    "math500_full_seed_repeats": ("repairable_diffusion/configs/final/protocol_math500_full_seed_repeats.yaml", "results/generated_configs/protocol_math500_full_seed_repeats_report.json", 2, 0),
    "gsm8k_full_seed_repeats": ("repairable_diffusion/configs/final/protocol_gsm8k_full_seed_repeats.yaml", "results/generated_configs/protocol_gsm8k_full_seed_repeats_report.json", 2, 0),
    "math500_full_dream_backbone": ("repairable_diffusion/configs/final/protocol_math500_full_dream_backbone.yaml", "results/generated_configs/protocol_math500_full_dream_backbone_report.json", 1, 0),
    "gsm8k_full_dream_backbone": ("repairable_diffusion/configs/final/protocol_gsm8k_full_dream_backbone.yaml", "results/generated_configs/protocol_gsm8k_full_dream_backbone_report.json", 1, 0),
}

AGGREGATE = ROOT / "results/benchmark_complete_reports/aggregate_report.json"
EXTENDED = ROOT / "results/benchmark_extended_analysis/extended_repair_analysis.json"
QUAL_JSON = ROOT / "results/benchmark_extended_analysis/qualitative_examples.json"
QUAL_MD = ROOT / "results/benchmark_extended_analysis/qualitative_examples.md"

EXPECTED_FIGURE_DATA = [
    ROOT / "results/benchmark_complete_reports/figure_data/repair_gain_curves.csv",
    ROOT / "results/benchmark_complete_reports/figure_data/best_step_histograms.csv",
    ROOT / "results/benchmark_complete_reports/figure_data/gain_negative_repair_tradeoff.csv",
]

EXPECTED_TABLES = [
    ROOT / "results/benchmark_complete_reports/tables/diffusion_latex.tex",
    ROOT / "results/benchmark_complete_reports/tables/ar_latex.tex",
]

EXPECTED_PAPER_TABLES = [
    ROOT / "paper/tables/main_diffusion.tex",
    ROOT / "paper/tables/ar_reference.tex",
    ROOT / "paper/tables/robustness_seed.tex",
    ROOT / "paper/tables/selector_comparison.tex",
    ROOT / "paper/tables/predictor_ablation.tex",
    ROOT / "paper/tables/cost_normalized.tex",
    ROOT / "paper/tables/backbone_dataset.tex",
]

EXPECTED_PAPER_SOURCE = [
    ROOT / "paper/main.tex",
    ROOT / "paper/references.bib",
]

EXPECTED_PAPER_FIGURES = [
    ROOT / "paper/figures/protocol_overview.pdf",
    ROOT / "paper/figures/repair_gain_curves.pdf",
    ROOT / "paper/figures/best_step_histogram.pdf",
    ROOT / "paper/figures/predictor_oracle.pdf",
    ROOT / "paper/figures/gain_negative_repair.pdf",
]

REQUIRED_STRATEGIES = {
    "confidence_low",
    "entropy_high",
    "masked_ratio_high",
    "early_step",
    "middle_step",
    "predictor",
    "predictor@0.50",
    "predictor@0.70",
    "predictor@0.90",
    "oracle",
    "abl_all",
    "abl_confidence_only",
    "abl_mask_only",
    "abl_step_only",
    "abl_no_confidence",
    "abl_no_mask",
    "abl_no_step",
}


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def preflight_errors() -> list[str]:
    errors: list[str] = []
    for label, (cfg_rel, _report_rel, _d, _a) in PROTOCOLS.items():
        cfg_path = ROOT / cfg_rel
        if not cfg_path.is_file():
            errors.append(f"{label}: missing config {cfg_rel}")
            continue
        with cfg_path.open("r", encoding="utf-8") as fh:
            cfg = yaml.safe_load(fh)
        dataset = cfg.get("dataset", {})
        if "limit" in dataset and dataset.get("limit") is not None:
            errors.append(f"{label}: full protocol must not set dataset.limit")
        diffusion_runs = cfg.get("protocol", {}).get("diffusion_runs", [])
        for run in diffusion_runs:
            evaluation = run.get("overrides", {}).get("evaluation", {})
            if evaluation.get("max_success_trajectories_for_negative_repair") != 0:
                errors.append(
                    f"{label}/{run.get('run_name')}: max_success_trajectories_for_negative_repair must be 0"
                )
    return errors


def protocol_status() -> tuple[list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    status: list[dict[str, Any]] = []
    for label, (_cfg_rel, report_rel, expected_d, expected_a) in PROTOCOLS.items():
        report_path = ROOT / report_rel
        row: dict[str, Any] = {
            "label": label,
            "report": report_rel,
            "expected_diffusion": expected_d,
            "expected_ar": expected_a,
            "complete": False,
        }
        if not report_path.is_file():
            errors.append(f"{label}: missing report {report_rel}")
            status.append(row)
            continue
        payload = read_json(report_path)
        runs = payload.get("runs", [])
        d = sum(1 for run in runs if run.get("family") == "diffusion")
        a = sum(1 for run in runs if run.get("family") == "ar")
        row.update(diffusion=d, ar=a, dry_run=payload.get("dry_run"))
        row["complete"] = payload.get("dry_run") is False and d == expected_d and a == expected_a
        if not row["complete"]:
            errors.append(
                f"{label}: report incomplete (dry_run={payload.get('dry_run')}, diffusion={d}/{expected_d}, ar={a}/{expected_a})"
            )
        status.append(row)
    return errors, status


def final_output_errors() -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    summary: dict[str, Any] = {}

    if not AGGREGATE.is_file():
        errors.append(f"missing aggregate: {AGGREGATE.relative_to(ROOT)}")
    else:
        aggregate = read_json(AGGREGATE)
        drows = aggregate.get("diffusion_rows", [])
        arows = aggregate.get("ar_rows", [])
        summary["diffusion_rows"] = len(drows)
        summary["ar_rows"] = len(arows)
        if len(drows) != 11:
            errors.append(f"aggregate diffusion rows: {len(drows)} != 11")
        if len(arows) != 4:
            errors.append(f"aggregate AR rows: {len(arows)} != 4")
        run_names = [row.get("run_name") for row in drows]
        if len(set(run_names)) != len(run_names):
            errors.append("aggregate has duplicate diffusion run_name values")

    if not EXTENDED.is_file():
        errors.append(f"missing extended analysis: {EXTENDED.relative_to(ROOT)}")
    else:
        extended = read_json(EXTENDED)
        rows = extended.get("rows", [])
        summary["extended_rows"] = len(rows)
        by_run: dict[str, set[str]] = {}
        for row in rows:
            by_run.setdefault(str(row.get("run_name")), set()).add(str(row.get("strategy")))
        summary["extended_runs"] = len(by_run)
        if len(by_run) != 11:
            errors.append(f"extended analysis covers {len(by_run)} runs != 11")
        for run_name, strategies in sorted(by_run.items()):
            missing = REQUIRED_STRATEGIES - strategies
            if missing:
                errors.append(f"{run_name}: missing extended strategies {sorted(missing)}")

    for path in EXPECTED_TABLES + EXPECTED_PAPER_SOURCE + EXPECTED_PAPER_TABLES + EXPECTED_PAPER_FIGURES + EXPECTED_FIGURE_DATA + [QUAL_JSON, QUAL_MD]:
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing/empty final artifact: {path.relative_to(ROOT)}")

    return errors, summary


def write_manifest(protocol_rows: list[dict[str, Any]], summary: dict[str, Any]) -> Path:
    out = ROOT / "results/full_paper_manifest.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "canonical_scope": "full-split benchmark-complete only",
        "historical_slice_results_are_not_final_tables": True,
        "claim_boundary": (
            "Failed diffusion reasoning trajectories contain measurable localized repairable states; "
            "repairability is evaluated jointly with negative repair, selector baselines, cost, seed robustness, "
            "dataset transfer, and a second diffusion backbone."
        ),
        "protocols": protocol_rows,
        "aggregate_report": str(AGGREGATE.relative_to(ROOT)),
        "extended_analysis": str(EXTENDED.relative_to(ROOT)),
        "tables": [str(path.relative_to(ROOT)) for path in EXPECTED_TABLES],
        "figure_data": [str(path.relative_to(ROOT)) for path in EXPECTED_FIGURE_DATA],
        "qualitative_examples": [str(QUAL_JSON.relative_to(ROOT)), str(QUAL_MD.relative_to(ROOT))],
        "summary": summary,
    }
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["preflight", "status", "final"], default="status")
    ap.add_argument("--write-manifest", action="store_true")
    args = ap.parse_args()

    errors = preflight_errors()
    report_errors: list[str] = []
    protocol_rows: list[dict[str, Any]] = []
    final_errors: list[str] = []
    summary: dict[str, Any] = {}

    if args.mode in {"status", "final"}:
        report_errors, protocol_rows = protocol_status()
        errors.extend(report_errors)
    if args.mode == "final":
        final_errors, summary = final_output_errors()
        errors.extend(final_errors)

    print(f"mode: {args.mode}")
    if protocol_rows:
        for row in protocol_rows:
            marker = "OK" if row.get("complete") else "WAIT"
            print(f"[{marker}] {row['label']}: {row['report']}")
    if summary:
        print(f"aggregate diffusion rows: {summary.get('diffusion_rows')}")
        print(f"aggregate AR rows: {summary.get('ar_rows')}")
        print(f"extended runs: {summary.get('extended_runs')}")
        print(f"extended rows: {summary.get('extended_rows')}")

    if errors:
        print("\nNOT READY")
        for error in errors:
            print(f"- {error}")
        if args.mode in {"preflight", "final"}:
            raise SystemExit(1)
        return

    if args.mode == "final" and args.write_manifest:
        manifest = write_manifest(protocol_rows, summary)
        print(f"manifest: {manifest.relative_to(ROOT)}")

    print("\nREADY")


if __name__ == "__main__":
    main()
