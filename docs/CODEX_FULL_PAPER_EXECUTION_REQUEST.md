# Codex Request: Execute and Close the Full Repairable-State Paper

Work directly on the current remote repository `imaimonkey/repairable-state-discovery` and its server checkout at `/home/kimhj/repairable-state-discovery`.

Your objective is to take the project from the current benchmark-complete pipeline state to a **fully executed, audited, paper-ready full-paper state**, without changing the scientific question merely to improve numbers.

Read these files first and treat them as binding contracts:

1. `docs/full_paper_experiment_contract.md`
2. `docs/final_experiment_matrix.md`
3. `docs/final_output_audit.md`
4. `docs/final_paper_outline.md`
5. `docs/predictor_method.md`
6. `README.md`

## 1. Preserve the research claim and historical results

The paper is a measurement/localization paper about **state-level repairability in diffusion reasoning trajectories**.

The central question is whether a failed diffusion reasoning trajectory passed through an intermediate state from which it could still be recovered, where such states occur, and how well non-oracle state signals can localize them.

Do not turn the paper into a raw DLM-vs-AR performance claim. AR models are reference baselines for answer quality.

Do not delete, overwrite, or relabel the existing 200-item results. They are historical development/analysis artifacts. Once the full suite is complete, the main-paper tables must use only the canonical full-split outputs.

Do not hide cases where the learned predictor is matched by simple selectors. If mask ratio, step prior, or entropy matches the predictor, report that faithfully and interpret it as refinement-state structure.

## 2. Sync and audit the repository before running anything

From `/home/kimhj/repairable-state-discovery`:

```bash
git status
git fetch origin
git pull --ff-only
bash scripts/full_paper_pipeline.sh preflight
bash scripts/full_paper_pipeline.sh status
```

Do not reset or discard unrelated local work. If the checkout is dirty, inspect the diff first and preserve valid local work.

The preflight must pass before submitting experiments. If it fails, fix the pipeline/configuration rather than bypassing the audit.

## 3. Execute the complete full-split experiment matrix

Use the canonical entry point:

```bash
bash scripts/full_paper_pipeline.sh submit
```

This must cover all seven full protocols:

- `protocol_math500_full.yaml`
- `protocol_gsm8k_full.yaml`
- `protocol_math500_full_robustness.yaml`
- `protocol_math500_full_seed_repeats.yaml`
- `protocol_gsm8k_full_seed_repeats.yaml`
- `protocol_math500_full_dream_backbone.yaml`
- `protocol_gsm8k_full_dream_backbone.yaml`

The expected final aggregate is exactly:

- 11 diffusion rows
- 4 autoregressive reference rows

The full protocols must remain full-split: no `dataset.limit`.

All full diffusion runs must keep:

```yaml
evaluation:
  max_success_trajectories_for_negative_repair: 0
```

so negative repair is measured over all successful trajectories.

The submitter is duplicate-aware. Reuse existing completed reports and pending/running jobs rather than launching duplicate runs.

## 4. Monitor jobs to actual completion

Do not stop after submission.

Inspect Slurm job state, output logs, error logs, generated protocol reports, and per-run artifacts until every required run is either successfully complete or has a diagnosed failure.

For failures:

1. inspect the exact traceback/log;
2. determine whether it is infrastructure, dependency, backend integration, OOM, dataset, serialization, evaluation, or scientific-code failure;
3. make the smallest scientifically neutral fix;
4. preserve the intended dataset split, run names, seeds, branch counts, checkpoint protocol, and evaluation contract;
5. rerun only the missing/failed work;
6. document any change that can alter scientific interpretation.

Do not reduce dataset size, silently reduce branch count, silently remove a backbone, or replace a failed experiment with the old 200-item result just to finish.

## 5. Build the canonical final result package

After all seven protocol reports are complete, run:

```bash
bash scripts/full_paper_pipeline.sh finalize
```

This must regenerate and validate:

- `results/benchmark_complete_reports/aggregate_report.json`
- `results/benchmark_complete_reports/diffusion_summary.csv`
- `results/benchmark_complete_reports/ar_summary.csv`
- `results/benchmark_complete_reports/tables/`
- `results/benchmark_complete_reports/figure_data/`
- `results/benchmark_extended_analysis/extended_repair_analysis.{json,csv,md}`
- `results/benchmark_extended_analysis/qualitative_examples.{json,md}`
- `results/full_paper_manifest.json`

Then run the strict gate again:

```bash
python scripts/audit_full_paper_ready.py --mode final --write-manifest
```

Do not call the experiment suite complete unless this exits successfully.

## 6. Analyze all required scientific questions

Using only the canonical full-split results for final claims, compute and report:

### Main repairability result

For canonical MATH-500 and GSM8K LLaDA runs:

- sample accuracy
- pass@1
- base pass@k
- predictor repaired pass@k
- predictor gain over base
- 95% bootstrap CI for repaired pass@k and gain
- oracle repaired pass@k
- predictor-oracle gap
- repairable failed rate
- peak repair step
- negative-repair rate

### Robustness

Analyze separately:

- MATH seed29
- MATH stride16
- MATH branch2
- MATH repeated seeds 41 and 53
- GSM8K repeated seeds 29 and 41

Do not mix configuration robustness with true repeated-seed uncertainty. Summarize seed mean/std where meaningful.

### Selector strength

Compare:

- confidence-low
- entropy-high
- mask-ratio-high
- early-step
- middle-step
- predictor
- predictor@0.50
- predictor@0.70
- predictor@0.90
- oracle

Quantify whether the learned predictor adds value beyond simple state/refinement signals. If not, state that clearly.

### Predictor ablations

Compare:

- all features
- confidence only
- mask/entropy only
- step only
- no confidence
- no mask
- no step

