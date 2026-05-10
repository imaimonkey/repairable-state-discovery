from __future__ import annotations

import argparse
import copy
from pathlib import Path
from typing import Any

from repairable_diffusion.src.run_ar_baseline import run_ar_baseline
from repairable_diffusion.src.run_pipeline import run_pipeline
from repairable_diffusion.src.utils.io import ensure_dir, load_json, load_yaml, save_json, save_yaml


def _load_profiles(path: str | Path) -> dict[str, Any]:
    payload = load_yaml(path)
    return payload.get("models", {})


def _deep_update(base: dict[str, Any], updates: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(base)
    for key, value in updates.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _deep_update(out[key], value)
        else:
            out[key] = copy.deepcopy(value)
    return out


def _build_diffusion_cfg(
    template_cfg: dict[str, Any],
    protocol_cfg: dict[str, Any],
    profile_name: str,
    profiles: dict[str, Any],
    run_name: str,
    overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    cfg = copy.deepcopy(template_cfg)
    cfg["paths"]["run_name"] = run_name
    cfg["paths"]["outputs_root"] = protocol_cfg["paths"]["outputs_root"]
    cfg["dataset"] = copy.deepcopy(protocol_cfg["dataset"])
    cfg["backend"] = copy.deepcopy(profiles[profile_name]["backend"])
    cfg["study"] = {
        "family": "diffusion",
        "model_profile": profile_name,
        "role": "main",
    }
    if overrides:
        cfg = _deep_update(cfg, overrides)
    return cfg


def _build_ar_cfg(
    protocol_cfg: dict[str, Any],
    profile_name: str,
    profiles: dict[str, Any],
    run_name: str,
    samples_per_item: int | None,
    overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    backend = copy.deepcopy(profiles[profile_name]["backend"])
    if samples_per_item is not None:
        backend["samples_per_item"] = int(samples_per_item)
    cfg = {
        "paths": {
            "outputs_root": protocol_cfg["paths"]["outputs_root"],
            "run_name": run_name,
        },
        "dataset": copy.deepcopy(protocol_cfg["dataset"]),
        "backend": backend,
        "base_seed": int(protocol_cfg["dataset"].get("sample_seed", 11)),
        "study": {
            "family": "ar",
            "model_profile": profile_name,
            "role": "compare",
        },
    }
    if overrides:
        cfg = _deep_update(cfg, overrides)
    return cfg


def _parse_csv(spec: str | None) -> set[str]:
    if not spec:
        return set()
    return {part.strip() for part in spec.split(",") if part.strip()}


def _allowed(spec: dict[str, Any], family: str, allowed_families: set[str], allowed_run_names: set[str]) -> bool:
    if allowed_families and family not in allowed_families:
        return False
    if allowed_run_names and spec["run_name"] not in allowed_run_names:
        return False
    return True


def _report_name_for_mode(report_name: str, *, dry_run: bool) -> str:
    if not dry_run:
        return report_name
    path = Path(report_name)
    suffix = path.suffix or ".json"
    return str(path.with_name(f"{path.stem}_dry_run{suffix}"))


def _diffusion_output_from_report(
    *,
    run_name: str,
    model_profile: str,
    run_dir: Path,
    report: dict[str, Any],
) -> dict[str, Any]:
    return {
        "run_name": run_name,
        "family": "diffusion",
        "dataset_name": report.get("dataset", {}).get("dataset_name"),
        "model_profile": model_profile,
        "run_dir": str(run_dir),
        "report_path": str(run_dir / "report.json"),
        "selection_eval_rows": len(report.get("selection_eval", [])),
        "sample_accuracy": report.get("dataset", {}).get("sample_accuracy"),
        "item_pass_at_1": report.get("dataset", {}).get("item_pass_at_1"),
        "item_pass_at_k": report.get("dataset", {}).get("item_pass_at_k"),
        "predictor_selector": report.get("headline", {}).get("predictor_selector", {}),
        "oracle_selector": report.get("headline", {}).get("oracle_selector", {}),
        "repairability_summary": report.get("repairability_summary", {}),
        "selector_deltas": report.get("selector_deltas", {}),
    }


def _ar_output_from_payload(
    *,
    run_name: str,
    dataset_name: str,
    model_profile: str,
    run_dir: Path,
    payload: dict[str, Any],
) -> dict[str, Any]:
    meta = payload.get("meta", payload)
    return {
        "run_name": run_name,
        "family": "ar",
        "dataset_name": dataset_name,
        "model_profile": model_profile,
        "run_dir": str(run_dir),
        "summary_path": str(run_dir / "ar_baseline_summary.json"),
        "pass_at_1": meta["pass_at_1"],
        "pass_at_k": meta["pass_at_k"],
    }


def _summarize_protocol_runs(outputs: list[dict[str, Any]]) -> dict[str, Any]:
    diffusion_table = []
    ar_table = []
    for row in outputs:
        if row["family"] == "diffusion":
            predictor_row = row.get("predictor_selector", {})
            oracle_row = row.get("oracle_selector", {})
            diffusion_table.append(
                {
                    "run_name": row["run_name"],
                    "dataset_name": row.get("dataset_name"),
                    "model_profile": row["model_profile"],
                    "sample_accuracy": row.get("sample_accuracy"),
                    "item_pass_at_1": row.get("item_pass_at_1"),
                    "item_pass_at_k": row.get("item_pass_at_k"),
                    "predictor_expected_pass_at_k": predictor_row.get("expected_repaired_item_pass_at_k"),
                    "predictor_expected_newly_solved": predictor_row.get("expected_newly_solved_items"),
                    "predictor_negative_repair_rate": predictor_row.get("negative_repair_rate"),
                    "predictor_gain_over_base_pass_at_k": row.get("selector_deltas", {}).get("predictor_gain_over_base_pass_at_k"),
                    "oracle_expected_pass_at_k": oracle_row.get("expected_repaired_item_pass_at_k"),
                    "oracle_expected_newly_solved": oracle_row.get("expected_newly_solved_items"),
                    "peak_step_index": row.get("repairability_summary", {}).get("peak_step_index"),
                    "repairable_failed_rate": row.get("repairability_summary", {}).get("repairable_failed_rate"),
                }
            )
        elif row["family"] == "ar":
            ar_table.append(
                {
                    "run_name": row["run_name"],
                    "dataset_name": row.get("dataset_name"),
                    "model_profile": row["model_profile"],
                    "pass_at_1": row.get("pass_at_1"),
                    "pass_at_k": row.get("pass_at_k"),
                }
            )
    return {
        "diffusion_table": diffusion_table,
        "ar_table": ar_table,
    }


def _run_key(row: dict[str, Any]) -> tuple[str, str]:
    return str(row.get("family", "")), str(row.get("run_name", ""))


def _merge_partial_outputs(report_path: Path, outputs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not report_path.exists():
        return outputs
    existing = load_json(report_path).get("runs", [])
    output_keys = {_run_key(row) for row in outputs}
    merged = [row for row in existing if _run_key(row) not in output_keys]
    merged.extend(outputs)
    return merged


def run_protocol(
    protocol_cfg: dict[str, Any],
    *,
    allowed_families: set[str] | None = None,
    allowed_run_names: set[str] | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    allowed_families = allowed_families or set()
    allowed_run_names = allowed_run_names or set()
    profiles = _load_profiles(protocol_cfg["profiles_path"])
    generated_root = ensure_dir(protocol_cfg["paths"]["generated_configs_root"])
    outputs = []

    if bool(protocol_cfg["protocol"].get("run_diffusion_main", True)):
        for spec in protocol_cfg["protocol"].get("diffusion_runs", []):
            if not _allowed(spec, "diffusion", allowed_families, allowed_run_names):
                continue
            profile_name = spec["model_profile"]
            template_cfg = load_yaml(spec["config_template"])
            cfg = _build_diffusion_cfg(
                template_cfg,
                protocol_cfg,
                profile_name,
                profiles,
                spec["run_name"],
                spec.get("overrides"),
            )
            cfg_path = generated_root / f"{spec['run_name']}.yaml"
            save_json(cfg_path.with_suffix(".json"), cfg)
            save_yaml(cfg_path, cfg)
            run_dir = Path(cfg["paths"]["outputs_root"]) / cfg["paths"]["run_name"]
            if dry_run:
                outputs.append(
                    {
                        "run_name": spec["run_name"],
                        "family": "diffusion",
                        "dataset_name": cfg["dataset"]["name"],
                        "model_profile": profile_name,
                        "run_dir": str(run_dir),
                        "config_path": str(cfg_path),
                        "config_json_path": str(cfg_path.with_suffix(".json")),
                    }
                )
                continue
            report_path = run_dir / "report.json"
            report = load_json(report_path) if report_path.exists() else run_pipeline(cfg, run_dir)
            outputs.append(
                _diffusion_output_from_report(
                    run_name=spec["run_name"],
                    model_profile=profile_name,
                    run_dir=run_dir,
                    report=report,
                )
            )

    if bool(protocol_cfg["protocol"].get("run_ar_compare", True)):
        for spec in protocol_cfg["protocol"].get("ar_runs", []):
            if not _allowed(spec, "ar", allowed_families, allowed_run_names):
                continue
            profile_name = spec["model_profile"]
            cfg = _build_ar_cfg(
                protocol_cfg,
                profile_name,
                profiles,
                spec["run_name"],
                spec.get("samples_per_item"),
                spec.get("overrides"),
            )
            cfg_path = generated_root / f"{spec['run_name']}.yaml"
            save_json(cfg_path.with_suffix(".json"), cfg)
            save_yaml(cfg_path, cfg)
            run_dir = Path(cfg["paths"]["outputs_root"]) / cfg["paths"]["run_name"]
            if dry_run:
                outputs.append(
                    {
                        "run_name": spec["run_name"],
                        "family": "ar",
                        "dataset_name": cfg["dataset"]["name"],
                        "model_profile": profile_name,
                        "run_dir": str(run_dir),
                        "config_path": str(cfg_path),
                        "config_json_path": str(cfg_path.with_suffix(".json")),
                    }
                )
                continue
            summary_path = run_dir / "ar_baseline_summary.json"
            payload = {"meta": load_json(summary_path)} if summary_path.exists() else run_ar_baseline(cfg, run_dir)
            outputs.append(
                _ar_output_from_payload(
                    run_name=spec["run_name"],
                    dataset_name=cfg["dataset"]["name"],
                    model_profile=profile_name,
                    run_dir=run_dir,
                    payload=payload,
                )
            )

    report_name = protocol_cfg["paths"].get("protocol_report_name", "protocol_report.json")
    report_name = _report_name_for_mode(report_name, dry_run=dry_run)
    report_path = Path(protocol_cfg["paths"]["generated_configs_root"]) / report_name
    if not dry_run and (allowed_families or allowed_run_names):
        outputs = _merge_partial_outputs(report_path, outputs)

    report = {
        "dry_run": dry_run,
        "runs": outputs,
        "summary": _summarize_protocol_runs(outputs),
    }
    save_json(report_path, report)
    return report


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--protocol", required=True)
    ap.add_argument("--families", default="", help="Comma-separated subset of families: diffusion,ar")
    ap.add_argument("--run-names", default="", help="Comma-separated subset of protocol run_name values")
    ap.add_argument("--dry-run", action="store_true", help="Generate configs and a dry-run manifest without executing runs")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    protocol_cfg = load_yaml(args.protocol)
    report = run_protocol(
        protocol_cfg,
        allowed_families=_parse_csv(args.families),
        allowed_run_names=_parse_csv(args.run_names),
        dry_run=bool(args.dry_run),
    )
    mode = "dry-run" if args.dry_run else "done"
    print(f"[protocol] {mode}: {args.protocol}")
    print(f"[protocol] runs: {len(report['runs'])}")


if __name__ == "__main__":
    main()
