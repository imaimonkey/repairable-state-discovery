# repairable-state-discovery

This repository studies **state-level repairability in diffusion language-model reasoning trajectories**.

The central question is:

> When a diffusion reasoning trajectory ends in a wrong answer, did it pass through an intermediate state from which the reasoning could still be recovered?

We operationalize this question as a protocol for collecting diffusion reasoning trajectories, probing intermediate checkpoints with local repair, localizing recoverable states, and evaluating whether a lightweight predictor can select useful repair points without oracle access.

## Claim

Failed diffusion reasoning trajectories can contain **repairable intermediate states**. These states are not uniformly distributed across denoising/refinement steps; they concentrate around dataset-dependent checkpoints and can be partially identified by a lightweight selector.

This project should be framed as a **measurement and localization protocol**. Local repair is used primarily as an operational probe for measuring recoverability of intermediate states.

## Contributions

1. We define state-level repairability for diffusion reasoning trajectories.
2. We introduce an oracle repair protocol that probes failed trajectories at intermediate checkpoints.
3. We compare practical step selectors: random, confidence-based, predictor-based, and oracle selection.
4. We report repair gain together with negative repair, exposing a gain-safety tradeoff.
5. We provide MATH-500, GSM8K, and robustness runs with aggregate reports and paper-ready tables.

## Protocol Overview

For each reasoning problem, the protocol performs:

1. **Trajectory collection**  
   Generate multiple diffusion reasoning trajectories and record intermediate refinement states.

2. **Failure filtering**  
   Identify trajectories whose final answer is incorrect.

3. **Checkpoint probing**  
   For each failed trajectory, restart from selected intermediate states and apply a local repair operator.

4. **Oracle localization**  
   Measure which checkpoint, if any, can recover the trajectory into a correct final answer.

5. **Predictor selection**  
   Train a lightweight predictor over state-level features to choose repair checkpoints without oracle repair trials.

6. **Aggregate evaluation**  
   Report base pass@k, repaired pass@k, newly solved items, repairable failed rate, predictor-oracle gap, and negative repair.

## Metrics

| Metric | Meaning |
| --- | --- |
| `item_pass_at_1` | Fraction of items solved by the first trajectory/sample. |
| `item_pass_at_k` | Fraction of items solved by any of the sampled trajectories. |
| `expected_repaired_item_pass_at_k` | Expected item-level pass@k after applying selected repair. |
| `predictor_gain_over_base_pass_at_k` | Repaired pass@k minus base pass@k. |
| `repairable_failed_rate` | Fraction of failed trajectories with at least one repairable checkpoint. |
| `peak_step_index` | Checkpoint with highest mean correction rate. |
| `oracle_minus_predictor_expected_pass_at_k` | Remaining gap between oracle selection and predictor selection. |
| `negative_repair_rate` | Fraction of originally successful trajectories harmed by the repair policy. |

## Experimental Setup

### Diffusion Model

- Main diffusion model: `GSAI-ML/LLaDA-8B-Instruct`
- Backend: local LLaDA/RFBA integration
- Repair operator: anchored remask with multi-branch restart probing
- Predictor: logistic-regression step scorer over trajectory/state features

### Datasets

- `MATH-500`
- `GSM8K`

The completed numeric artifacts in this repository were produced on a 200-item evaluation slice with 8 trajectories per item. The benchmark-complete suite below removes the dataset `limit` and writes separate full-split reports so full runs do not mix with slice results.

### Baselines

Autoregressive baselines are included as reference points, not as the primary object of analysis.

- `Qwen/Qwen2.5-7B-Instruct`
- `meta-llama/Meta-Llama-3.1-8B-Instruct`

## Main Results

### Diffusion Repairability Summary

| dataset | model | pass@1 | pass@k | pred repaired pass@k | pred gain | oracle-pred gap | peak step | repairable failed rate | neg repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| math500 | llada_8b_fast | 0.2300 | 0.3450 | 0.4578 | 0.1128 | 0.0890 | 16 | 0.3309 | 0.2050 |
| gsm8k | llada_8b_fast | 0.4900 | 0.7100 | 0.8336 | 0.1236 | 0.0404 | 8 | 0.6716 | 0.1787 |

### MATH-500 Robustness Variants

