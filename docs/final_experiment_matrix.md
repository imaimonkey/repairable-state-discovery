# Final Experiment Matrix

This document separates completed analysis from experiments that require new generation.

## Completed From Existing Artifacts

These analyses use completed run artifacts and do not require additional GPU decoding.

| Component | Status | Output |
| --- | --- | --- |
| Main final aggregate | done | `results/final_reports/` |
| Submission aggregate | done | `results/submission_reports/` |
| Bootstrap item-level CI | done | `results/extended_analysis/extended_repair_analysis.*` |
| Confidence/entropy/mask-ratio strategy baselines | done | `results/extended_analysis/extended_repair_analysis.*` |
| Predictor threshold/abstention policies | done | `results/extended_analysis/extended_repair_analysis.*` |
| Predictor feature ablations | done | `results/extended_analysis/extended_repair_analysis.*` |
| Cost proxy by repair branch evaluations | done | `results/extended_analysis/extended_repair_analysis.*` |
| Qualitative examples | done | `results/extended_analysis/qualitative_examples.*` |

## Interpretation Updates

The extended analysis shows that confidence is a weak but important baseline. Entropy and mask-ratio selectors are stronger than confidence-only selection. In the current LLaDA runs, the learned predictor often collapses to the same decision pattern as high-mask or early/middle-step selectors. This should be framed as evidence that repairability is strongly structured by refinement stage and mask state, rather than as evidence that a complex learned selector is always necessary.

## Remaining Generation Experiments

These require new model runs and cannot be produced by aggregation alone.

| Component | Purpose |
| --- | --- |
| Additional seed repeats | Replace bootstrap-only uncertainty with true run-to-run uncertainty. |
| Additional diffusion backbone | Test whether repairable-state localization generalizes beyond LLaDA. |
| Additional reasoning dataset | Test dataset-level generalization beyond MATH-500 and GSM8K. |

## Submission-Ready Table Set

1. Main diffusion repairability table.
2. Strategy baseline table: confidence, entropy, mask-ratio, step prior, predictor, oracle.
3. Feature ablation table.
4. Threshold/abstention table.
5. Cost-normalized table.
6. Qualitative examples table.

## Recommended Claim

The current strongest claim is:

> Failed diffusion reasoning trajectories contain recoverable intermediate states. These states are localized in the refinement process and can often be identified by simple state signals such as mask ratio, step position, entropy, and learned combinations of those signals.

This claim is directly supported by the completed artifacts and extended analysis.
