# Codex V2 Final Execution Playbook

This is the final execution handoff for the V2 paper experiments. Read `AGENTS.md` first. The scientific design is frozen; Codex is expected to validate, launch, monitor, resume, collect, and aggregate the frozen experiment. **Codex must not edit, commit, or push repository code.**

## 0. Mission

Produce final-paper-grade V2 artifacts for counterfactual state-level recoverability with no silent scientific deviations.

The exact source-of-truth order is:

1. `AGENTS.md`
2. `docs/v2_scientific_contract.md`
3. `repairable_diffusion/configs/v2/measurement_contract.yaml`
4. this file
5. V2 run configs

When implementation and contract disagree, fix implementation. Do not loosen gates or change the contract to make code pass.

## 1. Allowed scope

Codex may:

- configure paths/environment/Slurm resources through untracked environment variables and command-line flags;
- use clean node-local checkouts of the exact committed SHA;
- monitor, collect, and retry failed jobs with the same scientific fingerprint;
- report deterministic implementation bugs with exact logs.

Codex may not edit tracked code/config/tests/docs, commit, or push. Any repository change is returned to the research owner for implementation and a new SHA.

Codex must not, without explicit human approval:

- add/remove benchmark tasks;
- change dataset subsets or seeds;
- change branch counts/checkpoint schedule;
- change operator hyperparameters;
- change evaluator semantics;
- change headline selectors/metrics;
- optimize settings after seeing pilot/full results;
- convert V1 outputs into V2 evidence.

If a frozen requirement is infeasible, STOP and report the exact blocker.

## 2. Frozen execution matrix

### Tier A — deep anchor

- `v2_math500_llada`
- `v2_gsm8k_llada`

Required: trajectory bank, observed correctness, matched stochastic continuation, canonical repair, simple selectors, OOF value estimator, independent confirmation, prospective policy accounting, negative repair/harm, NFE, and actual fresh-sampling compute control.

### Tier B — paired mechanism controls

On the predeclared paired state subset of Tier A:

- native exact replay/fidelity control
- matched stochastic continuation (`q_C`)
- random-position remask
- low-confidence canonical remask (`q_R`)
- CoRe-snapshot

Do not interpret `native_continuation` as the `q_C` estimator; it is a replay/fidelity row.

### Tier C — cross-domain thin validation

- BBH `logical_deduction_three_objects`
- BBH `logical_deduction_five_objects`
- BBH `logical_deduction_seven_objects`
- MBPP sanitized test

Required thin rows only: base, matched continuation, canonical repair, primary non-oracle selection, oracle diagnostic.

### Tier D — backbone thin validation

- Dream-v0-Instruct-7B × MATH-500
- Dream-v0-Instruct-7B × GSM8K

Required thin rows only: base, matched continuation, canonical repair, primary non-oracle selection, oracle diagnostic.

## 3. Frozen pilot

Pilots exist only to establish semantic correctness and resource feasibility. They may not be used to tune scientific parameters.

Run exactly the pilot configs committed under `repairable_diffusion/configs/v2/runs/`.

The frozen pilot configs are LLaDA-only and gate the primary Tier A path. A pilot PASS requires:

- no stale-artifact fingerprint mismatch;
- branch-seed reproducibility/independence tests pass;
- LLaDA native replay test passes;
- localization/confirmation seed sets are disjoint;
- every operator row records NFE/forward calls;
- MBPP sandbox self-test passes before any MBPP model output execution;
- reports can be reloaded and aggregated without manual editing.

Dream has a separate GPU replay gate through `scripts/validate_v2_backends.py --backend dream`; there is no Dream pilot dependency on the primary LLaDA path.

Do not inspect effect direction as a reason to edit configs.

## 4. Mandatory command order

From repository root:

```bash
set -euo pipefail

git status --short
git rev-parse HEAD

bash scripts/run_v2_suite.sh preflight
python scripts/validate_v2_backends.py --backend llada
bash scripts/run_v2_suite.sh pilot-primary
python scripts/audit_v2_design.py --mode primary
```

Only after all four succeed:

```bash
python scripts/submit_v2_suite.py --tier primary --dry-run
python scripts/submit_v2_suite.py --tier primary
```

The Dream transfer gate is independent:

```bash
python scripts/validate_v2_backends.py --backend dream
python scripts/audit_v2_design.py --mode dream
python scripts/submit_v2_suite.py --tier dream --dry-run
python scripts/submit_v2_suite.py --tier dream
```

LLaDA breadth may be submitted after the primary gate with `--tier breadth`.

Monitor with:

```bash
python scripts/submit_v2_suite.py --status
```

Resume failed/incomplete jobs only with the same run config and fingerprint, and only within the affected already-cleared tier:

```bash
python scripts/submit_v2_suite.py --tier primary --resume
python scripts/submit_v2_suite.py --tier dream --resume
python scripts/submit_v2_suite.py --tier breadth --resume
```

