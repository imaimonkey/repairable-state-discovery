# Paper Readiness Checklist

This project should be framed as a measurement protocol for state-level repairability in diffusion reasoning trajectories.

## Current Claim

The current artifacts support the claim that failed diffusion reasoning trajectories contain measurable, localized, and partially predictable repairable intermediate states.

## Submission Blockers

1. Add uncertainty estimates.
   - Bootstrap item-level confidence intervals are available in `results/extended_analysis/`.
   - Full-split seed repeats are included in `protocol_math500_full_seed_repeats.yaml` and `protocol_gsm8k_full_seed_repeats.yaml`.
   - Report CI for base pass@k, predictor repaired pass@k, oracle repaired pass@k, and negative repair.

2. Add predictor ablations.
   - Feature ablations are available in `results/extended_analysis/`.
   - Compare all features against confidence-only, trajectory-position-only, and leave-one-feature-out variants.
   - Report predictor-oracle gap and negative repair for each ablation.

3. Add negative-repair mitigation.
   - Predictor threshold/abstention analysis is available in `results/extended_analysis/`.
   - Full-split protocols set `max_success_trajectories_for_negative_repair: 0`, removing the successful-trajectory cap used by faster slice runs.
   - Stronger mitigation may require new selector calibration or repair policy changes.
   - Report gain versus negative repair rather than gain alone.

4. Add cost-normalized comparisons.
   - A repair branch evaluation proxy and matched extra-sampling approximation are available in `results/extended_analysis/`.
   - Report base samples per item, repair branches, and total generation calls.
   - Compare predictor repair against random extra samples under a matched budget.

5. Add qualitative examples.
   - Initial examples are available in `results/extended_analysis/qualitative_examples.*`.
   - Include examples where an early state repairs successfully.
   - Include examples where late states fail.
   - Include examples where repair causes negative repair.

## Strong Additions

1. Add one more diffusion backbone if feasible.
   - Full Dream-v0-Instruct-7B protocols are included for MATH-500 and GSM8K.
2. Add one more reasoning dataset if feasible.
   - GSM8K full-split protocols are included alongside MATH-500.
3. Add a protocol overview figure.
   - Figure source is available at `docs/figures/protocol_overview.mmd`.
4. Add repair gain curves and best-step histograms for GSM8K and MATH-500.
   - Benchmark suite exports figure-data CSVs under `results/benchmark_complete_reports/figure_data/`.
5. Add a gain versus negative-repair tradeoff figure.
   - Benchmark suite exports `gain_negative_repair_tradeoff.csv`.

## Current Aggregate Outputs

- Final aggregate: `results/final_reports/`
- Submission aggregate: `results/submission_reports/`
- Benchmark-complete aggregate after full jobs finish: `results/benchmark_complete_reports/`
- Benchmark-complete extended analysis after full jobs finish: `results/benchmark_extended_analysis/`
- Protocol reports: `results/generated_configs/*_report.json`

Run-level heavy artifacts are intentionally excluded from git and should be regenerated or copied separately for archival releases.
