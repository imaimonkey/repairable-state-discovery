from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]


def _read(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _fmt(value: Any) -> str:
    if value is None:
        return "--"
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _escape(value: Any) -> str:
    return _fmt(value).replace("_", r"\_").replace("%", r"\%")


def _table(path: Path, caption: str, label: str, headers: list[str], rows: Iterable[list[Any]]) -> None:
    rows = list(rows)
    lines = [
        r"\begin{table*}[t]",
        r"\centering",
        r"\small",
        f"\\caption{{{caption}}}",
        f"\\label{{{label}}}",
        r"\begin{tabular}{" + "l" * len(headers) + "}",
        r"\toprule",
        " & ".join(headers) + " \\\\",
        r"\midrule",
    ]
    for row in rows:
        lines.append(" & ".join(_escape(value) for value in row) + " \\\\")
    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table*}", ""])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _is_main(row: dict[str, Any]) -> bool:
    return row.get("run_name") in {"math500_full_llada8b_fast", "gsm8k_full_llada8b_fast"}


def _write_facts(path: Path, aggregate: dict[str, Any]) -> None:
    rows = {row["run_name"]: row for row in aggregate.get("diffusion_rows", [])}
    names = {
        "math": "math500_full_llada8b_fast",
        "gsm": "gsm8k_full_llada8b_fast",
    }
    lines = ["% Generated from results/benchmark_complete_reports/aggregate_report.json."]
    for prefix, run_name in names.items():
        row = rows.get(run_name, {})
        macros = {
            f"{prefix}BasePassK": row.get("item_pass_at_k"),
            f"{prefix}PredPassK": row.get("predictor_expected_pass_at_k"),
            f"{prefix}PredGain": row.get("predictor_gain_over_base_pass_at_k"),
            f"{prefix}OraclePassK": row.get("oracle_expected_pass_at_k"),
            f"{prefix}OracleGap": row.get("oracle_minus_predictor_expected_pass_at_k"),
            f"{prefix}RepairableFailed": row.get("repairable_failed_rate"),
            f"{prefix}NegativeRepair": row.get("predictor_negative_repair_rate"),
            f"{prefix}PeakStep": row.get("peak_step_index"),
        }
        for macro, value in macros.items():
            lines.append(f"\\newcommand{{\\{macro}}}{{{_escape(value)}}}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def render(aggregate_path: Path, extended_path: Path, output_dir: Path) -> None:
    aggregate = _read(aggregate_path)
    extended = _read(extended_path).get("rows", [])
    paper_tables = output_dir / "tables"
    _write_facts(output_dir / "generated" / "facts.tex", aggregate)

    diffusion = [row for row in aggregate.get("diffusion_rows", []) if _is_main(row)]
    _table(
        paper_tables / "main_diffusion.tex",
        "Main full-split diffusion repairability results. All values are generated from the canonical aggregate.",
        "tab:main-diffusion",
        ["Dataset", "Model", "Pass@1", "Base Pass@k", "Pred. Pass@k", "Gain", "Oracle--Pred.", "Peak", "Repairable", "Neg. repair"],
        [
            [r.get("dataset_name"), r.get("model_profile"), r.get("item_pass_at_1"), r.get("item_pass_at_k"),
             r.get("predictor_expected_pass_at_k"), r.get("predictor_gain_over_base_pass_at_k"),
             r.get("oracle_minus_predictor_expected_pass_at_k"), r.get("peak_step_index"),
             r.get("repairable_failed_rate"), r.get("predictor_negative_repair_rate")]
            for r in diffusion
        ],
    )
    _table(
        paper_tables / "ar_reference.tex",
        "Autoregressive reference performance on the full splits.",
        "tab:ar-reference",
        ["Dataset", "Model", "Pass@1", "Pass@k"],
        [[r.get("dataset_name"), r.get("model_profile"), r.get("pass_at_1"), r.get("pass_at_k")] for r in aggregate.get("ar_rows", [])],
    )

    robustness_names = {
        "math500_full_seed29_llada8b_fast", "math500_full_stride16_llada8b_fast", "math500_full_branch2_llada8b_fast",
        "math500_full_seed41_llada8b_fast", "math500_full_seed53_llada8b_fast",
        "gsm8k_full_seed29_llada8b_fast", "gsm8k_full_seed41_llada8b_fast",
    }
    _table(
        paper_tables / "robustness_seed.tex",
        "Configuration robustness and repeated-seed uncertainty, kept as separate run families.",
        "tab:robustness-seeds",
        ["Run", "Dataset", "Base Pass@k", "Pred. Pass@k", "Oracle Pass@k", "Neg. repair", "Peak"],
        [
            [r.get("run_name"), r.get("dataset_name"), r.get("item_pass_at_k"), r.get("predictor_expected_pass_at_k"),
             r.get("oracle_expected_pass_at_k"), r.get("predictor_negative_repair_rate"), r.get("peak_step_index")]
            for r in aggregate.get("diffusion_rows", []) if r.get("run_name") in robustness_names
        ],
    )

    selector_names = {"confidence_low", "entropy_high", "masked_ratio_high", "early_step", "middle_step", "predictor", "oracle", "predictor@0.50", "predictor@0.70", "predictor@0.90"}
    selector_rows = [r for r in extended if r.get("run_name") in {"math500_full_llada8b_fast", "gsm8k_full_llada8b_fast"} and r.get("strategy") in selector_names]
    _table(
        paper_tables / "selector_comparison.tex",
        "Selector comparison on the canonical main runs.",
        "tab:selectors",
        ["Run", "Selector", "Repaired Pass@k", "Gain", "95\% CI", "Neg. repair"],
        [[r.get("run_name"), r.get("strategy"), r.get("repaired_pass_at_k"), r.get("gain"), f"[{_fmt(r.get('gain_ci_low'))}, {_fmt(r.get('gain_ci_high'))}]", r.get("negative_repair_rate")] for r in selector_rows],
    )

    ablation_rows = [r for r in extended if r.get("run_name") in {"math500_full_llada8b_fast", "gsm8k_full_llada8b_fast"} and str(r.get("strategy", "")).startswith("abl_")]
    _table(
        paper_tables / "predictor_ablation.tex",
        "Predictor feature ablations. Repair metrics are reported alongside diagnostic held-out scores when available.",
        "tab:ablations",
        ["Run", "Features", "Repaired Pass@k", "Gain", "Neg. repair", "Test acc.", "Test ROC-AUC"],
        [[r.get("run_name"), r.get("strategy"), r.get("repaired_pass_at_k"), r.get("gain"), r.get("negative_repair_rate"), r.get("ablation_test_accuracy"), r.get("ablation_test_roc_auc")] for r in ablation_rows],
    )

    cost_rows = [r for r in extended if r.get("run_name") in {"math500_full_llada8b_fast", "gsm8k_full_llada8b_fast"} and r.get("strategy") in {"predictor", "oracle"}]
    _table(
        paper_tables / "cost_normalized.tex",
        "Cost-normalized repair analysis. Extra-sampling values are explicitly an observed-sample proxy, not decoded controls.",
        "tab:cost",
        ["Run", "Policy", "Branch evals", "Cost/item", "Gain/1k evals", "Extra-sampling proxy", "Gain over proxy"],
        [[r.get("run_name"), r.get("strategy"), r.get("estimated_repair_branch_evals"), r.get("repair_cost_per_item"), r.get("repair_gain_per_1k_branch_evals"), r.get("extra_sampling_pass_at_k_approx"), r.get("gain_over_extra_sampling_approx")] for r in cost_rows],
    )

    backbone_rows = [r for r in aggregate.get("diffusion_rows", []) if "full_dream" in str(r.get("run_name", "")) or _is_main(r)]
    _table(
        paper_tables / "backbone_dataset.tex",
        "Dataset and diffusion-backbone comparison.",
        "tab:backbone-dataset",
        ["Run", "Dataset", "Backbone", "Base Pass@k", "Pred. Pass@k", "Gain", "Peak", "Neg. repair"],
        [[r.get("run_name"), r.get("dataset_name"), r.get("model_profile"), r.get("item_pass_at_k"), r.get("predictor_expected_pass_at_k"), r.get("predictor_gain_over_base_pass_at_k"), r.get("peak_step_index"), r.get("predictor_negative_repair_rate")] for r in backbone_rows],
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aggregate-report", default=str(ROOT / "results/benchmark_complete_reports/aggregate_report.json"))
    ap.add_argument("--extended-analysis", default=str(ROOT / "results/benchmark_extended_analysis/extended_repair_analysis.json"))
    ap.add_argument("--output-dir", default=str(ROOT / "paper"))
    args = ap.parse_args()
    render(Path(args.aggregate_report), Path(args.extended_analysis), Path(args.output_dir))
    print(f"[paper-artifacts] output: {args.output_dir}")


if __name__ == "__main__":
    main()