Report held-out grouped predictor accuracy/ROC-AUC as diagnostic metrics, but keep repaired pass@k, gain, and negative repair as the paper-relevant outcomes.

### Cost-normalized analysis

Report:

- base trajectories per item
- selected failed/success trajectories
- repair branch count
- estimated repair branch evaluations
- repair cost per item
- gain per 1k repair branch evaluations
- matched extra-sampling approximation
- gain over the matched extra-sampling approximation

The current matched extra-sampling result is a **proxy/approximation**, not a separately decoded control. Label it as such everywhere. If compute and time allow, add a true decoded matched-budget extra-sampling baseline as a stronger experiment, but do not replace or blur the proxy distinction.

### Dataset/backbone transfer

Compare the repairability phenomenon across:

- MATH-500 vs GSM8K
- LLaDA-8B vs Dream-v0-Instruct-7B

Report whether repairable-state localization, peak timing, selector ordering, and negative repair are consistent or dataset/backbone dependent.

### Qualitative analysis

Include representative cases for:

- early repair success
- late repair failure
- negative repair

Do not cherry-pick only favorable examples; use the generated selection logic or document any manual selection rule.

## 7. Produce final paper figures and tables

Use the canonical outputs rather than manually copied numbers.

Required main-paper artifacts:

1. Main diffusion repairability table
2. AR reference table
3. Robustness/seed table
4. Selector comparison table
5. Predictor ablation table
6. Cost-normalized table
7. Protocol overview figure
8. Repair-gain-vs-step figure
9. Best-step histogram
10. Predictor-vs-oracle figure or table
11. Gain-vs-negative-repair tradeoff figure

Source figure data already comes from:

- `repair_gain_curves.csv`
- `best_step_histograms.csv`
- `gain_negative_repair_tradeoff.csv`

Make plotting scripts deterministic and save both vector/PDF and PNG where practical. Do not hard-code result values into plotting code.

## 8. Update or create the full paper source

Search the repository for an existing manuscript first.

If a manuscript already exists, update it in place.

If no manuscript source exists, create a clean `paper/` LaTeX structure suitable for an ICLR-style full paper, with at least:

- `paper/main.tex`
- `paper/sections/01_introduction.tex`
- `paper/sections/02_related_work.tex`
- `paper/sections/03_method.tex`
- `paper/sections/04_experiments.tex`
- `paper/sections/05_results.tex`
- `paper/sections/06_analysis.tex`
- `paper/sections/07_limitations.tex`
- `paper/sections/08_conclusion.tex`
- `paper/figures/`
- `paper/tables/`

Use the framing in `docs/final_paper_outline.md`, but rewrite sections as a coherent full paper rather than copying the outline verbatim.

The paper's contribution structure should remain:

1. formalize state-level repairability as a measurable property of diffusion reasoning trajectories;
2. introduce an oracle repair protocol that localizes recoverable intermediate states;
3. evaluate non-oracle state selection and quantify the predictor-oracle gap;
4. show that repair gain must be interpreted jointly with negative repair, cost, and robustness.

Do not overclaim causality beyond the intervention actually performed by the repair probe.

Do not claim broad DLM generality if Dream or dataset transfer does not support it.

## 9. Results-writing requirements

Every main quantitative claim must be traceable to a canonical generated file.

In Results and Analysis:

- state exact dataset and model;
- state whether a number is full-split or historical slice;
- include confidence intervals where available;
- separate main runs, seed repeats, and config robustness;
- report negative repair next to positive repair gain;
- describe simple-selector parity honestly;
- describe the extra-sampling baseline as approximate unless it was truly decoded;
- report failed or inconsistent backbone results as limitations rather than deleting them.

The old 200-item numbers may be mentioned only as development/history or sanity-check material, clearly labeled as such. They must not populate final main tables after the full suite passes.

## 10. Reproducibility appendix / artifact traceability

Add a reproducibility section or appendix that records:

- exact model profiles
- datasets/splits
- full protocol config paths
- seeds
- number of trajectories per item
- repair branch count
- checkpoint schedule
- predictor feature list
- grouped item split for predictor evaluation
- negative-repair definition
- bootstrap procedure
- cost accounting definition
- commands required to reproduce the final suite
- `results/full_paper_manifest.json` as the machine-readable final source map

## 11. Validate code and paper before committing

At minimum run:

```bash
python -m compileall repairable_diffusion scripts
python scripts/audit_full_paper_ready.py --mode final --write-manifest
```

Run any repository tests that are available and add targeted tests if you change scientific logic.

Compile the LaTeX paper if a TeX environment is available. Fix broken references, missing figures, malformed tables, and compilation errors.

## 12. Commit and push

When the full suite and paper updates are genuinely complete:

1. inspect `git diff` carefully;
2. ensure no model weights, caches, giant run artifacts, secrets, or logs are staged;
3. commit code/config/docs/paper/generated small tables/figures needed for the manuscript;
4. preserve heavy run-level artifacts outside git as intended by `.gitignore`;
5. push the completed state to the remote branch used for the paper.

Use clear commits that separate scientific-code fixes from final paper/result updates when possible.

## Completion report

At the end, report all of the following concretely:

- final commit SHA
- branch pushed
- seven protocol report completion states
- 11 diffusion / 4 AR aggregate count
- strict audit result
- paths to canonical tables and figures
- paths to the final paper source and compiled PDF if available
- main full-split numerical findings
- seed robustness summary
- Dream backbone summary
- selector/ablation conclusion
- negative-repair conclusion
- cost-normalized conclusion
- any failed experiments or unresolved limitations

Do not report completion merely because jobs were submitted. Completion means the strict final audit passes and the paper has been updated from the canonical full-split results.
