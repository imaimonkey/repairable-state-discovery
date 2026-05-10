# Final Output Audit

This audit records the final-paper elements that were previously identified and whether the repository now has a concrete execution path for them.

## Status

| Requirement | Status | Implementation |
| --- | --- | --- |
| Full benchmark size, not 200-item slice | configured | `protocol_*_full*.yaml` omit dataset `limit` |
| Full negative-repair measurement | configured | Full protocols set `max_success_trajectories_for_negative_repair: 0` |
| Bootstrap confidence intervals | implemented | `repairable_diffusion/src/analysis/extended_repair_analysis.py` |
| True seed repeats | configured | MATH-500 and GSM8K full seed-repeat protocols |
| Predictor feature ablation | implemented | `abl_*` rows in extended analysis |
| Threshold/abstention policies | implemented | `predictor@0.50`, `predictor@0.70`, `predictor@0.90` rows |
| Non-predictor repair strategy baselines | implemented | confidence, entropy, mask ratio, early step, middle step, oracle |
| Cost-normalized comparison | implemented | repair-branch cost plus matched extra-sampling approximation |
| Qualitative examples | implemented | `extract_qualitative_examples.py`, max 3 per type in benchmark suite |
| Additional diffusion backbone | configured | Dream-v0-Instruct-7B full protocols |
| Additional dataset | configured | GSM8K full protocols alongside MATH-500 |
| Robustness variants | configured | MATH-500 full seed29, stride16, branch2 protocol |
| Separate final outputs from 200-item artifacts | implemented | `results/benchmark_complete_reports/`, `results/benchmark_extended_analysis/` |
| Predictor method explanation | documented | `docs/predictor_method.md` |
| Figure-data export | implemented | `results/benchmark_complete_reports/figure_data/` |
| Protocol overview figure source | documented | `docs/figures/protocol_overview.mmd` |

## Final Execution Path

```bash
cd /home/kimhj/repairable-state-discovery
bash scripts/submit_benchmark_complete_suite.sh
```

The submitter skips a protocol when its full report already exists with the expected run counts. If the report is missing but a matching Slurm job is already pending or running, it reuses that job id for the aggregate dependency instead of submitting another copy. The aggregate job depends on all missing or in-flight protocol jobs and writes the benchmark-complete reports after successful completion.

## Expected Full Reports

| Report | Expected rows |
| --- | --- |
| `protocol_math500_full_report.json` | 1 diffusion, 2 AR |
| `protocol_gsm8k_full_report.json` | 1 diffusion, 2 AR |
| `protocol_math500_full_robustness_report.json` | 3 diffusion |
| `protocol_math500_full_seed_repeats_report.json` | 2 diffusion |
| `protocol_gsm8k_full_seed_repeats_report.json` | 2 diffusion |
| `protocol_math500_full_dream_backbone_report.json` | 1 diffusion |
| `protocol_gsm8k_full_dream_backbone_report.json` | 1 diffusion |

Final aggregate target: 11 diffusion rows and 4 AR reference rows.

## Remaining Condition

The repository now has the final execution configuration. The final numeric state exists only after the benchmark-complete Slurm jobs finish successfully on `devbox`.
