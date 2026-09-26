from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from repairable_diffusion.src.rsd_ref_v3 import runner
from repairable_diffusion.src.rsd_ref_v3.task_adapters import task_definition
from repairable_diffusion.src.utils.io import load_yaml


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "repairable_diffusion/configs/rsd_ref_v3/measurement_contract.yaml"
CONFIG_ROOT = ROOT / "repairable_diffusion/configs/rsd_ref_v3/runs"


class RSDRefV3ContractTests(unittest.TestCase):
    def test_generation_namespace_and_source_populations(self) -> None:
        cfg = load_yaml(CONTRACT)
        self.assertEqual(cfg["generation_id"], "rsd_ref_v3")
        self.assertEqual(cfg["artifact_namespace"], "rsd_ref_v3")
        self.assertEqual(cfg["design_seed"], 314159265)
        self.assertEqual(cfg["tasks"]["llada_math"]["dataset"]["count"], 5000)
        self.assertEqual(cfg["tasks"]["llada_gsm8k"]["dataset"]["count"], 1319)
        self.assertFalse(cfg["tasks"]["llada_math"]["dataset"]["bridge_is_confirmatory_population"])

    def test_all_configs_use_full_source_namespace(self) -> None:
        paths = sorted(CONFIG_ROOT.glob("*.yaml"))
        self.assertGreaterEqual(len(paths), 8)
        for path in paths:
            text = path.read_text(encoding="utf-8")
            cfg = load_yaml(path)
            self.assertEqual(cfg["generation_id"], "rsd_ref_v3")
            self.assertTrue(cfg["run_name"].startswith("rsd_ref_v3_"))
            self.assertNotIn("limit: 200", text)
            self.assertNotIn("outputs/v2_measurement", text)
            self.assertNotIn("results/v2_measurement", text)

    def test_source_native_adapter_rejects_confirmatory_bridge(self) -> None:
        native = task_definition("llada_math")
        calibration = task_definition("llada_math_calibration")
        self.assertEqual(native["count"], 5000)
        self.assertFalse(native["calibration_only"])
        self.assertEqual(calibration["count"], 500)
        self.assertTrue(calibration["calibration_only"])

    def test_selection_key_is_stable_and_purpose_separated(self) -> None:
        def key(purpose: str) -> str:
            payload = "|".join(("rsd_ref_v3", "314159265", "llada", "llada_math", purpose, "17", "0"))
            return hashlib.sha256(payload.encode("utf-8")).hexdigest()

        self.assertEqual(key("core"), key("core"))
        self.assertNotEqual(key("core"), key("temporal"))

    def test_readiness_is_fail_closed_before_storage(self) -> None:
        readiness = json.loads(runner.readiness_path().read_text(encoding="utf-8"))
        storage = json.loads(runner.storage_plan_path().read_text(encoding="utf-8"))
        self.assertEqual(readiness["server1"]["scientific_execution_qualification"], "SCIENTIFIC_EXECUTION_QUALIFIED")
        self.assertFalse(readiness["single_server_primary_gate"]["execution_allowed"])
        self.assertEqual(storage["status"], "STORAGE_NOT_RESERVED")
        self.assertFalse(storage["execution_allowed"])
        self.assertIn("expected_execution_git_sha", readiness)
        self.assertIn("design_freeze_sha256", readiness)


if __name__ == "__main__":
    unittest.main()
