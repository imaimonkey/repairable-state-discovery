# Paper Readiness Checklist

This project should be framed as a measurement protocol for state-level repairability in diffusion reasoning trajectories, not as a general self-correction method.

## Current Claim

The current artifacts support the claim that failed diffusion reasoning trajectories contain measurable, localized, and partially predictable repairable intermediate states.

## Submission Blockers

1. Add uncertainty estimates.
   - Run seed repeats or bootstrap item-level confidence intervals.
   - Report CI for base pass@k, predictor repaired pass@k, oracle repaired pass@k, and negative repair.

2. Add predictor ablations.
   - Compare all features against confidence-only, trajectory-position-only, and leave-one-feature-out variants.
   - Report predictor-oracle gap and negative repair for each ablation.

3. Add negative-repair mitigation.
   - Evaluate abstention thresholds.
   - Evaluate repair only when predictor confidence clears a calibrated threshold.
   - Report gain versus negative repair rather than gain alone.

4. Add cost-normalized comparisons.
   - Report base samples per item, repair branches, and total generation calls.
   - Compare predictor repair against random extra samples under a matched budget.

5. Add qualitative examples.
   - Include examples where an early state repairs successfully.
   - Include examples where late states fail.
   - Include examples where repair causes negative repair.

## Strong Additions

1. Add one more diffusion backbone if feasible.
2. Add one more reasoning dataset if feasible.
3. Add a protocol overview figure.
4. Add repair gain curves and best-step histograms for GSM8K and MATH-500.
5. Add a gain versus negative-repair tradeoff figure.

## Current Aggregate Outputs

- Final aggregate: `results/final_reports/`
- Submission aggregate: `results/submission_reports/`
- Protocol reports: `results/generated_configs/*_report.json`

Run-level heavy artifacts are intentionally excluded from git and should be regenerated or copied separately for archival releases.
