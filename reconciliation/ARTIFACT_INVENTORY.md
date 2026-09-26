# Artifact Inventory

This inventory separates source/code, scientific artifacts, operational state, and deadline-specific material. Nothing is deleted or overwritten in this phase.

## Source/code

| Root/family | State | Classification | Action |
|---|---|---|---|
| `origin/main` `0dd161c…` | clean V2 baseline | canonical starting candidate | use as immutable base for a clean build |
| `fix/v2-stable-execution-provenance` `435e24e…` | clean branch | scientific/provenance and bug-fix candidate | preserve commits; port after tests |
| V2 unified `8b1361d…` and Dream hotfix `15f40e…` | clean source checkouts with separate result overlays | backend/protocol variant | compare hashes and behavior; do not merge blindly |
| V2R source family around `45c295f…`/`78fe5d7…` | live reference checkout is mutable | source-pinned gates, sampler, seed/artifact/shard machinery | extract generic scientific core into clean build |
| legacy `f45569d…` and server2 non-Git directory | dirty/unknown identity | V1/legacy | preserve as legacy; never use as canonical V2 source |

## Scientific artifacts

| Root | Observed content/status | Classification | Retention |
| `/var/tmp/kimhj-v2r-reference` | approximately 606M; source-pinned runtime, caches, gate execution workdirs, reference outputs | `SEALED_REFERENCE_PILOT` plus active/incomplete gates | retain; source and artifact manifests must remain linked |
| `/var/tmp/kimhj-v2r-independent` | approximately 88K metadata directories for independent server outputs | `INCOMPLETE`/active reference dispatch | retain; do not infer completion from metadata alone |
| `v2-exec-20260925/results/v2_measurement` | approximately 504K manifests/readiness plus approximately 2.0G dynamic outputs and approximately 48K logs at inspection | active measurement artifacts; mixed complete/incomplete | retain; do not edit active worktree |
| V2 pilot outputs | `v2_pilot_math500_llada`, `v2_pilot_gsm8k_llada`, `v2_bbh_logical3_llada`, `v2_bbh_logical5_llada` have completed manifests/reports; several report `SEALED` provenance | `SEALED_REFERENCE_PILOT` or completed pilot | retain and classify per manifest |
| Current V2 outputs | GSM8K and BBH logical7 trajectory banks ready but final reports absent; MBPP/Math500 queued | `INCOMPLETE` | retain until explicit scientific disposition |
| committed analysis bundles | final reports, submission reports, extended analysis, V2 artifacts, forensic files, SHA manifests | `AUXILIARY` / evidence | retain immutable copies; archive from source core |
| legacy V2/reference-primary/MATH-500/GSM8K/Dream/BBH/MBPP roots | historical pilots, outputs, manifests, and reports | `LEGACY_PILOT`, `SEALED_REFERENCE_PILOT`, `INVALID`, or `INCOMPLETE` according to their own manifest | preserve; no blanket cleanup |

## Operational state

| Root/state | Content | Classification | Action |
|---|---|---|---|
| `status/v2r/current_status.json` | development SHA, final scientific SHA `78fe5d7…`, gate results, historical cancellations | operational evidence | preserve as snapshot; do not make it canonical |
| `status/v2r/aggregate_status.json` | `SEALED_REFERENCE_EVIDENCE_AVAILABLE` | operational/evidence index | retain |
| `status/v2r/attention_required.md` | heartbeat, monitor drift, current jobs, next actions | monitoring state | retain; replace only with neutral monitor output later |
| tmux/processes | existing monitors, orchestrator, watchdogs, dispatchers, finalization waiters | live operational state | do not stop or modify |
| Slurm job records | 12 current jobs plus completed audit probes | scheduler source of truth | retain in scheduler; re-query before decisions |

## Deadline-specific material

The following are preserved but excluded from the canonical scientific source: paper branches, PDF audit state, named-deadline docs, `iclr2027-*` monitor/watchdog names, author-review state, submission bundles, and deadline priority/status files. They are evidence and paper-production inputs, not portable execution logic.

## Artifact integrity policy

- A scientific result is usable only when its execution SHA, config/recipe hash, dataset/source hash, seed registry, shard manifest, backend gate, and seal status agree.
- A trajectory bank without a final report is `INCOMPLETE`, even if the job is RUNNING or the bank file exists.
- A `SEALED` artifact is not automatically canonical source; it is an immutable evidence product tied to its recorded source identity.
- Nearly full filesystems make opportunistic copying unsafe. The canonical build should reference existing manifests and use small metadata, not duplicate raw outputs.
