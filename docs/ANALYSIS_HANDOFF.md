# Analysis handoff contract

Every claim-bearing GPU run must leave a small, Git-trackable bundle in `reports/latest_run/` before the result commit is pushed.

Required files:

- `manifest.json`: source Git SHA captured before execution, branch/current SHA at export, Slurm/GPU environment, command, exit status, resolved run/report path.
- `metrics.json`: compact claim-bearing metrics, including the leakage-free/net-aware selector results when present.
- `analysis_summary.json`: the primary protocol/run report used for interpretation.
- `artifact_index.json`: paths, sizes and SHA-256 hashes for reasonably sized artifacts; large raw artifacts remain on the server.
- `stdout_tail.txt`, `stderr_tail.txt`: scheduler log tails when available.
- `summary.md`: human-readable pointer to the exact experiment source and report.

Large trajectory pickles, raw generations and caches remain ignored. The handoff is intentionally small enough to commit.

`scripts/run_protocol_repairability_final.sh` captures the source checkout before execution and exports the final protocol result automatically while preserving the experiment exit code. For any new/manual entrypoint, finish with `scripts/export_analysis_handoff.py --run-dir <exact-run-or-report-path>` and preserve `HANDOFF_SOURCE_GIT_SHA` from job start.

After the run, commit/push `reports/latest_run/` together with the intentionally updated final/submission report. Remote analysis should be able to reconstruct code provenance, protocol/config, OOF/net metrics, scheduler job and raw-artifact locations without requiring server access.