| variant | base pass@k | pred repaired pass@k | pred gain | oracle-pred gap | peak step | neg repair |
| --- | --- | --- | --- | --- | --- | --- |
| seed29 | 0.3350 | 0.4426 | 0.1076 | 0.1101 | 16 | 0.2125 |
| stride16 | 0.3450 | 0.4759 | 0.1309 | 0.0210 | 16 | 0.2725 |
| branch2 | 0.3450 | 0.4403 | 0.0953 | 0.0989 | 16 | 0.2275 |

### Autoregressive Reference

| dataset | model | pass@1 | pass@k |
| --- | --- | --- | --- |
| math500 | qwen2_5_7b_instruct | 0.4450 | 0.5650 |
| math500 | llama_3_1_8b_instruct | 0.3900 | 0.6100 |
| gsm8k | qwen2_5_7b_instruct | 0.8350 | 0.9550 |
| gsm8k | llama_3_1_8b_instruct | 0.7750 | 0.9350 |

## Interpretation

The current evidence supports the repairability framing:

- Predictor-selected repair improves diffusion pass@k by roughly 9.5 to 13.1 points across the completed runs.
- Repairability is localized: GSM8K peaks at step 8, while MATH-500 variants consistently peak around step 16.
- GSM8K has a larger repairable failed rate, suggesting more recoverable failed trajectories under the current probe.
- MATH-500 remains harder and shows a larger predictor-oracle gap in several settings.

Autoregressive rows are reference measurements for raw answer quality. The paper argument is the state-level measurement protocol and the observation that failed diffusion trajectories often contain recoverable intermediate states.

## Paper Readiness

The repository contains enough evidence for a draft focused on protocol, measurement, and localization. The 200-item artifacts now support analysis development; the benchmark-complete suite is the final execution path for submission-quality tables.

The final table set is configured to include:

1. Seed repeats plus bootstrap confidence intervals.
2. Predictor feature ablations.
3. Threshold/abstention analysis for negative-repair mitigation.
4. Cost-normalized comparisons against extra-sampling approximations.
5. Qualitative examples of successful repair, failed repair, and negative repair.
6. Additional diffusion-backbone coverage through Dream-v0-Instruct-7B and dataset coverage through GSM8K.

See [docs/final_experiment_matrix.md](docs/final_experiment_matrix.md), [docs/paper_readiness_checklist.md](docs/paper_readiness_checklist.md), [docs/final_output_audit.md](docs/final_output_audit.md), and [docs/predictor_method.md](docs/predictor_method.md) for the completed extended analyses, benchmark-complete generation plan, and predictor method details.

## Repository Layout

```text
repairable-state-discovery/
├── README.md
├── docs/
│   ├── final_paper_outline.md
│   └── paper_readiness_checklist.md
├── repairable_diffusion/
│   ├── configs/
│   │   ├── model_profiles.yaml
│   │   └── final/
│   │       ├── protocol_math500_final.yaml
│   │       ├── protocol_gsm8k_final.yaml
│   │       └── protocol_math500_submission_robustness.yaml
│   └── src/
│       ├── run_pipeline.py
│       ├── run_protocol.py
│       ├── run_ar_baseline.py
│       ├── analysis/
│       ├── backends/
│       ├── collect/
│       ├── data/
│       ├── repair/
│       └── utils/
├── results/
│   ├── generated_configs/
│   ├── final_reports/
│   └── submission_reports/
├── scripts/
└── tests/
```

Heavy run-level artifacts are excluded from git:

- `.hf_home/`
- `repairable_diffusion/outputs/`
- logs, pickle files, JSONL trajectory dumps, and Python caches

The repository tracks source code, configs, protocol reports, and aggregate summary tables.

## Installation

```bash
cd repairable-state-discovery
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -r requirements.txt
```

The diffusion backend reuses an external RFBA/LLaDA implementation. Set:

```bash
export RFBA_ROOT=/absolute/path/to/rfba
```

## Running Protocols

### Dry Run

```bash
python -m repairable_diffusion.src.run_protocol \
  --protocol repairable_diffusion/configs/final/protocol_math500_final.yaml \
  --dry-run
```

### Final Protocols

```bash
PROTOCOL_PATH=repairable_diffusion/configs/final/protocol_math500_final.yaml \
  sbatch scripts/run_protocol_repairability_final.sh

PROTOCOL_PATH=repairable_diffusion/configs/final/protocol_gsm8k_final.yaml \
  sbatch scripts/run_protocol_repairability_final.sh

PROTOCOL_PATH=repairable_diffusion/configs/final/protocol_math500_submission_robustness.yaml \
  sbatch scripts/run_protocol_repairability_final.sh
```

### Paper-Complete Suite

