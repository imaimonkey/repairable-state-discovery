from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import pickle
import subprocess
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

from repairable_diffusion.src.utils.io import ensure_dir, load_yaml, save_json
from repairable_diffusion.src.v2.backends import create_v2_backend
from repairable_diffusion.src.v2.contracts import deterministic_branch_seed, validate_contract_dict
from repairable_diffusion.src.v2.metrics import last_repairable_step, paired_branch_item_pass_at_k
from repairable_diffusion.src.v2.oof import crossfit_value_scores
from repairable_diffusion.src.v2.provenance import config_sha256, scientific_fingerprint, sha256_file
from repairable_diffusion.src.v2.task_adapters import create_task_adapter


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "repairable_diffusion/configs/v2/measurement_contract.yaml"
PROFILES_PATH = ROOT / "repairable_diffusion/configs/model_profiles.yaml"


def _git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def _final_report_provenance(base_fingerprint: dict[str, Any]) -> dict[str, str]:
    """Keep scientific execution provenance stable if the worktree moves later."""
    execution_sha = str(base_fingerprint["git_sha"])
    return {
        "git_sha": execution_sha,
        "execution_git_sha": execution_sha,
        "finalization_git_sha": _git_sha(),
    }


def _load_profile(name: str, path: Path = PROFILES_PATH) -> dict[str, Any]:
    payload = load_yaml(path)
    profile = dict(payload["models"][name])
    return dict(profile["backend"])


