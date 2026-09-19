from __future__ import annotations

import unittest

from repairable_diffusion.src.v2.backends import ComputeCounter, V2DreamBackend, V2Snapshot, _restore_rng, _rng_snapshot
from repairable_diffusion.src.v2.contracts import deterministic_branch_seed, validate_contract_dict
from repairable_diffusion.src.v2.metrics import last_repairable_step, paired_branch_item_pass_at_k, summarize_state
from repairable_diffusion.src.v2.oof import crossfit_binary_scores, crossfit_value_scores
from repairable_diffusion.src.v2.provenance import assert_fingerprint_match, scientific_fingerprint
from repairable_diffusion.src.v2.task_adapters import GSM8KAdapter, Math500Adapter, MBPPAdapter


class V2ContractTests(unittest.TestCase):
    def test_branch_seed_reproducibility(self) -> None:
        kwargs = dict(root_seed=7, item_id=3, trajectory_id=2, step_index=16, branch_index=1, stage="localization")
        self.assertEqual(deterministic_branch_seed(**kwargs), deterministic_branch_seed(**kwargs))

    def test_branch_seed_independence(self) -> None:
        loc = deterministic_branch_seed(root_seed=7, item_id=3, trajectory_id=2, step_index=16, branch_index=1, stage="localization")
        confirm = deterministic_branch_seed(root_seed=7, item_id=3, trajectory_id=2, step_index=16, branch_index=1, stage="confirmation")
        self.assertNotEqual(loc, confirm)

    def test_fixed_operator_across_branches(self) -> None:
        cfg = {
            "version": "v2_counterfactual_recoverability",
            "artifact_namespace": "v2_measurement",
            "branches": {"localization_count": 4, "confirmation_count": 8, "replicate_semantics": "stochastic_seed_only"},
            "measurement": {"confirmation_threshold": 0.25, "threshold_sensitivity": [0.125, 0.25, 0.5]},
            "canonical_operator": {
                "id": "low_confidence_remask_v2",
                "position_policy": "low_confidence",
                "remask_fraction": 0.25,
                "min_remask_positions": 4,
                "continuation_temperature": "match_base",
                "schedule_mode": "phase_faithful",
            },
            "operator_controls": {"required": ["native_continuation", "matched_stochastic_continuation", "random_position_remask", "low_confidence_remask_v2", "fresh_sampling_compute_control", "core"]},
            "selectors": {"learned": {"require_oof_for_headline": True, "group_key": "item_id"}},
            "compute": {"actual_fresh_sampling_required": True, "analytic_extra_sampling_proxy_main_result": False},
        }
        validate_contract_dict(cfg)

    def test_artifact_fingerprint_invalidation(self) -> None:
        a = scientific_fingerprint({"git_sha": "a", "operator": "x"})
        b = scientific_fingerprint({"git_sha": "b", "operator": "x"})
        self.assertNotEqual(a, b)
        with self.assertRaises(RuntimeError):
            assert_fingerprint_match(a, b, artifact="probe_bank")

    def test_policy_negative_repair_accounting(self) -> None:
        items = {1: [[True, False], [False, False]]}
        self.assertAlmostEqual(paired_branch_item_pass_at_k(items), 0.5)

    def test_recoverability_decomposition(self) -> None:
        row = summarize_state(observed_correct=False, native_outcomes=[False] * 4, repair_outcomes=[True, False, True, False])
        self.assertEqual(row.category, "repairable_but_not_native")
        self.assertAlmostEqual(row.q_native, 0.0)
        self.assertAlmostEqual(row.q_repair, 0.5)
        self.assertAlmostEqual(row.intervention_lift, 0.5)

    def test_last_repairable_step(self) -> None:
        self.assertEqual(last_repairable_step({8: 0.5, 16: 0.0, 24: 0.25}, threshold=0.25), 24)

    def test_snapshot_native_replay(self) -> None:
        # Unit-level replay contract: a snapshot carries the complete explicit
        # state required by the backend replay path, including RNG state. Real
        # one-step LLaDA/Dream semantic replay is the mandatory GPU integration
        # gate in scripts/validate_v2_backends.py.
        state = _rng_snapshot()
        snapshot = V2Snapshot(
            backend_type="unit",
            schema_version="v2.3",
            step_index=8,
            total_steps=64,
            prompt_len=2,
            full_token_ids=[1, 2, 3],
            token_confidences=[0.5],
            masked_ratio=0.0,
            commitment_ratio=1.0,
            block_index=0,
            step_in_block=8,
            active_plan=[1] * 32,
            first_conf=None,
            rng_state=state,
            backend_state={},
        )
        self.assertEqual(snapshot.rng_state, state)
        _restore_rng(snapshot.rng_state)

    def test_dream_native_final_step_transfers_all_masks(self) -> None:
        import torch

        count = V2DreamBackend._native_transfer_count(
            37, step_id=63, total_steps=64, eps=1e-3, device=torch.device("cpu")
        )
        self.assertEqual(count, 37)

    def test_dream_terminal_snapshot_has_no_repair_intervention(self) -> None:
        backend = V2DreamBackend({}, Math500Adapter())
        snapshot = {
            "step_index": 64,
            "total_steps": 64,
            "prompt_len": 2,
            "full_token_ids": [1, 2, 3, 4],
            "token_confidences": [0.2, 0.9],
            "backend_state": {},
        }
        generation_cfg = {"steps": 64}
        operator_cfg = {
            "anchor_confidence_threshold": 0.80,
            "remask_fraction": 0.25,
            "min_remask_positions": 4,
        }
        self.assertEqual(
            backend.canonical_remask_positions(snapshot, operator_cfg, generation_cfg),
            [],
        )
        result = backend.intervene_snapshot(
            snapshot,
            operator_id="low_confidence_remask_v2",
            operator_cfg=operator_cfg,
            generation_cfg=generation_cfg,
            branch_seed=7,
        )
        self.assertFalse(result.applicable)
        self.assertEqual(result.modified_positions, [])
        self.assertEqual(result.metadata.get("reason"), "no_remaining_native_schedule")

    def test_zero_repair_no_positive_label(self) -> None:
        rows = []
        for item in range(6):
            for step in (8, 16):
                rows.append({"item_id": item, "x": float(step), "target": 0})
        scored = crossfit_binary_scores(rows, feature_keys=["x"], target_key="target", n_splits=3)
        self.assertTrue(all(float(row["oof_score"]) == 0.0 for row in scored))

    def test_grouped_oof_no_item_leakage(self) -> None:
        rows = []
        for item in range(10):
            for step in (8, 16, 24):
                rows.append({"item_id": item, "x": float(step), "value": float((item + step) % 5) / 4.0})
        scored = crossfit_value_scores(rows, feature_keys=["x"], target_key="value", n_splits=5)
        folds_by_item = {}
        for row in scored:
            folds_by_item.setdefault(row["item_id"], set()).add(row["oof_fold"])
        self.assertTrue(all(len(folds) == 1 for folds in folds_by_item.values()))
        self.assertTrue(all("oof_value" in row for row in scored))

    def test_task_adapter_evaluator(self) -> None:
        gsm = GSM8KAdapter()
        self.assertTrue(gsm.evaluate("1,234", "1234"))
        self.assertFalse(gsm.evaluate("1235", "1234"))
        math_adapter = Math500Adapter()
        self.assertTrue(math_adapter.evaluate("\\frac{1}{2}", "0.5"))
        sandbox = MBPPAdapter().executor
        sandbox.self_test()

    def test_operator_nfe_accounting(self) -> None:
        counter = ComputeCounter()
        counter.add_forward()
        counter.add_forward(2)
        self.assertEqual(counter.forward_calls, 3)
        self.assertEqual(counter.nfe, 3)


if __name__ == "__main__":
    unittest.main()
