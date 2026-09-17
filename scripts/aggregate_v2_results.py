from __future__ import annotations

import csv
import json
import pickle
import statistics
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from repairable_diffusion.src.utils.io import load_yaml
from repairable_diffusion.src.v2.metrics import paired_branch_item_pass_at_k
from repairable_diffusion.src.v2.provenance import config_sha256


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "repairable_diffusion/outputs/v2_measurement"
RESULT_ROOT = ROOT / "results/v2_measurement"
PAPER_ROOT = ROOT / "paper/v2_generated/tables"
CONTRACT = load_yaml(ROOT / "repairable_diffusion/configs/v2/measurement_contract.yaml")
THRESHOLD = float(CONTRACT["measurement"]["confirmation_threshold"])
B_EVAL = int(CONTRACT["branches"]["confirmation_count"])

FULL_CONFIGS = [
    "repairable_diffusion/configs/v2/runs/full_math500_llada.yaml",
    "repairable_diffusion/configs/v2/runs/full_gsm8k_llada.yaml",
    "repairable_diffusion/configs/v2/runs/full_math500_dream.yaml",
    "repairable_diffusion/configs/v2/runs/full_gsm8k_dream.yaml",
    "repairable_diffusion/configs/v2/runs/full_bbh_logical3_llada.yaml",
    "repairable_diffusion/configs/v2/runs/full_bbh_logical5_llada.yaml",
    "repairable_diffusion/configs/v2/runs/full_bbh_logical7_llada.yaml",
    "repairable_diffusion/configs/v2/runs/full_mbpp_llada.yaml",
]
TIER_A_RUNS = {"v2_math500_llada", "v2_gsm8k_llada"}


def _git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file() or path.stat().st_size == 0:
        return []
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    keys = []
    seen = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                keys.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def _f(value: Any) -> float | None:
    if value in (None, "", "None", "nan"):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def _median(values: list[float]) -> float | None:
    return float(statistics.median(values)) if values else None


def _load_run(config_rel: str) -> dict[str, Any] | None:
    cfg = load_yaml(ROOT / config_rel)
    run_name = str(cfg["run_name"])
    run_dir = OUTPUT_ROOT / run_name
    report_path = run_dir / "report.json"
    if not report_path.is_file():
        return None
    return {
        "config_rel": config_rel,
        "cfg": cfg,
        "run_name": run_name,
        "run_dir": run_dir,
        "report": _read_json(report_path),
    }


def _table1(run: dict[str, Any]) -> dict[str, Any]:
    report = run["report"]
    cfg = run["cfg"]
    rows = _read_csv(run["run_dir"] / "existence.csv")
    transient = [float(str(r.get("transient_correct", "False")).lower() == "true") for r in rows]
    confirmed = [float(str(r.get("confirmed_repairable", "False")).lower() == "true") for r in rows]
    never = [float(str(r.get("repairable_but_never_correct", "False")).lower() == "true") for r in rows]
    native = []
    last_steps = []
    for r in rows:
        qn = _f(r.get("q_native_confirm"))
        if qn is not None:
            native.append(float(qn >= THRESHOLD))
        t = _f(r.get("t_last"))
        if t is not None and str(r.get("temporal_confirmation_complete", "False")).lower() == "true":
            last_steps.append(t)
    return {
        "run_name": run["run_name"],
        "dataset": cfg["dataset"]["name"],
        "dataset_config": cfg["dataset"].get("config_name", ""),
        "model_profile": cfg["model_profile"],
        "items": report.get("items"),
        "base_pass_at_k": report.get("base_pass_at_k"),
        "failed_items_probed": len(rows),
        "earlier_correct_rate": _mean(transient),
        "native_recoverable_rate": _mean(native),
        "confirmed_repairable_rate": _mean(confirmed),
        "repairable_but_never_correct_rate": _mean(never),
        "median_last_repairable_step": _median(last_steps),
        "prospective_policy_pass_at_k": report.get("prospective_policy_pass_at_k"),
        "prospective_net_gain": report.get("prospective_net_gain"),
    }


