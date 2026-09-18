# CODEX: Execute V2 Now

This is the one-shot execution entrypoint for the final paper experiment. **Do not stop after planning. Execute the workflow end-to-end until jobs are submitted/monitored/aggregated, or until a stop condition in `AGENTS.md` is reached.**

## Instruction to Codex

Read, in order:

1. `AGENTS.md`
2. `docs/v2_scientific_contract.md`
3. `repairable_diffusion/configs/v2/measurement_contract.yaml`
4. `docs/CODEX_V2_FINAL_EXECUTION.md`
5. `docs/distributed_cluster_execution.md`

Then execute the frozen V2 experiment. The research design and repository implementation are owned outside Codex. You are an **execution/verification-only agent**: do not edit tracked files, do not commit, and do not push.

### Non-negotiable behavior

- Do not change RQs, datasets, task subsets, checkpoint schedule, branch counts, operator hyperparameters, evaluator semantics, selectors, confirmation threshold, or primary metrics.
- Do not use V1 results as substitutes for missing V2 rows.
- Do not tune anything after looking at pilot/full results.
- Do not silently skip negative/null/inconsistent results.
- Do not call `native_continuation` the estimator of `q_C`; `matched_stochastic_continuation` is `q_C` and native continuation is the replay/fidelity control.
- Label the external context-brittleness control `CoRe-snapshot`, not full unmodified CoRe.
- If a scientific gate fails, stop and report. Never weaken the gate.

### Infrastructure reality

The four Slurm/GPU nodes may have different local filesystems. Do not assume the submitting node's absolute repository or environment path exists on the allocated node.

Before GPU submission:

- determine the node-local repository, Python environment, HF cache, RFBA root, and Dream playground root for each target node;
- synchronize or clone **the exact final git SHA** to every execution node;
- verify the remote commit marker/SHA before submission;
- use environment variables such as `RFBA_ROOT`, `DIFFUSION_PLAYGROUND_ROOT`, `HF_HOME`, `PYTHON_BIN`, and Slurm resource/path overrides instead of editing frozen scientific configs;
- if launcher/path/backend behavior requires a code fix, stop the affected tier and report the exact blocker; do not edit or commit repository code;
- synchronize every completed V2 run directory to one aggregation root before aggregation. Never aggregate from an incomplete partial copy.

### Mandatory execution order

From the final committed checkout:

```bash
set -euo pipefail

git status --short
git rev-parse HEAD

bash scripts/run_v2_suite.sh preflight
python scripts/validate_v2_backends.py --backend llada
bash scripts/run_v2_suite.sh pilot-primary
python scripts/audit_v2_design.py --mode primary
```

If and only if all gates pass, inspect the Slurm commands first:

```bash
python scripts/submit_v2_suite.py --tier primary --dry-run
```

Then submit using the infrastructure arrangement appropriate for the independent node filesystems. If all allocated nodes expose the same repository path, the suite launcher may be used directly:

```bash
python scripts/submit_v2_suite.py --tier primary
```

Otherwise submit the same frozen configs per node with the exact same final SHA and node-local paths, preserving the scientific fingerprint. This is an infrastructure adaptation and must not edit the run YAMLs.

In parallel or afterward, execute the independent Dream transfer gate:

```bash
python scripts/validate_v2_backends.py --backend dream
python scripts/audit_v2_design.py --mode dream
python scripts/submit_v2_suite.py --tier dream --dry-run
python scripts/submit_v2_suite.py --tier dream
```

A Dream failure must not block already-ready LLaDA Tier A. LLaDA breadth may be submitted with `--tier breadth` after the primary gate.

Monitor continuously with Slurm (`squeue`/`sacct`) and the repository status tooling. Retry only failed/incomplete jobs with the same config/fingerprint. If a failure indicates a code change is required, stop and report it for owner-side patching. Do not rerun completed scientific artifacts under a changed implementation SHA.

After all available frozen runs have been collected at the aggregation root:

```bash
bash scripts/run_v2_suite.sh aggregate
python scripts/audit_v2_design.py --mode final
```

### Deadline priority

If wall-clock time is insufficient, preserve the frozen design and complete in this order:

1. Tier A MATH-500/LLaDA and GSM8K/LLaDA;
2. replay/fidelity + matched continuation + random remask + canonical repair mechanism controls;
3. actual fresh-sampling compute controls;
4. CoRe-snapshot;
5. Dream MATH/GSM transfer;
6. BBH logical-deduction and MBPP breadth;
7. optional methods only after all required rows.

Do not replace a missing lower-priority tier with a cheaper unregistered experiment.

### Completion condition

Do not report “done” merely because jobs launched. Completion means:

- readiness stamps are PASS and tied to the final SHA;
- both frozen pilots are complete under that SHA;
- all completed full-run artifacts are collected;
- Tier A is complete for a final-paper-ready core result;
- `aggregate_report.json`, Tables 1–3 CSVs, figure-data CSVs, generated LaTeX tables, and `final_execution_manifest.json` exist;
- `python scripts/audit_v2_design.py --mode final` passes for the completed required core;
- missing lower-priority frozen tiers, if any, are explicitly reported rather than substituted.

At the end report only the final SHA, gate PASS/FAILs, job/run completion, exact artifact paths, infrastructure-only deviations, and genuine scientific blockers.
