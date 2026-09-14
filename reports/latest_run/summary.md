# Latest experiment handoff

- Repository: `repairable-state-discovery`
- Analysis source commit: `1ed1a04d60dd35aed560b90200a21b376cc71b14`
- Branch: `idea/unbiased-repair-eval`
- Status: **completed** (exit code 0)
- Run path: `repairable_diffusion/outputs/runs/math500_unbiased_20260915`
- Analysis source: `repairable_diffusion/outputs/runs/math500_unbiased_20260915/report.json`
- Dataset: MATH-500, 500 items, 4,000 trajectories (8/item)
- Probe coverage: complete for 3,173 failed and 827 successful trajectories; no additional GPU probe generation is required.

## Claim-grade headline

- Base item pass@k: `0.308`
- Predictor **net** expected pass@k: `0.3975289611816406`
- Predictor **net** gain over base: `+0.08952896118164061`
- Predictor recovery-only expected pass@k: `0.41837387084960936` (diagnostic, not the headline net metric)
- Predictor expected newly solved items: `55.18693542480469`
- Predictor expected lost solved items: `10.422454833984375`
- Predictor negative-repair rate: `0.23458282950423218`
- Random-control net pass@k: `0.3660732421875`
- Confidence-control net pass@k: `0.3509825439453125`
- Oracle net pass@k: `0.502960205078125`
- Repairable failed trajectories: `975 / 3173 = 0.30728017648912703`
- Peak mean correction rate: `0.10250551528521903` at step `8`

The predictor result is evaluated with item-grouped cross-fit/OOF scoring and net damage accounting. Do not substitute recovery-only repaired pass@k for the net result, and do not relabel historical optimistic evaluations as claim-grade.

This directory is intentionally Git-trackable. Large raw artifacts remain server-local and are referenced through the handoff rather than committed.
