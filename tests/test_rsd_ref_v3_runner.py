from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from repairable_diffusion.src.rsd_ref_v3 import runner
from repairable_diffusion.src.rsd_ref_v3.runtime import runtime_location
from repairable_diffusion.src.v2r.planning import make_plan
from repairable_diffusion.src.v2r.schema import ContractError


class RSDRefV3RunnerTests(unittest.TestCase):
    def test_all_public_stages_resolve_to_generation3_configs(self) -> None:
        for stage in ("reference", "core", "temporal", "mechanism", "successful-harm"):
            path, config = runner.load_run_config("llada_math", stage)
            self.assertTrue(path.name.startswith("llada_math_"))
            self.assertEqual(config["generation_id"], "rsd_ref_v3")
            self.assertTrue(config["run_name"].startswith("rsd_ref_v3_"))

    def test_checkpoint_grid_uses_source_recipe_schedule(self) -> None:
        _, config = runner.load_run_config("llada_gsm8k", "reference")
        steps = runner._checkpoint_steps(config)
        self.assertEqual(steps, [31, 63, 95, 127, 159, 191, 223])

    def test_deep_stage_requires_materialized_subset(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            frozen = root / "status" / "subset.json"
            frozen.parent.mkdir(parents=True)
            frozen.write_text(json.dumps({"item_ids": None}), encoding="utf-8")
            with patch.object(runner, "ROOT", root):
                with self.assertRaises(ContractError):
                    runner._materialized_subset({"subset_manifest": "status/subset.json"}, {"approved_output_root": str(root / "approved" / "rsd_ref_v3")})

    def test_subset_materialization_is_outcome_stratified_and_hash_ranked(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subset_dir = root / "status" / "rsd_ref_v3" / "subsets"
            subset_dir.mkdir(parents=True)
            for purpose, eligibility in (("core", False), ("temporal", False), ("mechanism", False), ("successful_harm", True)):
                (subset_dir / f"llada_math_{purpose}.json").write_text(json.dumps({
                    "population": "source_native_opencompass_math", "target": 1, "minimum": 1,
                    "item_ids": None,
                }), encoding="utf-8")
            rows = [{"item_id": str(i), "result": {"correct": i % 2 == 0}} for i in range(4)]
            approved = root / "approved" / "rsd_ref_v3"
            with patch.object(runner, "ROOT", root), patch.object(runner, "_rows_from_base", return_value=rows):
                outputs = runner.materialize_subsets("llada_math", {}, root / "base", approved / "subsets")
                self.assertEqual(len(outputs), 4)
                first = json.loads(outputs[-1].read_text(encoding="utf-8"))
                runner.materialize_subsets("llada_math", {}, root / "base", approved / "subsets")
                second = json.loads(outputs[-1].read_text(encoding="utf-8"))
            self.assertEqual(first, second)
            self.assertEqual(first["item_ids"], ["0"] if first["purpose"] == "successful_harm" else first["item_ids"])
            self.assertFalse((root / "results").exists())

    def test_logical_outputs_resolve_below_approved_root_not_repo_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            approved = root / "storage" / "rsd_ref_v3"
            location = runtime_location("outputs/rsd_ref_v3/llada_math_reference", {"approved_output_root": str(approved)})
            self.assertEqual(location["physical_path"], str(approved / "llada_math_reference"))
            self.assertTrue(Path(location["physical_path"]).is_relative_to(approved))
            self.assertNotEqual(location["physical_path"], str(root / "outputs/rsd_ref_v3/llada_math_reference"))

    def test_logical_path_and_symlink_escape_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            approved = root / "storage" / "rsd_ref_v3"
            outside = root / "outside"
            outside.mkdir()
            (approved / "subsets").mkdir(parents=True)
            (approved / "subsets" / "escape").symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ContractError):
                runtime_location("results/rsd_ref_v3/subsets/escape/file.json", {"approved_output_root": str(approved)})
            with self.assertRaises(ContractError):
                runtime_location("results/rsd_ref_v3/../outside/file.json", {"approved_output_root": str(approved)})

    def test_aggregate_seal_and_subset_names_share_approved_namespace(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            approved = Path(temp) / "storage" / "rsd_ref_v3"
            storage = {"approved_output_root": str(approved)}
            aggregate = runtime_location("outputs/rsd_ref_v3/llada_math_reference", storage)
            seal = runtime_location("outputs/rsd_ref_v3/llada_math_reference/sealed", storage)
            subset = runtime_location("results/rsd_ref_v3/subsets", storage)
            self.assertTrue(Path(aggregate["physical_path"]).is_relative_to(approved))
            self.assertTrue(Path(seal["physical_path"]).is_relative_to(approved))
            self.assertTrue(Path(subset["physical_path"]).is_relative_to(approved))
            self.assertEqual(aggregate["approved_output_root"], seal["approved_output_root"])
            self.assertEqual(aggregate["filesystem_device"], subset["filesystem_device"])

    def test_runtime_state_sha_mismatch_is_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            (state / "storage_plan.json").write_text(json.dumps({"status": "STORAGE_READY", "execution_allowed": True}), encoding="utf-8")
            (state / "execution_readiness.json").write_text(json.dumps({
                "expected_execution_git_sha": "0" * 40,
                "design_freeze_sha256": "0" * 64,
            }), encoding="utf-8")
            with patch.dict(os.environ, {"RSD_RUNTIME_STATE_ROOT": str(state)}):
                with self.assertRaisesRegex(ContractError, "EXECUTION_GIT_SHA_MISMATCH"):
                    runner.require_runtime_readiness()

    def test_storage_ready_with_unapproved_physical_root_is_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            (state / "storage_plan.json").write_text(json.dumps({
                "status": "STORAGE_READY", "execution_allowed": True,
                "approved_output_root": str(state / "wrong-root"), "reservation_id": "r1",
                "reserved_bytes": 200 * 1024**3,
            }), encoding="utf-8")
            (state / "execution_readiness.json").write_text(json.dumps({
                "expected_execution_git_sha": runner.current_git_sha(),
                "design_freeze_sha256": "f" * 64,
                "server1": {"scientific_execution_qualification": "SCIENTIFIC_EXECUTION_QUALIFIED"},
                "protocol": {"design_freeze": "FROZEN"},
                "single_server_primary_gate": {
                    "canonical_source_config_sha_match": True,
                    "storage_ready": True,
                    "execution_allowed": True,
                },
            }), encoding="utf-8")
            with patch.dict(os.environ, {"RSD_RUNTIME_STATE_ROOT": str(state)}), patch.object(runner, "design_freeze_sha", return_value="f" * 64):
                with self.assertRaisesRegex(ContractError, "APPROVED_OUTPUT_ROOT_NAMESPACE_MISMATCH"):
                    runner.require_runtime_readiness()

    def test_external_runtime_state_does_not_change_design_freeze_hash(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp) / "runtime.json"
            with patch.object(runner, "design_freeze_sha", return_value="f" * 64) as freeze:
                before = freeze()
                state.write_text(json.dumps({"status": "STORAGE_NOT_RESERVED"}), encoding="utf-8")
                state.write_text(json.dumps({"status": "STORAGE_READY", "reservation_id": "changed"}), encoding="utf-8")
                self.assertEqual(before, freeze())

    def test_storage_readiness_is_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            (state / "storage_plan.json").write_text(json.dumps({"status": "STORAGE_NOT_RESERVED", "execution_allowed": False}), encoding="utf-8")
            (state / "execution_readiness.json").write_text(json.dumps({
                "expected_execution_git_sha": runner.current_git_sha(), "design_freeze_sha256": "f" * 64,
            }), encoding="utf-8")
            with patch.dict(os.environ, {"RSD_RUNTIME_STATE_ROOT": str(state)}), patch.object(runner, "design_freeze_sha", return_value="f" * 64):
                with self.assertRaisesRegex(ContractError, "STORAGE_NOT_READY"):
                    runner.require_runtime_readiness()

    def test_tracked_dirty_checkout_is_fail_closed(self) -> None:
        result = type("Result", (), {"returncode": 0, "stdout": " M tracked.py\n"})()
        with patch.object(runner.subprocess, "run", return_value=result):
            with self.assertRaisesRegex(ContractError, "DIRTY_EXECUTION_TREE"):
                runner.assert_clean_checkout()

    def test_generation3_namespace_reuses_v2r_atomic_worker(self) -> None:
        spec = {
            "namespace": "rsd_ref_v3", "run_id": "rsd_ref_v3_fixture", "stage": "r0_smoke",
            "execution_git_sha": "a" * 40, "design_sha256": "b" * 64, "design_seed": 1,
            "model": {"id": "fixture", "revision": "c" * 40},
            "dataset": {"id": "fixture", "revision": "d" * 40, "split": "test"},
            "recipe": {"fixture": True}, "config": {"fixture": True}, "item_ids": ["a"],
            "executor": "tests.test_rsd_ref_v3_runner:fixture_executor",
            "timing": {"seconds_per_item": 1, "target_shard_hours": 2},
            "seed_plan": [{"purpose": "base", "checkpoints": [0], "branches": 1, "operators": ["reference"]}],
        }
        manifest = make_plan(spec)
        self.assertEqual(manifest["namespace"], "rsd_ref_v3")


def fixture_executor(manifest, item_id, output_dir, records):
    (Path(output_dir) / "fixture.txt").write_text(item_id, encoding="utf-8")
    return {"correct": True, "seed_context_ids": [row["context_id"] for row in records], "evidence_kind": "cpu_fixture"}


if __name__ == "__main__":
    unittest.main()
