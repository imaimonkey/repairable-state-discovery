from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from repairable_diffusion.src.repair.oracle import run_oracle_repair


def _config() -> dict:
    return {
        "generation": {
            "min_oracle_step": 1,
        },
        "repair": {
            "branch_temperatures": [0.0],
            "branch_remask_fractions": [0.1],
            "branch_seed_stride": 1000,
            "oracle_checkpoint_interval": 1,
        },
        "evaluation": {
            "measure_negative_repair": False,
            "max_success_trajectories_for_negative_repair": 0,
        },
    }


def _record(item_id: int) -> dict:
    return {
        "item_id": item_id,
        "trajectory_id": 0,
        "seed": item_id,
        "question": f"question-{item_id}",
        "gold_answer": "1",
        "correct": False,
        "steps": [
            {
                "step_index": 1,
                "masked_ratio": 0.5,
                "state_token_conf_mean": 0.5,
                "masked_entropy_mean": 1.0,
                "answer_candidate": None,
                "snapshot": {"item_id": item_id},
            }
        ],
    }


class _Backend:
    def __init__(self, fail_item_id: int | None = None):
        self.fail_item_id = fail_item_id
        self.calls = []

    def repair_from_snapshot(self, *, item, snapshot_dict, **_kwargs):
        self.calls.append(item["item_id"])
        if item["item_id"] == self.fail_item_id:
            raise RuntimeError("intentional interruption")
        return {
            "correct": snapshot_dict["item_id"] % 2 == 0,
            "final_answer": "1",
        }


class OracleRepairResumeTests(unittest.TestCase):
    def test_interrupted_oracle_repair_resumes_completed_records(self) -> None:
        payload = {"records": [_record(1), _record(2)]}
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            interrupted_backend = _Backend(fail_item_id=2)

            with self.assertRaisesRegex(RuntimeError, "intentional interruption"):
                run_oracle_repair(_config(), run_dir, interrupted_backend, payload)

            self.assertEqual(interrupted_backend.calls, [1, 2])
            self.assertTrue((run_dir / "oracle_repair.progress.pkl").exists())

            resumed_backend = _Backend()
            result = run_oracle_repair(_config(), run_dir, resumed_backend, payload)

            self.assertEqual(resumed_backend.calls, [2])
            self.assertEqual(len(result["results"]), 2)
            self.assertTrue((run_dir / "oracle_repair.json").exists())
            self.assertFalse((run_dir / "oracle_repair.progress.pkl").exists())


if __name__ == "__main__":
    unittest.main()
