from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


def test_export_analysis_handoff_smoke(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    run = repo / "run"
    run.mkdir(parents=True)
    (run / "report.json").write_text(json.dumps({"headline": {"net": 0.6}, "selector_deltas": {"gain": 0.1}}), encoding="utf-8")
    script = Path(__file__).resolve().parents[1] / "scripts" / "export_analysis_handoff.py"
    subprocess.run([sys.executable, str(script), "--repo-root", str(repo), "--repo-name", "smoke", "--run-dir", str(run)], check=True)
    handoff = repo / "reports" / "latest_run"
    assert (handoff / "manifest.json").is_file()
    assert (handoff / "metrics.json").is_file()
    assert (handoff / "analysis_summary.json").is_file()
    metrics = json.loads((handoff / "metrics.json").read_text())
    assert metrics["headline"]["net"] == 0.6