def _mechanism_rows(run: dict[str, Any]) -> list[dict[str, Any]]:
    if run["run_name"] not in TIER_A_RUNS:
        return []
    report = run["report"]
    subset = {int(x) for x in report.get("mechanism_subset_items", [])}
    branches = _read_jsonl(run["run_dir"] / "probe_branches.jsonl")
    output = []
    operators = [
        "native_continuation",
        "matched_stochastic_continuation",
        "random_position_remask",
        "low_confidence_remask_v2",
        "core",
    ]
    matched_failed = None
    temp: dict[str, dict[str, Any]] = {}
    for op in operators:
        stage = "fidelity" if op == "native_continuation" else "localization"
        rows = [
            r for r in branches
            if r.get("operator_id") == op
            and r.get("stage") == stage
            and int(r.get("item_id", -1)) in subset
            and r.get("correct") is not None
        ]
        failed = [r for r in rows if not bool(r.get("base_correct"))]
        success = [r for r in rows if bool(r.get("base_correct"))]
        failure_rate = _mean([float(bool(r["correct"])) for r in failed])
        harm = _mean([1.0 - float(bool(r["correct"])) for r in success])
        fidelity = _mean([float(bool(r["correct"]) == bool(r["base_correct"])) for r in rows]) if op == "native_continuation" else None
        temp[op] = {
            "run_name": run["run_name"],
            "operator": "CoRe-snapshot" if op == "core" else op,
            "role": "fidelity_control" if op == "native_continuation" else "repair_or_continuation",
            "failed_recovery_rate": failure_rate,
            "negative_harm_rate": harm,
            "fidelity_match_rate": fidelity,
            "avg_modified_tokens": _mean([float(r.get("modified_count", 0)) for r in rows]),
            "avg_nfe": _mean([float(r.get("nfe", 0)) for r in rows]),
            "rows": len(rows),
        }
        if op == "matched_stochastic_continuation":
            matched_failed = failure_rate
    for op in operators:
        row = temp[op]
        row["lift_vs_matched_continuation"] = (
            row["failed_recovery_rate"] - matched_failed
            if matched_failed is not None and row["failed_recovery_rate"] is not None and op != "native_continuation"
            else None
        )
        output.append(row)
    output.append(
        {
            "run_name": run["run_name"],
            "operator": "fresh_sampling_compute_control",
            "role": "compute_control",
            "failed_recovery_rate": None,
            "negative_harm_rate": 0.0,
            "fidelity_match_rate": None,
            "avg_modified_tokens": None,
            "avg_nfe": report.get("fresh_sampling_achieved_nfe"),
            "lift_vs_matched_continuation": None,
            "policy_gain": report.get("fresh_sampling_gain"),
            "rows": len(_read_jsonl(run["run_dir"] / "fresh_sampling.jsonl")),
        }
    )
    return output


