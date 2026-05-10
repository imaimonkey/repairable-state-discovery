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
| Cost-normalized extra-sampling approximation | done | `results/extended_analysis/extended_repair_analysis.*` |
| Qualitative examples | done | `results/extended_analysis/qualitative_examples.*` |

## Interpretation Updates

The extended analysis shows that confidence is a weak but important baseline. Entropy and mask-ratio selectors are stronger than confidence-only selection. In the current LLaDA runs, the learned predictor often collapses to the same decision pattern as high-mask or early/middle-step selectors. This should be framed as evidence that repairability is strongly structured by refinement stage and mask state, rather than as evidence that a complex learned selector is always necessary.

## Remaining Generation Experiments

These require new model runs and cannot be produced by aggregation alone. The fast 200-item versions are submitted by `scripts/submit_paper_complete_suite.sh`; the full benchmark versions are submitted by `scripts/submit_benchmark_complete_suite.sh`.

| Component | Purpose |
| --- | --- |
| Additional seed repeats | Replace bootstrap-only uncertainty with true run-to-run uncertainty. |
| Additional diffusion backbone | Test whether repairable-state localization generalizes beyond LLaDA. |

## Paper-Complete Protocols

| Protocol | Runs |
| --- | --- |
| `protocol_math500_final.yaml` | MATH-500 LLaDA final + AR references |
| `protocol_gsm8k_final.yaml` | GSM8K LLaDA final + AR references |
| `protocol_math500_submission_robustness.yaml` | MATH-500 seed/stride/branch robustness |
| `protocol_math500_seed_repeats.yaml` | MATH-500 LLaDA seed 41 and 53 |
| `protocol_gsm8k_seed_repeats.yaml` | GSM8K LLaDA seed 29 and 41 |
| `protocol_math500_dream_backbone.yaml` | MATH-500 Dream-v0-Instruct-7B |
| `protocol_gsm8k_dream_backbone.yaml` | GSM8K Dream-v0-Instruct-7B |

## Benchmark-Complete Protocols

These protocols are the final full-split execution path. They use run names distinct from the 200-item runs, omit dataset `limit`, and set `max_success_trajectories_for_negative_repair: 0` so negative repair is evaluated over all successful trajectories.

| Protocol | Runs |
| --- | --- |
| `protocol_math500_full.yaml` | MATH-500 full LLaDA final + AR references |
| `protocol_gsm8k_full.yaml` | GSM8K full LLaDA final + AR references |
| `protocol_math500_full_robustness.yaml` | MATH-500 full seed29, stride16, branch2 |
| `protocol_math500_full_seed_repeats.yaml` | MATH-500 full LLaDA seed 41 and 53 |
| `protocol_gsm8k_full_seed_repeats.yaml` | GSM8K full LLaDA seed 29 and 41 |
| `protocol_math500_full_dream_backbone.yaml` | MATH-500 full Dream-v0-Instruct-7B |
| `protocol_gsm8k_full_dream_backbone.yaml` | GSM8K full Dream-v0-Instruct-7B |

The submitter is:

```bash
cd /home/kimhj/repairable-state-discovery
bash scripts/submit_benchmark_complete_suite.sh
```

Expected final outputs:

| Output | Contents |
| --- | --- |
| `results/benchmark_complete_reports/` | Full aggregate report, CSV summaries, rendered tables, figure-data CSVs |
| `results/benchmark_extended_analysis/` | Bootstrap CIs, strategy baselines, threshold/abstention, ablations, cost-normalized extra-sampling approximation, qualitative examples |

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
