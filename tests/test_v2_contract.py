from __future__ import annotations

import unittest

from repairable_diffusion.src.v2.contracts import (
    deterministic_branch_seed,
    validate_contract_dict,
)
from repairable_diffusion.src.v2.metrics import (
    last_repairable_step,
    paired_branch_item_pass_at_k,
    summarize_state,
)
from repairable_diffusion.src.v2.provenance import (
    assert_fingerprint_match,
    scientific_fingerprint,
)


class V2ContractTests(unittest.TestCase):
    def test_branch_seed_reproducibility(self) -> None:
        kwargs = dict(
            root_seed=7,
            item_id=3,
            trajectory_id=2,
            step_index=16,
            branch_index=1,
            stage="localization",
        )
        self.assertEqual(deterministic_branch_seed(**kwargs), deterministic_branch_seed(**kwargs))

    def test_branch_seed_independence(self) -> None:
        loc = deterministic_branch_seed(
            root_seed=7,
            item_id=3,
            trajectory_id=2,
            step_index=16,
            branch_index=1,
            stage="localization",
        )
        confirm = deterministic_branch_seed(
            root_seed=7,
            item_id=3,
            trajectory_id=2,
            step_index=16,
            branch_index=1,
            stage="confirmation",
        )
        self.assertNotEqual(loc, confirm)

    def test_fixed_operator_across_branches(self) -> None:
        cfg = {
            "version": "v2_counterfactual_recoverability",
            "artifact_namespace": "v2_measurement",
            "branches": {
                "localization_count": 4,
                "confirmation_count": 8,
                "replicate_semantics": "stochastic_seed_only",
            },
            "measurement": {
                "confirmation_threshold": 0.25,
                "threshold_sensitivity": [0.125, 0.25, 0.5],
            },
            "canonical_operator": {
                "id": "low_confidence_remask_v2",
                "position_policy": "low_confidence",
                "remask_fraction": 0.25,
                "min_remask_positions": 4,
                "continuation_temperature": "match_base",
                "schedule_mode": "phase_faithful",
            },
            "operator_controls": {
                "required": [
                    "native_continuation",
                    "matched_stochastic_continuation",
                    "random_position_remask",
                    "low_confidence_remask_v2",
                    "fresh_sampling_compute_control",
                    "core",
                ]
            },
            "selectors": {
                "learned": {
                    "require_oof_for_headline": True,
                    "group_key": "item_id",
                }
            },
            "compute": {
                "actual_fresh_sampling_required": True,
                "analytic_extra_sampling_proxy_main_result": False,
            },
        }
        validate_contract_dict(cfg)

    def test_artifact_fingerprint_invalidation(self) -> None:
        a = scientific_fingerprint({"git_sha": "a", "operator": "x"})
        b = scientific_fingerprint({"git_sha": "b", "operator": "x"})
        self.assertNotEqual(a, b)
        with self.assertRaises(RuntimeError):
            assert_fingerprint_match(a, b, artifact="probe_bank")

    def test_policy_negative_repair_accounting(self) -> None:
        # Item 1 has two trajectories and two policy branches. Branch 0 keeps a
        # success, branch 1 loses it; the prospective item value is therefore .5.
        items = {1: [[True, False], [False, False]]}
        self.assertAlmostEqual(paired_branch_item_pass_at_k(items), 0.5)

    def test_recoverability_decomposition(self) -> None:
        row = summarize_state(
            observed_correct=False,
            native_outcomes=[False, False, False, False],
            repair_outcomes=[True, False, True, False],
        )
        self.assertEqual(row.category, "repairable_but_not_native")
        self.assertAlmostEqual(row.q_native, 0.0)
        self.assertAlmostEqual(row.q_repair, 0.5)
        self.assertAlmostEqual(row.intervention_lift, 0.5)

    def test_last_repairable_step(self) -> None:
        self.assertEqual(last_repairable_step({8: 0.5, 16: 0.0, 24: 0.25}, threshold=0.25), 24)

    @unittest.skip("Execution gate: implemented with faithful V2 backend replay")
    def test_snapshot_native_replay(self) -> None:
        pass

    @unittest.skip("Execution gate: implemented with OOF runner integration")
    def test_zero_repair_no_positive_label(self) -> None:
        pass

    @unittest.skip("Execution gate: implemented with OOF runner integration")
    def test_grouped_oof_no_item_leakage(self) -> None:
        pass

    @unittest.skip("Execution gate: implemented with task adapters")
    def test_task_adapter_evaluator(self) -> None:
        pass

    @unittest.skip("Execution gate: implemented with backend instrumentation")
    def test_operator_nfe_accounting(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