def _policy_rows(run: dict[str, Any]) -> list[dict[str, Any]]:
    selector_rows = _read_csv(run["run_dir"] / "selector_confirmation.csv")
    if not selector_rows:
        return []
    with (run["run_dir"] / "trajectories.pkl").open("rb") as fh:
        records = pickle.load(fh)["records"]
    branches = _read_jsonl(run["run_dir"] / "probe_branches.jsonl")
    cfg = run["cfg"]
    policy_ids = {int(x) for x in cfg.get("probe", {}).get("policy_trajectory_ids", [0])}
    base_by_item: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        base_by_item[int(record["item_id"])].append(record)
    base_passk = sum(float(any(bool(r["correct"]) for r in rs)) for rs in base_by_item.values()) / max(1, len(base_by_item))

    branch_bucket: dict[tuple[int, int, int], dict[int, dict[str, Any]]] = defaultdict(dict)
    for r in branches:
        if r.get("stage") == "confirmation" and r.get("operator_id") == "low_confidence_remask_v2" and r.get("correct") is not None:
            branch_bucket[(int(r["item_id"]), int(r["trajectory_id"]), int(r["step_index"]))][int(r["branch_index"])] = r

    choice_map: dict[tuple[int, int, str], int] = {}
    selectors = set()
    for r in selector_rows:
        selector = str(r["selector"])
        selectors.add(selector)
        choice_map[(int(r["item_id"]), int(r["trajectory_id"]), selector)] = int(r["step_index"])

    output = []
    for selector in sorted(selectors):
        items: dict[int, list[list[bool]]] = {}
        harm_values = []
        recovery_values = []
        delta_values = []
        nfe_values = []
        covered = 0
        eligible = 0
        for item_id, records_i in base_by_item.items():
            records_i = sorted(records_i, key=lambda r: int(r["trajectory_id"]))
            trajectories = []
            for record in records_i:
                tid = int(record["trajectory_id"])
                if tid not in policy_ids:
                    trajectories.append([bool(record["correct"])] * B_EVAL)
                    continue
                eligible += 1
                step = choice_map.get((item_id, tid, selector))
                bucket = branch_bucket.get((item_id, tid, step)) if step is not None else None
                if bucket and all(b in bucket for b in range(B_EVAL)):
                    outcomes = [bool(bucket[b]["correct"]) for b in range(B_EVAL)]
                    trajectories.append(outcomes)
                    covered += 1
                    nfe_values.extend(float(bucket[b].get("nfe", 0)) for b in range(B_EVAL))
                    if bool(record["correct"]):
                        harm_values.extend(1.0 - float(x) for x in outcomes)
                    else:
                        recovery_values.extend(float(x) for x in outcomes)
                else:
                    trajectories.append([bool(record["correct"])] * B_EVAL)
            items[item_id] = trajectories
        prospective = paired_branch_item_pass_at_k(items)
        diag = [r for r in selector_rows if r["selector"] == selector and str(r.get("base_correct", "False")).lower() == "false"]
        for r in diag:
            d = _f(r.get("delta_confirm"))
            if d is not None:
                delta_values.append(d)
        output.append(
            {
                "run_name": run["run_name"],
                "selector": selector,
                "diagnostic_confirmed_recovery": _mean(recovery_values),
                "diagnostic_delta_vs_native": _mean(delta_values),
                "prospective_pass_at_k": prospective,
                "prospective_net_gain": prospective - base_passk,
                "negative_harm_rate": _mean(harm_values),
                "coverage": covered / eligible if eligible else 0.0,
                "avg_extra_nfe": _mean(nfe_values),
            }
        )
    return output


def _landscape_rows(run: dict[str, Any]) -> list[dict[str, Any]]:
    rows = _read_jsonl(run["run_dir"] / "state_values.jsonl")
    buckets: dict[float, list[dict[str, Any]]] = defaultdict(list)
    for r in rows:
        if not bool(next((x["correct"] for x in []), False)):
            pass
        buckets[float(r["normalized_step"])].append(r)
    out = []
    for step, values in sorted(buckets.items()):
        qc = [_f(r.get("q_native_loc")) for r in values]
        qr = [_f(r.get("q_repair_loc")) for r in values]
        out.append(
            {
                "run_name": run["run_name"],
                "normalized_step": step,
                "q_native_mean": _mean([x for x in qc if x is not None]),
                "q_repair_mean": _mean([x for x in qr if x is not None]),
                "observed_correct_rate": _mean([float(bool(r.get("observed_correct"))) for r in values]),
                "count": len(values),
            }
        )
    return out


def _survival_rows(run: dict[str, Any]) -> list[dict[str, Any]]:
    existence = _read_csv(run["run_dir"] / "existence.csv")
    temporal = [r for r in existence if str(r.get("temporal_confirmation_complete", "False")).lower() == "true"]
    if not temporal:
        return []
    checkpoints = list(range(8, 65, 8))
    out = []
    for step in checkpoints:
        alive = 0
        for r in temporal:
            t = _f(r.get("t_last"))
            if t is not None and t >= step:
                alive += 1
        out.append(
            {
                "run_name": run["run_name"],
                "step_index": step,
                "normalized_step": step / 64.0,
                "survival": alive / len(temporal),
                "count": alive,
                "denominator": len(temporal),
            }
        )
    return out