After completion:

```bash
bash scripts/run_v2_suite.sh aggregate
python scripts/audit_v2_design.py --mode final
```

## 5. Scientific implementation checks

### Snapshot fidelity

For LLaDA snapshots preserve enough state to reproduce the native transition semantics from the next step: current token sequence, active block, within-block progress, transfer schedule/remaining plan, generation parameters, and RNG state for exact replay.

For Dream snapshots preserve the current sequence, diffusion step index, fixed total steps, native sampler identity/parameters (`alg`, `alg_temp`, `eps`), generation parameters, pinned model/source revision, and RNG state. V2.3 follows the official Dream native sampler; the legacy custom `first_conf` state is not part of Dream's native replay semantics.

The exact replay test compares transition state/next-step behavior, not merely final answer equality.

### Branch semantics

`B_loc` and `B_eval` use disjoint deterministic stage-separated seeds. In a single `q_R` or `q_C` estimate, every non-seed operator hyperparameter is identical.

### Canonical intervention

`low_confidence_remask_v2` uses the committed contract values. For LLaDA it modifies only committed positions in the current active block. It does not reopen completed blocks. The remaining active-phase schedule may be recomputed only as documented by the operator implementation, without adding post-hoc extra decoding steps.

### Random control

At each paired checkpoint, random remask modifies the same count of eligible positions as the canonical targeted intervention and uses the same continuation budget.

### CoRe-snapshot

Use the public CoRe context-brittleness scoring semantics as a checkpoint-local adaptation. Record the source repository/revision. Label the row `CoRe-snapshot`; never describe it as a byte-for-byte reproduction of full-sequence CoRe.

### Learned localization

Use grouped OOF by `item_id`. Headline learned targets are continuous `q_R` or `Delta_R`. State-local and cross-trajectory variants remain separate. A trajectory with zero recovery at every checkpoint must not gain a fabricated positive label.

### Prospective policy

Retrospective diagnostic recovery may condition on known final failure. Prospective policy value may not. Apply the frozen policy trajectory set regardless of original correctness and count intervention-caused degradation.

### Fresh-sampling control

Generate real fresh samples. Match aggregate additional NFE as closely as possible with a deterministic, outcome-independent allocation rule. Report exact achieved NFE; do not claim exact matching if the discrete fresh-sample unit causes a residual budget difference.

## 6. Runtime priority under deadline

Priority is scientific validity, then Tier A completeness, then mechanism controls, then breadth.

If wall-clock time becomes critical, do not change scientific parameters. Instead follow this allowed priority order:

1. complete both Tier A runs;
2. complete exact replay + matched continuation + random remask + canonical repair on Tier B;
3. complete fresh-sampling controls;
4. complete CoRe-snapshot;
5. complete Dream thin transfer;
6. complete BBH/MBPP thin breadth;
7. optional DecoCal remains omitted unless all above are complete.

If time expires, aggregate the completed frozen tiers and explicitly mark missing tiers. Never replace a missing frozen result with V1 or a cheaper unregistered surrogate.

## 7. Failure policy

For a failed job:

1. capture log and job id;
2. classify as infrastructure, deterministic code bug, OOM, unavailable asset, or scientific-gate failure;
3. if no repository edit is required, correct only environment/Slurm/runtime setup and rerun the exact same scientific config;
4. if a repository edit is required, stop the affected tier and report the exact blocker for owner-side patching;
5. record infrastructure-only deviations in `final_execution_manifest.json`.

Stop and ask for human approval if the only fix requires changing a frozen scientific parameter.

## 8. Final artifacts

The run is not complete until all available frozen tiers are represented in:

- `results/v2_measurement/aggregate_report.json`
- `results/v2_measurement/table1_existence.csv`
- `results/v2_measurement/table2_mechanisms.csv`
- `results/v2_measurement/table3_localization.csv`
- `results/v2_measurement/figure_data/recoverability_landscape.csv`
- `results/v2_measurement/figure_data/repairability_survival.csv`
- `results/v2_measurement/figure_data/recovery_harm_compute.csv`
- `paper/v2_generated/tables/`
- `results/v2_measurement/final_execution_manifest.json`

The final manifest must include:

- final git SHA;
- every config hash;
- dataset/model identifiers and revisions where available;
- run/job ids;
- PASS stamps for preflight/backend validation;
- missing optional rows;
- infrastructure-only deviations;
- explicit statement that V1 results were not substituted.

## 9. Final report back to the researcher

At the end, report only:

1. final git SHA;
2. PASS/FAIL status of each readiness gate;
3. completed/missing frozen runs;
4. exact result artifact paths;
5. any infrastructure-only deviations;
6. scientific blockers requiring human judgment.

Do not redesign the paper or propose new experiments unless asked after the frozen matrix is complete.