This is the fast paper-analysis pipeline over the existing 200-item protocol family. It skips protocol reports that are already complete, submits only missing generation jobs, then builds the paper-complete aggregate, extended strategy/ablation analysis, cost proxy, and qualitative examples.

```bash
cd /home/kimhj/repairable-state-discovery
bash scripts/submit_paper_complete_suite.sh
```

The suite covers:

- MATH-500 final
- GSM8K final
- MATH-500 robustness variants
- MATH-500 LLaDA seed repeats
- GSM8K LLaDA seed repeats
- MATH-500 Dream-v0-Instruct-7B backbone
- GSM8K Dream-v0-Instruct-7B backbone

### Benchmark-Complete Suite

This is the final full-split execution pipeline. It uses separate run names and report names, omits dataset `limit`, evaluates negative repair over all successful trajectories, runs full seed repeats/backbone/robustness protocols, then builds full aggregate tables, bootstrap intervals, strategy baselines, threshold/abstention analysis, feature ablations, cost-normalized extra-sampling approximations, and qualitative examples.

The submitter is duplicate-aware: it skips completed protocol reports and reuses pending/running Slurm jobs with the same benchmark job names instead of submitting another copy.

```bash
cd /home/kimhj/repairable-state-discovery
bash scripts/submit_benchmark_complete_suite.sh
```

The suite covers:

- MATH-500 full LLaDA final + AR references
- GSM8K full LLaDA final + AR references
- MATH-500 full robustness variants: seed29, stride16, branch2
- MATH-500 full LLaDA seed repeats: seed41, seed53
- GSM8K full LLaDA seed repeats: seed29, seed41
- MATH-500 full Dream-v0-Instruct-7B backbone
- GSM8K full Dream-v0-Instruct-7B backbone

### Build Aggregate Reports

```bash
bash scripts/build_final_report.sh
bash scripts/build_submission_report.sh
```

### Build Extended Analysis

The extended analysis computes item-level bootstrap intervals, additional repair strategies, predictor threshold policies, feature ablations, cost proxies, and qualitative examples from existing run artifacts.

```bash
python -m repairable_diffusion.src.analysis.extended_repair_analysis \
  --run-dir repairable_diffusion/outputs/runs/math500_final_llada8b_fast \
  --run-dir repairable_diffusion/outputs/runs/gsm8k_final_llada8b_fast \
  --run-dir repairable_diffusion/outputs/runs/math500_submit_llada8b_fast_seed29 \
  --run-dir repairable_diffusion/outputs/runs/math500_submit_llada8b_fast_stride16 \
  --run-dir repairable_diffusion/outputs/runs/math500_submit_llada8b_fast_branch2 \
  --output-dir results/extended_analysis \
  --bootstrap 1000
```

Aggregate outputs:

```text
results/paper_complete_reports/
  aggregate_report.json
  diffusion_summary.csv
  ar_summary.csv
  tables/

results/benchmark_complete_reports/
  aggregate_report.json
  diffusion_summary.csv
  ar_summary.csv
  tables/
  figure_data/

results/benchmark_extended_analysis/
  extended_repair_analysis.json
  extended_repair_analysis.csv
  extended_repair_analysis.md
  qualitative_examples.json
  qualitative_examples.md

results/final_reports/
  aggregate_report.json
  diffusion_summary.csv
  ar_summary.csv
  tables/

results/submission_reports/
  aggregate_report.json
  diffusion_summary.csv
  ar_summary.csv
  tables/
```

## Reuse And Partial Runs

The pipeline is designed to reuse existing artifacts:

- `run_pipeline.py` reuses trajectory, oracle, predictor, and selection-eval artifacts when available.
- `run_protocol.py` reuses run-level `report.json` files.
- AR baselines write progress files and can resume interrupted runs.
- Partial protocol reruns merge with existing protocol reports instead of dropping unrelated rows.

Example partial rerun:

```bash
PROTOCOL_PATH=repairable_diffusion/configs/final/protocol_math500_final.yaml \
PROTOCOL_FAMILIES=ar \
  sbatch scripts/run_protocol_repairability_final.sh
```

## Known Limitations

- Current committed numeric results use a limited evaluation slice; the benchmark-complete jobs must finish before full-split submission tables are available.
- The 200-item reports are kept as diagnostic artifacts and should not be mixed with benchmark-complete tables.
- Negative repair remains nontrivial and should be treated as a central safety metric.
- Tests are currently limited and should be expanded around protocol aggregation and reporting.
