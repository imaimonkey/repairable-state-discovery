# ICLR 2027 Repairable-State-Discovery observation snapshot

Generated: `2026-09-23T13:53:16+09:00 KST`  
Collector/source commit: `0dd161c8cf4bf3e7dbe4042234a0954950ce870e`

This snapshot is read-only operational evidence. It does not change scientific
code/configuration/protocols, active jobs, execution worktrees, or aggregate
outputs. Server1 artifact fields remain unknown because its SSH endpoint denied
the available credentials; unknown values are not inferred from an older file.

## Current job summary

| job | model × task | node | Slurm | elapsed / limit | report | provenance | aggregate |
|---|---|---|---|---|---|---|---|
| 50668 | LLaDA × MATH-500 | server1/devbox | RUNNING | 3-22:39:11 / 30d | unobserved | unobserved | ineligible while active |
| 50669 | LLaDA × GSM8K | server1/devbox | RUNNING | 3-22:39:11 / 30d | unobserved | unobserved | ineligible while active |
| 50924 | Dream × GSM8K | server4 | RUNNING | 3-18:21:42 / 30d | absent | absent | ineligible while active |
| 50738 | LLaDA × BBH logical3 | server1/devbox | COMPLETED | 2-05:13:34 / 30d | unobserved | unobserved | unknown until artifacts observed |
| 50753 | LLaDA × BBH logical7 | server2 | COMPLETED | 2-19:20:49 / 30d | present | SEALED | run-level eligible |
| 50754 | LLaDA × MBPP | server2 | COMPLETED | 2-18:19:02 / 30d | present | SEALED | run-level eligible |
| 50923 | Dream × MATH-500 | server4 | COMPLETED | 1-05:48:51 / 30d | present | SEALED | run-level eligible |
| 50752 | LLaDA × BBH logical5 | server2 | FAILED | 1-09:56:11 / 30d | absent | absent | explicitly excluded |

Newly completed relative to the 2026-09-21 status snapshot: `50738`, `50753`,
`50754`. Current active jobs: `50668`, `50669`, `50924`.

## Pipeline interpretation

The machine-readable stage statuses and artifact counts are in
[`iclr2027_current_status.json`](./iclr2027_current_status.json). Observed
completed runs reached report and SEALED provenance. 50924 has trajectory,
probe, and state-value artifacts; its next observed stage is confirmation.
50752 reached trajectory/probe/state-value artifacts and failed during
continuation before producing report/provenance.

## Frozen V2 matrix

See [`v2_experiment_matrix.csv`](./v2_experiment_matrix.csv). Values are copied
only from observed `report.json` fields. Oracle and negative-repair columns are
`null` where no scalar was exposed by the report; no estimate was substituted.

## Artifact index

See [`v2_artifact_index.json`](./v2_artifact_index.json) for absolute paths,
sizes, mtimes, run SHA, report/provenance presence, and line/data-row counts.

Observed sealed runs:

- 50753: 58,896 probe rows; 2,944 state-value rows; 3,680 selector rows;
  177 existence rows.
- 50754: 60,336 probe rows; 3,024 state-value rows; 3,780 selector rows;
  237 existence rows.
- 50923: 106,872 probe rows; 5,576 state-value rows; 6,970 selector rows;
  497 existence rows.

## Dream-MATH-500 (50923)

Existing per-run analysis is present at:

- `/data/kimhj/repairable-state-discovery-v2-dream-hotfix-8b1361d/results/v2_measurement/v2_math500_dream_analysis.json`
- `/data/kimhj/repairable-state-discovery-v2-dream-hotfix-8b1361d/results/v2_measurement/v2_math500_dream_analysis.md`

The status index is: failed-only temporal landscape **canonical**; all-base-failed
stratification **per-run**; never-saved-correct **per-run**; transient correctness
**per-run**; oracle checkpoint histogram **derivable**; OOF checkpoint histogram
**per-run**; successful-vs-failed temporal separation **derivable**; negative
repair **per-run**; oracle-vs-prospective **per-run**; CI **missing**;
`T_last`/survival **derivable**. No new analysis code was written.

## BBH5 forensic (50752)

The forensic index enumerates `34,672` confirmation candidates. Shard 00 covers
ordinals `0..8667` (`8,668/8,668`, complete); ordinals `8668..34671`
(`26,004`) remain. The original failure branch is identified from the original
stderr: LLaDA continuation exhausted the fixed schedule with 100 masks and
refused extra post-hoc steps. The exact candidate replay completed without
re-triggering that failure; no scientific fix was applied.

Details are in the `bbh5_forensic` object of the JSON snapshot and the absolute
paths in [`v2_artifact_index.json`](./v2_artifact_index.json).

## Aggregate

No provisional or final V2 aggregate was created. The canonical command is
`python scripts/aggregate_v2_results.py` (normally through
`bash scripts/run_v2_suite.sh aggregate`), targeting
`results/v2_measurement/aggregate_report.json`. It was not run because active
rows remain, 50752 failed, and 50738 artifacts could not be observed. Existing
`results/final_reports/aggregate_report.json` and
`results/submission_reports/aggregate_report.json` are retained as historical
non-V2 artifacts and were not used or overwritten. See
[`aggregate_status.json`](./aggregate_status.json).

## Server/Git and paper repo

See [`server_repo_map.md`](./server_repo_map.md) for execution/development/
artifact/status worktree separation and preserved SHA differences.

Paper repo observation:

- path: `/data/kimhj/repairable-state-discovery-iclr-2027`
- remote: `git@github.com:imaimonkey/repairable-state-discovery.git`
- branch: detached at `0dd161c8`
- dirty: modified `paper/sections/04_experiments.tex`, modified
  `paper/sections/09_reproducibility.tex`, untracked `paper/build/`
- main TeX: `/data/kimhj/repairable-state-discovery-iclr-2027/paper/main.tex`
- latest result-integration commit: `15f40e05` (`Add compact Dream MATH500 V2 result artifact`)
- `paper/figures/` and `paper/tables/` are absent in this checkout
- a read-only build check in `/tmp` passed with Tectonic exit code 0; existing
  undefined-reference and overfull-box warnings remain.

## Main blocker

The final aggregate is not ready: 3 target jobs are still active, BBH5 is a
failed/excluded row, and server1 artifact access prevents confirming 50738 and
the live stage of 50668/50669. No data was fabricated to fill those gaps.