def _jsonl_write(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    ensure_dir(path.parent)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def _jsonl_read(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    ensure_dir(path.parent)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    keys: list[str] = []
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


def _stable_subset(ids: Iterable[int], *, count: int, seed: int) -> set[int]:
    values = sorted(set(int(x) for x in ids))
    ranked = sorted(
        values,
        key=lambda x: hashlib.sha256(f"{seed}|{x}".encode("utf-8")).hexdigest(),
    )
    return set(ranked[: min(int(count), len(ranked))])


def _nearest_step(steps: list[dict[str, Any]], target: float) -> dict[str, Any]:
    return min(steps, key=lambda row: (abs(float(row["normalized_step"]) - target), int(row["step_index"])))


def _selectors_for_trajectory(
    steps: list[dict[str, Any]],
    state_rows: list[dict[str, Any]],
    *,
    root_seed: int,
    item_id: int,
    trajectory_id: int,
) -> dict[str, int]:
    if not steps:
        return {}
    by_step = {int(row["step_index"]): row for row in state_rows}
    eligible = [row for row in steps if int(row["step_index"]) in by_step]
    if not eligible:
        return {}
    digest = hashlib.sha256(f"selector|{root_seed}|{item_id}|{trajectory_id}".encode()).digest()
    random_idx = int.from_bytes(digest[:8], "big") % len(eligible)
    output = {
        "random_checkpoint": int(eligible[random_idx]["step_index"]),
        "earliest_eligible": int(min(eligible, key=lambda x: int(x["step_index"]))["step_index"]),
        "normalized_quarter": int(_nearest_step(eligible, 0.25)["step_index"]),
        "normalized_midpoint": int(_nearest_step(eligible, 0.50)["step_index"]),
        "normalized_three_quarter": int(_nearest_step(eligible, 0.75)["step_index"]),
        "confidence_low": int(min(eligible, key=lambda x: float(x.get("state_token_conf_mean", 0.0)))["step_index"]),
        "entropy_high": int(max(eligible, key=lambda x: float(x.get("masked_entropy_mean", 0.0)))["step_index"]),
        "mask_ratio": int(max(eligible, key=lambda x: float(x.get("masked_ratio", 0.0)))["step_index"]),
    }
    if by_step:
        output["oof_state_value"] = max(by_step.values(), key=lambda x: float(x.get("oof_value", float("-inf"))))["step_index"]
        output["oracle_localization"] = max(by_step.values(), key=lambda x: float(x.get("q_repair_loc", -1.0)))["step_index"]
    return {k: int(v) for k, v in output.items()}


def _base_fingerprint(run_cfg: dict[str, Any], backend_cfg: dict[str, Any], adapter: Any) -> dict[str, Any]:
    dataset = run_cfg["dataset"]
    payload = {
        "git_sha": _git_sha(),
        "config_sha256": config_sha256(run_cfg),
        "model_id": backend_cfg.get("model_path"),
        "model_revision": backend_cfg.get("revision", "default"),
        "dataset_id": dataset.get("path"),
        "dataset_revision": dataset.get("revision", "default"),
        "dataset_split": dataset.get("split"),
        "subset_hash": config_sha256(
            {
                "indices": dataset.get("indices"),
                "limit": dataset.get("limit"),
                "sample_seed": dataset.get("sample_seed"),
                "config_name": dataset.get("config_name"),
            }
        ),
        "task_adapter_version": adapter.evaluator_version,
        "evaluator_id": adapter.evaluator_id,
        "evaluator_version": adapter.evaluator_version,
    }
    return {**payload, "fingerprint": scientific_fingerprint(payload)}


def _record_key(record: dict[str, Any]) -> tuple[int, int]:
    return int(record["item_id"]), int(record["trajectory_id"])


def _selected_probe_records(records: list[dict[str, Any]], policy_ids: list[int]) -> list[dict[str, Any]]:
    by_item: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_item[int(record["item_id"])].append(record)
    selected: dict[tuple[int, int], dict[str, Any]] = {}
    for item_id, rows in by_item.items():
        rows = sorted(rows, key=lambda r: int(r["trajectory_id"]))
        failed = [r for r in rows if not bool(r["correct"])]
        success = [r for r in rows if bool(r["correct"])]
        if failed:
            selected[_record_key(failed[0])] = failed[0]
        if success:
            selected[_record_key(success[0])] = success[0]
        for trajectory_id in policy_ids:
            match = next((r for r in rows if int(r["trajectory_id"]) == int(trajectory_id)), None)
            if match is not None:
                selected[_record_key(match)] = match
    return [selected[key] for key in sorted(selected)]


def _branch_row(
    *,
    run_name: str,
    record: dict[str, Any],
    step: dict[str, Any],
    operator_id: str,
    stage: str,
    branch_index: int,
    branch_seed: int,
    result: dict[str, Any],
) -> dict[str, Any]:
    compute = result.get("compute", {})
    return {
        "run_name": run_name,
        "item_id": int(record["item_id"]),
        "trajectory_id": int(record["trajectory_id"]),
        "base_correct": bool(record["correct"]),
        "step_index": int(step["step_index"]),
        "normalized_step": float(step.get("normalized_step", int(step["step_index"]) / int(step["total_steps"]))),
        "operator_id": operator_id,
        "stage": stage,
        "branch_index": int(branch_index),
        "branch_seed": int(branch_seed),
        "applicable": bool(result.get("applicable", True)),
        "correct": result.get("correct"),
        "final_answer": result.get("final_answer"),
        "modified_count": len(result.get("modified_positions", [])),
        "nfe": int(compute.get("nfe", 0)),
        "forward_calls": int(compute.get("forward_calls", 0)),
        "metadata": result.get("metadata", {}),
    }


def _group_rates(rows: list[dict[str, Any]], *, stage: str) -> dict[tuple[int, int, int, str], float]:
    buckets: dict[tuple[int, int, int, str], list[int]] = defaultdict(list)
    for row in rows:
        if row["stage"] != stage or row.get("correct") is None:
            continue
        key = (int(row["item_id"]), int(row["trajectory_id"]), int(row["step_index"]), str(row["operator_id"]))
        buckets[key].append(int(bool(row["correct"])))
    return {key: sum(values) / len(values) for key, values in buckets.items() if values}


def run(config_path: Path, *, force: bool = False) -> dict[str, Any]:
    contract = load_yaml(CONTRACT_PATH)
    validate_contract_dict(contract)
    cfg = load_yaml(config_path)
    run_name = str(cfg["run_name"])
    if not run_name.startswith("v2_"):
        raise ValueError("V2 run_name must start with v2_")
    output_root = Path(cfg.get("output_root", ROOT / "repairable_diffusion/outputs/v2_measurement"))
    if not output_root.is_absolute():
        output_root = ROOT / output_root
    run_dir = ensure_dir(output_root / run_name)

    adapter = create_task_adapter(cfg["dataset"])
    backend_cfg = _load_profile(str(cfg["model_profile"]), Path(cfg.get("profiles_path", PROFILES_PATH)))
    base_fp = _base_fingerprint(cfg, backend_cfg, adapter)
    manifest_path = run_dir / "run_manifest.json"
    if manifest_path.exists() and not force:
        old = json.loads(manifest_path.read_text(encoding="utf-8"))
        if old.get("base_fingerprint") != base_fp["fingerprint"]:
            raise RuntimeError("stale V2 run directory fingerprint mismatch; use a new run_name, not --force")
    elif manifest_path.exists() and force:
        raise RuntimeError("--force may not overwrite an existing V2 scientific run; choose a new run_name")

    records_path = run_dir / "trajectories.pkl"
    items = adapter.load_records(cfg["dataset"])
    item_lookup = {int(item["item_id"]): item for item in items}
    backend = create_v2_backend(backend_cfg, adapter)

    if records_path.exists():
        with records_path.open("rb") as fh:
            trajectory_payload = pickle.load(fh)
        records = trajectory_payload["records"]
    else:
        records = []
        trajectories_per_item = int(cfg["generation"]["trajectories_per_item"])
        for item in items:
            for trajectory_id in range(trajectories_per_item):
                records.append(backend.generate_trajectory_v2(item, trajectory_id, cfg["generation"]))
        trajectory_payload = {"records": records, "run_name": run_name, "base_fingerprint": base_fp}
        with records_path.open("wb") as fh:
            pickle.dump(trajectory_payload, fh)

    bank_hash = sha256_file(records_path)
    manifest = {
        "run_name": run_name,
        "status": "trajectory_bank_ready",
        "base_fingerprint": base_fp["fingerprint"],
        "base_provenance": base_fp,
        "trajectory_bank_hash": bank_hash,
        "git_sha": _git_sha(),
        "contract_version": contract["version"],
        "config_path": str(config_path),
        "config_sha256": config_sha256(cfg),
    }
    save_json(manifest_path, manifest)

    policy_ids = [int(x) for x in cfg.get("probe", {}).get("policy_trajectory_ids", [0])]
    probe_records = _selected_probe_records(records, policy_ids)
    all_item_ids = sorted(item_lookup)
    mechanism_items = _stable_subset(
        all_item_ids,
        count=int(cfg.get("probe", {}).get("mechanism_subset_items", min(128, len(all_item_ids)))),
        seed=int(cfg.get("probe", {}).get("mechanism_subset_seed", 271828)),
    )
    temporal_items = _stable_subset(
        all_item_ids,
        count=int(cfg.get("probe", {}).get("temporal_subset_items", min(128, len(all_item_ids)))),
        seed=int(cfg.get("probe", {}).get("temporal_subset_seed", 314159)),
    )
    root_seed = int(cfg.get("probe", {}).get("root_seed", 2027))
    b_loc = int(contract["branches"]["localization_count"])
    b_eval = int(contract["branches"]["confirmation_count"])
    operator_cfg = dict(contract["canonical_operator"])
    operator_cfg["anchor_confidence_threshold"] = float(cfg.get("operator", {}).get("anchor_confidence_threshold", 0.80))
    operator_cfg.update(cfg.get("operator", {}))

    branch_path = run_dir / "probe_branches.jsonl"
    probe_complete = run_dir / "probe_complete.json"
    if probe_complete.exists():
        branches = _jsonl_read(branch_path)
    else:
        branches: list[dict[str, Any]] = []
        # Localization / mechanism stage.
        for record in probe_records:
            item = item_lookup[int(record["item_id"])]
            for step in record["steps"]:
                snapshot = step.get("snapshot")
                if snapshot is None:
                    continue
                canonical_positions = backend.canonical_remask_positions(snapshot, operator_cfg, cfg["generation"])
                # Exact replay is a fidelity row and intentionally a single deterministic replay.
                fidelity_seed = deterministic_branch_seed(
                    root_seed=root_seed,
                    item_id=int(record["item_id"]),
                    trajectory_id=int(record["trajectory_id"]),
                    step_index=int(step["step_index"]),
                    branch_index=0,
                    stage="localization",
                )
                native = backend.run_operator_branch(
                    item,
                    snapshot,
                    cfg["generation"],
                    operator_cfg,
                    operator_id="native_continuation",
                    branch_seed=fidelity_seed,
                )
                branches.append(
                    _branch_row(
                        run_name=run_name,
                        record=record,
                        step=step,
                        operator_id="native_continuation",
                        stage="fidelity",
                        branch_index=0,
                        branch_seed=fidelity_seed,
                        result=native,
                    )
                )
                operators = ["matched_stochastic_continuation", "low_confidence_remask_v2"]
                if int(record["item_id"]) in mechanism_items and backend.backend_type == "rfba_llada_v2":
                    operators += ["random_position_remask", "core"]
                for operator_id in operators:
                    for branch_index in range(b_loc):
                        seed = deterministic_branch_seed(
                            root_seed=root_seed,
                            item_id=int(record["item_id"]),
                            trajectory_id=int(record["trajectory_id"]),
                            step_index=int(step["step_index"]),
                            branch_index=branch_index,
                            stage="localization",
                        )
                        result = backend.run_operator_branch(
                            item,
                            snapshot,
                            cfg["generation"],
                            operator_cfg,
                            operator_id=operator_id,
                            branch_seed=seed,
                            paired_modified_count=len(canonical_positions),
                        )
                        branches.append(
                            _branch_row(
                                run_name=run_name,
                                record=record,
                                step=step,
                                operator_id=operator_id,
                                stage="localization",
                                branch_index=branch_index,
                                branch_seed=seed,
                                result=result,
                            )
                        )
        _jsonl_write(branch_path, branches)
        save_json(probe_complete, {"fingerprint": base_fp["fingerprint"], "trajectory_bank_hash": bank_hash, "rows": len(branches)})

    loc_rates = _group_rates(branches, stage="localization")
    state_rows = []
    record_step_lookup: dict[tuple[int, int, int], dict[str, Any]] = {}
    for record in probe_records:
        for step in record["steps"]:
            if not step.get("snapshot"):
                continue
            key3 = (int(record["item_id"]), int(record["trajectory_id"]), int(step["step_index"]))
            record_step_lookup[key3] = step
            q_c = loc_rates.get((*key3, "matched_stochastic_continuation"), float("nan"))
            q_r = loc_rates.get((*key3, "low_confidence_remask_v2"), float("nan"))
            state_rows.append(
                {
                    "item_id": key3[0],
                    "trajectory_id": key3[1],
                    "step_index": key3[2],
                    "normalized_step": float(step.get("normalized_step", key3[2] / int(step["total_steps"]))),
                    "block_index": step.get("block_index"),
                    "step_in_block": step.get("step_in_block"),
                    "masked_ratio": float(step.get("masked_ratio", 0.0)),
                    "commitment_ratio": float(step.get("commitment_ratio", 0.0)),
                    "state_token_conf_mean": float(step.get("state_token_conf_mean", 0.0)),
                    "state_token_conf_min": float(step.get("state_token_conf_min", 0.0)),
                    "masked_entropy_mean": float(step.get("masked_entropy_mean", 0.0)),
                    "masked_entropy_max": float(step.get("masked_entropy_max", 0.0)),
                    "observed_correct": bool(step.get("observed_correct", False)),
                    "q_native_loc": q_c,
                    "q_repair_loc": q_r,
                    "delta_loc": q_r - q_c if not math.isnan(q_c) and not math.isnan(q_r) else float("nan"),
                }
            )
    finite_state_rows = [row for row in state_rows if not math.isnan(float(row["q_repair_loc"]))]
    feature_keys = [
        "normalized_step",
        "masked_ratio",
        "commitment_ratio",
        "state_token_conf_mean",
        "state_token_conf_min",
        "masked_entropy_mean",
        "masked_entropy_max",
    ]
    if len({row["item_id"] for row in finite_state_rows}) >= 2:
        scored = crossfit_value_scores(
            finite_state_rows,
            feature_keys=feature_keys,
            target_key=str(cfg.get("selector", {}).get("target", "q_repair_loc")),
            group_key="item_id",
            n_splits=int(contract["selectors"]["learned"]["folds"]),
        )
        score_map = {(r["item_id"], r["trajectory_id"], r["step_index"]): r for r in scored}
        for row in state_rows:
            match = score_map.get((row["item_id"], row["trajectory_id"], row["step_index"]))
            row["oof_value"] = match.get("oof_value") if match else float("nan")
            row["oof_fold"] = match.get("oof_fold") if match else None
    else:
        for row in state_rows:
            row["oof_value"] = row.get("q_repair_loc", float("nan"))
            row["oof_fold"] = None
    _jsonl_write(run_dir / "state_values.jsonl", state_rows)

    state_by_traj: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for row in state_rows:
        state_by_traj[(int(row["item_id"]), int(row["trajectory_id"]))].append(row)
    selector_choices: dict[tuple[int, int], dict[str, int]] = {}
    for record in probe_records:
        key = _record_key(record)
        selector_choices[key] = _selectors_for_trajectory(
            [s for s in record["steps"] if s.get("snapshot")],
            state_by_traj.get(key, []),
            root_seed=root_seed,
            item_id=key[0],
            trajectory_id=key[1],
        )

    existing_confirmation_keys = {
        (r["item_id"], r["trajectory_id"], r["step_index"], r["operator_id"], r["stage"], r["branch_index"])
        for r in branches
        if r["stage"] == "confirmation"
    }
    for record in probe_records:
        item = item_lookup[int(record["item_id"])]
        key = _record_key(record)
        required_steps = set(selector_choices.get(key, {}).values())
        if int(record["item_id"]) in temporal_items and not bool(record["correct"]):
            required_steps.update(int(s["step_index"]) for s in record["steps"] if s.get("snapshot"))
        step_map = {int(s["step_index"]): s for s in record["steps"] if s.get("snapshot")}
        for step_index in sorted(required_steps):
            step = step_map.get(step_index)
            if step is None:
                continue
            snapshot = step["snapshot"]
            canonical_positions = backend.canonical_remask_positions(snapshot, operator_cfg, cfg["generation"])
            for operator_id in ("matched_stochastic_continuation", "low_confidence_remask_v2"):
                for branch_index in range(b_eval):
                    dedup = (key[0], key[1], step_index, operator_id, "confirmation", branch_index)
                    if dedup in existing_confirmation_keys:
                        continue
                    seed = deterministic_branch_seed(
                        root_seed=root_seed,
                        item_id=key[0],
                        trajectory_id=key[1],
                        step_index=step_index,
                        branch_index=branch_index,
                        stage="confirmation",
                    )
                    result = backend.run_operator_branch(
                        item,
                        snapshot,
                        cfg["generation"],
                        operator_cfg,
                        operator_id=operator_id,
                        branch_seed=seed,
                        paired_modified_count=len(canonical_positions),
                    )
                    branches.append(
                        _branch_row(
                            run_name=run_name,
                            record=record,
                            step=step,
                            operator_id=operator_id,
                            stage="confirmation",
                            branch_index=branch_index,
                            branch_seed=seed,
                            result=result,
                        )
                    )
                    existing_confirmation_keys.add(dedup)
    _jsonl_write(branch_path, branches)

    confirm_rates = _group_rates(branches, stage="confirmation")
    selector_rows = []
    record_map = {_record_key(r): r for r in records}
    for key, choices in selector_choices.items():
        record = record_map[key]
        for selector, step_index in choices.items():
            q_c = confirm_rates.get((key[0], key[1], step_index, "matched_stochastic_continuation"))
            q_r = confirm_rates.get((key[0], key[1], step_index, "low_confidence_remask_v2"))
            selector_rows.append(
                {
                    "item_id": key[0],
                    "trajectory_id": key[1],
                    "base_correct": bool(record["correct"]),
                    "selector": selector,
                    "step_index": step_index,
                    "q_native_confirm": q_c,
                    "q_repair_confirm": q_r,
                    "delta_confirm": (q_r - q_c) if q_c is not None and q_r is not None else None,
                }
            )
    _csv_write(run_dir / "selector_confirmation.csv", selector_rows)

    # Prospective policy: frozen trajectory ids regardless of base correctness.
    primary_selector = str(cfg.get("selector", {}).get("primary", "oof_state_value"))
    post_policy_items: dict[int, list[list[bool]]] = {}
    policy_extra_nfe_by_item: dict[int, float] = {}
    confirmation_rows = [r for r in branches if r["stage"] == "confirmation" and r["operator_id"] == "low_confidence_remask_v2"]
    conf_bucket: dict[tuple[int, int, int], dict[int, dict[str, Any]]] = defaultdict(dict)
    for row in confirmation_rows:
        conf_bucket[(int(row["item_id"]), int(row["trajectory_id"]), int(row["step_index"]))][int(row["branch_index"])] = row

    by_item_records: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_item_records[int(record["item_id"])].append(record)
    for item_id, rows in by_item_records.items():
        rows = sorted(rows, key=lambda r: int(r["trajectory_id"]))
        trajectories: list[list[bool]] = []
        item_policy_nfe = []
        for record in rows:
            tid = int(record["trajectory_id"])
            if tid not in policy_ids:
                trajectories.append([bool(record["correct"])] * b_eval)
                continue
            choice = selector_choices.get((item_id, tid), {}).get(primary_selector)
            bucket = conf_bucket.get((item_id, tid, int(choice))) if choice is not None else None
            if bucket and all(b in bucket for b in range(b_eval)):
                trajectories.append([bool(bucket[b]["correct"]) for b in range(b_eval)])
                item_policy_nfe.extend(int(bucket[b]["nfe"]) for b in range(b_eval))
            else:
                trajectories.append([bool(record["correct"])] * b_eval)
        post_policy_items[item_id] = trajectories
        policy_extra_nfe_by_item[item_id] = mean(item_policy_nfe) if item_policy_nfe else 0.0

    base_passk = mean(float(any(bool(r["correct"]) for r in rows)) for rows in by_item_records.values()) if by_item_records else 0.0
    prospective_passk = paired_branch_item_pass_at_k(post_policy_items)

    # Actual aggregate-NFE-matched fresh sampling allocation. Allocation depends on
    # item id and compute only, never correctness/outcome.
    target_fresh_nfe = int(round(sum(policy_extra_nfe_by_item.values())))
    fresh_seed = int(cfg.get("probe", {}).get("fresh_control_seed", 161803))
    fresh_order = sorted(
        all_item_ids,
        key=lambda x: hashlib.sha256(f"fresh|{fresh_seed}|{x}".encode()).hexdigest(),
    )
    fresh_rows = []
    achieved_nfe = 0
    fresh_solved_items = set()
    if bool(cfg.get("compute_control", {}).get("enabled", True)) and target_fresh_nfe > 0:
        for rank, item_id in enumerate(fresh_order):
            if achieved_nfe >= target_fresh_nfe and fresh_rows:
                break
            fresh = backend.generate_trajectory_v2(item_lookup[item_id], 100000 + rank, cfg["generation"])
            nfe = int(fresh["compute"]["nfe"])
            fresh_rows.append(
                {
                    "item_id": item_id,
                    "trajectory_id": 100000 + rank,
                    "correct": bool(fresh["correct"]),
                    "nfe": nfe,
                    "final_answer": fresh.get("final_answer"),
                }
            )
            achieved_nfe += nfe
            if fresh["correct"]:
                fresh_solved_items.add(item_id)
    _jsonl_write(run_dir / "fresh_sampling.jsonl", fresh_rows)
    fresh_passk = mean(
        float(any(bool(r["correct"]) for r in rows) or item_id in fresh_solved_items)
        for item_id, rows in by_item_records.items()
    ) if by_item_records else 0.0

    # Existence / temporal metrics on the first failed trajectory per item.
    failed_first: dict[int, dict[str, Any]] = {}
    for record in probe_records:
        if not record["correct"] and int(record["item_id"]) not in failed_first:
            failed_first[int(record["item_id"])] = record
    existence_rows = []
    for item_id, record in sorted(failed_first.items()):
        key = _record_key(record)
        transient = any(bool(step.get("observed_correct", False)) for step in record["steps"] if step.get("snapshot"))
        oracle_step = selector_choices.get(key, {}).get("oracle_localization")
        q_c = confirm_rates.get((key[0], key[1], int(oracle_step), "matched_stochastic_continuation")) if oracle_step is not None else None
        q_r = confirm_rates.get((key[0], key[1], int(oracle_step), "low_confidence_remask_v2")) if oracle_step is not None else None
        temporal_rates = {
            int(step["step_index"]): confirm_rates[(key[0], key[1], int(step["step_index"]), "low_confidence_remask_v2")]
            for step in record["steps"]
            if step.get("snapshot") and (key[0], key[1], int(step["step_index"]), "low_confidence_remask_v2") in confirm_rates
        }
        t_last = last_repairable_step(temporal_rates, threshold=float(contract["measurement"]["confirmation_threshold"])) if temporal_rates else None
        existence_rows.append(
            {
                "item_id": item_id,
                "trajectory_id": key[1],
                "transient_correct": transient,
                "oracle_step": oracle_step,
                "q_native_confirm": q_c,
                "q_repair_confirm": q_r,
                "repairable_but_never_correct": bool(not transient and q_r is not None and q_r >= float(contract["measurement"]["confirmation_threshold"])),
                "confirmed_repairable": bool(q_r is not None and q_r >= float(contract["measurement"]["confirmation_threshold"])),
                "t_last": t_last,
                "temporal_confirmation_complete": item_id in temporal_items,
            }
        )
    _csv_write(run_dir / "existence.csv", existence_rows)

    report = {
        "run_name": run_name,
        **_final_report_provenance(base_fp),
        "config_sha256": config_sha256(cfg),
        "trajectory_bank_hash": bank_hash,
        "dataset": cfg["dataset"],
        "model_profile": cfg["model_profile"],
        "items": len(items),
        "trajectories": len(records),
        "base_pass_at_k": base_passk,
        "prospective_policy_selector": primary_selector,
        "prospective_policy_pass_at_k": prospective_passk,
        "prospective_net_gain": prospective_passk - base_passk,
        "policy_extra_nfe_target_for_fresh": target_fresh_nfe,
        "fresh_sampling_achieved_nfe": achieved_nfe,
        "fresh_sampling_pass_at_k": fresh_passk,
        "fresh_sampling_gain": fresh_passk - base_passk,
        "probe_branch_rows": len(branches),
        "mechanism_subset_items": sorted(mechanism_items),
        "temporal_subset_items": sorted(temporal_items),
        "existence": {
            "failed_items_probed": len(existence_rows),
            "transient_correct_rate": mean(float(r["transient_correct"]) for r in existence_rows) if existence_rows else 0.0,
            "confirmed_repairable_rate": mean(float(r["confirmed_repairable"]) for r in existence_rows) if existence_rows else 0.0,
            "repairable_but_never_correct_rate": mean(float(r["repairable_but_never_correct"]) for r in existence_rows) if existence_rows else 0.0,
        },
        "v1_artifacts_substituted": False,
    }
    save_json(run_dir / "report.json", report)
    manifest["status"] = "complete"
    manifest["report"] = "report.json"
    manifest["probe_branches_sha256"] = sha256_file(branch_path)
    save_json(manifest_path, manifest)
    return report


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    report = run(Path(args.config), force=args.force)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
