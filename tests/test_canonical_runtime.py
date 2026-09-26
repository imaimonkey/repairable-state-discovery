import unittest

from scripts.v2r_submit import _neutral_name
from scripts import v2r_status, v2r_watchdog


class CanonicalRuntimeTests(unittest.TestCase):
    def test_neutral_scheduler_names(self):
        self.assertEqual(_neutral_name("gate-l-r0"), "rsd-gate-l-r0")
        self.assertEqual(_neutral_name("base-l-math-s00"), "rsd-base-l-math-s00")
        with self.assertRaises(ValueError):
            _neutral_name("old-deadline-gate")

    def test_neutral_service_names_and_status_namespace(self):
        self.assertEqual(v2r_watchdog.MONITOR_SESSION, "rsd-monitor")
        self.assertEqual(v2r_watchdog.ORCHESTRATOR_SESSION, "rsd-orchestrator")
        self.assertEqual(v2r_status.OUT.name, "reset")

    def test_phase_2a_status_disables_raw_execution(self):
        self.assertEqual(v2r_status.PREFERRED_SOURCE, "78fe5d7c1829b67d1bb1416b7205edfa647bb2fa")
        self.assertEqual(v2r_status.HISTORICAL_ANCESTOR, "0dd161c8cf4bf3e7dbe4042234a0954950ce870e")


if __name__ == "__main__":
    unittest.main()