def _latex_table(path: Path, rows: list[dict[str, Any]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["% Auto-generated by scripts/aggregate_v2_results.py", "\\begin{tabular}{" + "l" * len(columns) + "}", "\\toprule", " & ".join(columns) + " \\\\", "\\midrule"]
    for row in rows:
        cells = []
        for col in columns:
            value = row.get(col, "")
            if isinstance(value, float):
                value = f"{value:.4f}"
            cells.append(str(value).replace("_", "\\_"))
        lines.append(" & ".join(cells) + " \\\\")
    lines += ["\\bottomrule", "\\end{tabular}"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    completed = []
    missing = []
    runs = []
    config_hashes = {}
    for config_rel in FULL_CONFIGS:
        cfg = load_yaml(ROOT / config_rel)
        config_hashes[config_rel] = config_sha256(cfg)
        run = _load_run(config_rel)
        if run is None:
            missing.append(str(cfg["run_name"]))
        else:
            completed.append(str(cfg["run_name"]))
            runs.append(run)

    table1 = [_table1(run) for run in runs]
    table2 = [row for run in runs for row in _mechanism_rows(run)]
    table3 = [row for run in runs for row in _policy_rows(run)]
    landscape = [row for run in runs if run["run_name"] in TIER_A_RUNS for row in _landscape_rows(run)]
    survival = [row for run in runs if run["run_name"] in TIER_A_RUNS for row in _survival_rows(run)]

    _write_csv(RESULT_ROOT / "table1_existence.csv", table1)
    _write_csv(RESULT_ROOT / "table2_mechanisms.csv", table2)
    _write_csv(RESULT_ROOT / "table3_localization.csv", table3)
    _write_csv(RESULT_ROOT / "figure_data/recoverability_landscape.csv", landscape)
    _write_csv(RESULT_ROOT / "figure_data/repairability_survival.csv", survival)
    _write_csv(RESULT_ROOT / "figure_data/recovery_harm_compute.csv", table2)

    _latex_table(PAPER_ROOT / "table1_existence.tex", table1, ["run_name", "base_pass_at_k", "native_recoverable_rate", "confirmed_repairable_rate", "repairable_but_never_correct_rate"])
    _latex_table(PAPER_ROOT / "table2_mechanisms.tex", table2, ["run_name", "operator", "failed_recovery_rate", "lift_vs_matched_continuation", "negative_harm_rate", "avg_nfe"])
    _latex_table(PAPER_ROOT / "table3_localization.tex", table3, ["run_name", "selector", "diagnostic_confirmed_recovery", "prospective_net_gain", "negative_harm_rate", "coverage"])

    aggregate = {
        "status": "complete_for_available_frozen_runs",
        "git_sha": _git_sha(),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "completed_runs": completed,
        "missing_runs": missing,
        "tier_a_complete": TIER_A_RUNS.issubset(set(completed)),
        "table1_rows": len(table1),
        "table2_rows": len(table2),
        "table3_rows": len(table3),
        "v1_artifacts_substituted": False,
    }
    (RESULT_ROOT / "aggregate_report.json").write_text(json.dumps(aggregate, indent=2) + "\n", encoding="utf-8")

    readiness = {}
    for name in ("unit_preflight", "backend_validation"):
        path = RESULT_ROOT / "readiness" / f"{name}.json"
        readiness[name] = _read_json(path) if path.is_file() else None
    jobs = _read_json(RESULT_ROOT / "job_manifest.json") if (RESULT_ROOT / "job_manifest.json").is_file() else None
    final_manifest = {
        "status": "FINALIZED" if aggregate["tier_a_complete"] else "PARTIAL_FROZEN_MATRIX",
        "git_sha": _git_sha(),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "config_hashes": config_hashes,
        "completed_runs": completed,
        "missing_runs": missing,
        "readiness": readiness,
        "jobs": jobs,
        "infrastructure_only_deviations": [],
        "v1_results_substituted": False,
        "claim_guard": "Do not infer claims beyond completed V2 rows; negative/null results are retained.",
    }
    (RESULT_ROOT / "final_execution_manifest.json").write_text(json.dumps(final_manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(aggregate, indent=2))


if __name__ == "__main__":
    main()
