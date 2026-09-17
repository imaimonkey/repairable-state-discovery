# Full-Paper Experiment Contract

This is the canonical contract for the submission-quality experiment state of `repairable-state-discovery`.

## Scientific Claim Boundary

Primary claim:

> Failed diffusion reasoning trajectories contain measurable, localized repairable intermediate states. Their location is structured by refinement state and can be partially selected without oracle intervention. Repair gain must be interpreted jointly with negative repair, selector strength, cost, seed robustness, dataset transfer, and backbone transfer.

Do not turn the paper into a claim that the diffusion model is stronger than autoregressive baselines in raw answer quality. AR rows are reference measurements.

Do not claim that the learned predictor is intrinsically superior if simple selectors such as step position, mask ratio, or entropy match it. That outcome is itself evidence that repairability is strongly structured by refinement state.

## Canonical Result Boundary

The committed 200-item results are historical analysis/development artifacts. Preserve them, but do not use them as the final main-paper tables once the full suite is complete.

Canonical full-paper results must come only from:

- `results/benchmark_complete_reports/`
- `results/benchmark_extended_analysis/`
- `results/full_paper_manifest.json`

The full-split protocol family must omit `dataset.limit` and must evaluate negative repair on all successful trajectories with `max_success_trajectories_for_negative_repair: 0`.

## Required Generation Matrix

| Protocol | Required rows | Purpose |
| --- | ---: | --- |
| `protocol_math500_full.yaml` | 1 diffusion + 2 AR | MATH-500 main result |
| `protocol_gsm8k_full.yaml` | 1 diffusion + 2 AR | GSM8K main result |
| `protocol_math500_full_robustness.yaml` | 3 diffusion | seed/stride/branch robustness |
| `protocol_math500_full_seed_repeats.yaml` | 2 diffusion | true run-to-run uncertainty |
| `protocol_gsm8k_full_seed_repeats.yaml` | 2 diffusion | true run-to-run uncertainty |
| `protocol_math500_full_dream_backbone.yaml` | 1 diffusion | second diffusion backbone |
| `protocol_gsm8k_full_dream_backbone.yaml` | 1 diffusion | second diffusion backbone |

Final aggregate target: **11 diffusion rows + 4 AR rows**.

## Required Analysis Matrix

Every full diffusion run must be included in the benchmark extended analysis with:

- predictor repair
- oracle repair
- confidence-low selector
- entropy-high selector
- mask-ratio-high selector
- early-step selector
- middle-step selector
- predictor thresholds 0.50 / 0.70 / 0.90
- predictor feature ablations
- bootstrap item-level confidence intervals
- negative repair
- repair branch cost
- matched extra-sampling approximation
- qualitative examples

The matched extra-sampling result is an approximation derived from observed sample accuracy and expected repair branch cost. It must be labeled as a proxy/approximation in the paper and must not be described as a separately decoded control unless a true decoded matched-budget baseline is actually run.

## Canonical Execution

```bash
cd /home/kimhj/repairable-state-discovery
bash scripts/full_paper_pipeline.sh preflight
PROTOCOL_NODE=<actual-slurm-node> \\
AGGREGATE_NODE=<actual-slurm-node> \\
MAX_PARALLEL_GPUS=4 \\
bash scripts/full_paper_pipeline.sh submit
bash scripts/full_paper_pipeline.sh status
# after all required protocol jobs finish successfully:
bash scripts/full_paper_pipeline.sh finalize
```

`submit` is duplicate-aware through `submit_benchmark_complete_suite.sh`: completed run artifacts and protocol reports are skipped, pending/running jobs are reused, and each independent run requests one GPU. Protocol reports are materialized by CPU-only aggregation jobs after their run-level dependencies complete. Slurm's node/QoS policy may cap concurrency below the requested node GPU count; the launcher records the actual assigned node and GPU in each log.

`finalize` rebuilds the aggregate and extended analysis, then runs a strict audit and writes `results/full_paper_manifest.json`.

## Final Readiness Gate

A full paper may treat the experiment suite as closed only when:

1. `python scripts/audit_full_paper_ready.py --mode preflight` passes.
2. All seven required full protocol reports exist and are non-dry-run with the expected run counts.
3. `results/benchmark_complete_reports/aggregate_report.json` contains exactly 11 diffusion rows and 4 AR rows.
4. `results/benchmark_extended_analysis/extended_repair_analysis.json` covers all 11 diffusion runs and all required strategy/ablation rows.
5. Final LaTeX tables exist.
6. Figure-data CSVs exist for repair curves, best-step histograms, and gain-vs-negative-repair tradeoff.
7. Qualitative examples exist.
8. `bash scripts/full_paper_pipeline.sh finalize` exits successfully and writes `results/full_paper_manifest.json`.

## Main-Paper Result Mapping

### Main table

Use the canonical full main LLaDA runs on MATH-500 and GSM8K. Report:

- pass@1
- base pass@k
- predictor repaired pass@k
- predictor gain with CI
- oracle repaired pass@k / predictor-oracle gap
- repairable-failed rate
- negative-repair rate
- peak repair step

### Robustness table

Use MATH-500 seed29 / stride16 / branch2 plus true seed repeats. Separate decoding/config robustness from repeated-seed uncertainty.

### Selector/ablation table

Compare predictor to confidence, entropy, mask ratio, early/middle step, oracle, thresholded predictor, and feature ablations. Do not hide simple-selector parity with the learned predictor.

### Cost table

Report base trajectories per item, repair branch evaluations, repair cost per item, gain per branch budget, and matched extra-sampling approximation. Explicitly mark the approximation as non-decoded unless a true decoded baseline is added.

### Backbone/dataset generalization

Use both LLaDA and Dream-v0-Instruct-7B on MATH-500 and GSM8K. Describe failures or reversals rather than filtering them out.

### Figures

Use the generated CSVs to render:

1. protocol overview
2. repair gain vs checkpoint step
3. best-step histogram
4. predictor vs oracle gap
5. gain vs negative-repair tradeoff

## Paper-Writing Rules

- Preserve the measurement/localization framing.
- Separate observed results from interpretation.
- Report uncertainty and run counts next to claims.
- Distinguish full-split results from historical 200-item diagnostics.
- Include negative repair as a first-class metric, not a footnote.
- Include limitations: limited backbone breadth, dataset breadth, selector gap, cost proxy limitations, and any failed/unstable full runs.
- Never silently drop a required experiment because it is unfavorable.
- Never copy slice numbers into final full-paper tables after the full suite is complete.

## Failure Handling

If a Slurm job fails:

1. inspect the exact log and failed run;
2. identify whether the failure is infrastructure, dependency, backend contract, OOM, data, or scientific-code related;
3. make the smallest scientifically neutral fix;
4. preserve run names, seeds, benchmark split, repair branch count, and evaluation contract unless a documented methodological correction is necessary;
5. rerun only missing/failed work;
6. document any methodological change before using the result in the paper.
