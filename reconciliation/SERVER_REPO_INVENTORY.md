# Server and Repository Inventory

Snapshot date: 2026-09-26 KST. This is a read-only forensic snapshot; live monitors and scientific jobs may advance after this file was written.

## 1. Cluster inventory

| Logical server | Hostname | GPU inventory | Storage observed | Access/evidence | Confidence |
|---|---|---|---|---|---|
| server1 | `devbox` | 8 x NVIDIA RTX A6000, 49,140 MiB each; driver 595.71.05 | `/`: 1.8T total, 297G free (83%); `/mnt/raid5`: 21T total, 204G free (99%); inode use 5% | direct SSH and `nvidia-smi` | high |
| server2 | `server2` | Slurm advertises 8 x `gpu:a6000`; direct GPU probe was queued and terminated after resource wait | `/`: 1.8T total, 19G free (99%); inode use 6%; `/data` absent | Slurm read-only probes; direct SSH authentication unavailable | medium for node/storage, low for active GPU processes |
| server3 | `ubuntu` | 4 x NVIDIA H200 NVL, 143,771 MiB each; driver 595.71.05; all 4 had active processes | `/`: 1.8T total, 77G free (96%); `/data`: 7.0T total, 116G free (99%); inode use 3%/4% | direct local inspection and `nvidia-smi` | high |
| server4 | `server4` | Slurm advertises 8 x RTX PRO 6000 Blackwell Server Edition; assigned probe saw 97,887 MiB GPU | `/`: 1.8T total, 99G free (95%); `/data`: 7.0T total, 83G free (99%); inode use 3%/5% | Slurm read-only probes; direct SSH authentication unavailable | medium |

All four nodes were `MIXED` or `MIXED+PLANNED` in Slurm. Because the data filesystems are nearly full, this reconciliation does not create or copy large scientific outputs.

## 2. Repository/worktree inventory

The following are the relevant observed checkouts. A path marked `dynamic` is being mutated by an existing monitor/orchestrator and must not be edited during reconciliation.

| Server/path | HEAD / branch | Working tree | Role and disposition |
|---|---|---|---|
| server1 `/home/kimhj/repairable-state-discovery-v2-exec` | `0dd161c8cf4bf3e7dbe4042234a0954950ce870e`, detached | untracked `results/v2_measurement/` | V2 execution baseline; preserve outputs |
| server1 `/home/kimhj/repairable-state-discovery-v2-unified-8b1361d` | `8b1361d3d8d60a58e28847ac35af8dfc2b023d2d`, detached | clean at probe | V2 unified/Dream boundary variant; preserve, compare before reuse |
| server1 `/home/kimhj/repairable-state-discovery-v2-seal-ops-0dd-20260923` | not captured | not captured | sealing operations checkout; inspect only if needed |
| server2 `/home/kimhj/repairable-state-discovery` | not a Git repository | 9 directories observed; 77 source-like files fingerprinted | legacy source copy; identity resolved as older `LEGACY_EXPERIMENT_ONLY` variant |
| server2 `/home/kimhj/repairable-state-discovery-v2-exec` | `0dd161c8cf4bf3e7dbe4042234a0954950ce870e`, detached | untracked `results/v2_measurement/` | V2 execution baseline; preserve outputs |
| server2 `/home/kimhj/repairable-state-discovery-v2-unified-8b1361d` | not independently re-read | not captured | unified variant directory; preserve |
| server2 `/home/kimhj/repairable-state-discovery-v2-seal-ops-0dd-20260923` | not captured | not captured | sealing operations checkout |
| server3 `/data/kimhj/repairable-state-discovery` | `14a721d9bb563e1ea9289778f6e70c0a230e6e21`, `main`, behind `origin/main` by 25 | tracked generated configs and untracked generated/results files | legacy/V1 plus local overlays; do not use as canonical source |
| server3 `/data/kimhj/repairable-state-discovery-50924-artifact-ops-20260923` | `7a6c479c9c308bc74461515c22ef1e906d3c2872`, `codex/v2-gsm8k-dream-50924-provenance-20260923` | clean, behind upstream by 2 | artifact/provenance audit branch |
| server3 `/data/kimhj/repairable-state-discovery-iclr-2027` | `0dd161c8cf4bf3e7dbe4042234a0954950ce870e`, detached | dirty paper files; untracked build | paper/deadline checkout; archive |
| server3 `/data/kimhj/repairable-state-discovery-live-monitor-20260923` | dynamic `codex/iclr2027-live-monitor-20260923` | monitor-controlled | monitoring history; reimplement neutral monitor |
| server3 `/data/kimhj/repairable-state-discovery-provenance-fix-20260923` | `435e24ea1729b11a15c6ae7b8cb1bfc4f79ca6fc`, `fix/v2-stable-execution-provenance` | clean | important provenance/boundary source candidate |
| server3 `/data/kimhj/repairable-state-discovery-reference` | non-Git directory | not applicable | scratch/reference runtime; preserve |
| server3 `/data/kimhj/repairable-state-discovery-reference-20260923` | dynamic `codex/iclr2027-reference-live-20260923` | tracked scripts plus untracked runtime/status files | live reference execution; do not edit |
| server3 `/data/kimhj/repairable-state-discovery-reference-paper-20260923` | `69669e8cd4b810b5c601ed38e4cf13a9a37ff282`, `codex/reference-primary-paper-20260923` | `status/v2r/pdf_audit.json` dirty | paper/evidence importer; archive separately |
| server3 `/data/kimhj/repairable-state-discovery-seed-forensic-20260923` | `e1b56311ed6c0e46d751e67ef2c2916fbbb53ee4`, `codex/v2-seed-collision-forensic-20260923` | clean | forensic evidence; preserve as audit artifact |
| server3 `/data/kimhj/repairable-state-discovery-status-20260923` | `c41d6b10ed0c041581cae4f84a41b4ad783ebe00`, `codex/iclr2027-analysis-bundle-20260923` | clean | analysis/status bundle; archive from source core |
| server3 `/data/kimhj/repairable-state-discovery-v2-exec` | `43d8a6e1ca5075b03c63313e467359b83b00434c`, `codex/current-job-status-20260921` | clean | status/handoff checkout |
| server3 `/data/kimhj/repairable-state-discovery-v2-exec-20260925` | `926495e78f9558ee2c0a606ef9f9f641cacb78da`, detached | `scripts/submit_v2_suite.py` dirty; V2 results untracked | active measurement worktree; do not edit |
| server3 `/data/kimhj/repairable-state-discovery-v2-unified-8b1361d` | `8b1361d3d8d60a58e28847ac35af8dfc2b023d2d`, detached | clean | unified V2 source comparison |
| server4 `/data/kimhj/repairable-state-discovery` | `f45569d7d4b74674d0679851fedf27193ca0e266`, `codex/status-20260917` | dirty/untracked | legacy/V1 and status overlay |
| server4 `/data/kimhj/repairable-state-discovery-v2-exec` | `0dd161c8cf4bf3e7dbe4042234a0954950ce870e`, detached | untracked `results/v2_measurement/` | V2 execution baseline |
| server4 `/data/kimhj/repairable-state-discovery-v2-dream-hotfix-8b1361d` | `15f40e052329261885c757664273f25bede2b074`, `codex/dream-math500-compact-artifacts-20260922` | untracked V2 results | Dream/MATH-500 hotfix; preserve and compare |
| server4 `/data/kimhj/repairable-state-discovery-v2-unified-8b1361d` | `8b1361d3d8d60a58e28847ac35af8dfc2b023d2d`, detached | clean | unified V2 source comparison |

## 3. Source identity taxonomy

The earlier “six source families” count mixed scientific code, operational history, paper artifacts, and uncommitted state. The corrected taxonomy is:

### Scientific code lineage

1. `V1 legacy`: `f45569d…` and the older server2 non-Git variant.
2. `V2 historical ancestor`: `0dd161c8…` (`v2/backends.py` `5d445d…`, validator `82717e…`).
3. `V2 provenance/boundary`: `435e24e…` (`v2/backends.py` `c460ac…`, validator `5e6674…`, provenance changes).
4. `V2R canonical scientific candidate`: `78fe5d7c…`, exactly 18 commits ahead of `0dd161c8…`, with source-pinned recipes, R0/R1/R2 gates, schema/science/seeds, sampler, shard/artifact infrastructure, and tests.

### Operational/status lineage

- `926495e…` is exactly 1,470 commits ahead of `0dd161c…`; the observed delta is dominated by status, monitoring, independent dispatch, and operational history. It is not a separate scientific method lineage.
- The live monitor and reference-live branches are dynamic operational/status overlays. Their historical evidence is retained, but their moving heads are not source anchors.

### Paper/artifact lineage

Paper branches, submission bundles, PDF audits, sealed evidence indexes, and historical result bundles are derived artifacts. They retain source SHA links but are not executable scientific source.

### Uncommitted overlays

Dirty worktrees, generated configs, active result directories, and live monitor files are operational overlays. They must not be promoted into the canonical source without a manifest and review.

## 4. Server2 non-Git fingerprint result

`reconciliation/SERVER2_SOURCE_FINGERPRINT.csv` contains 77 source/config-like files from `/home/kimhj/repairable-state-discovery`, including relative path, size, mtime, and SHA-256. Results:

- 73 files match one or more known candidate worktrees exactly.
- Two files have no exact match: `repairable_diffusion/src/run_protocol.py` and `scripts/run_protocol_repairability_final.sh`.
- Read-only server2 diffs against its own V2 checkout show that both are older legacy variants: they lack the V2 path normalization and use the older AR payload shape. They do not add a server2-only scientific fix.
- The remaining apparent non-match was the CSV header, not a source file.

Therefore the server2 ambiguity is resolved as **older legacy source, no canonical-only scientific change found**. No Git conversion or source modification was performed.

## 5. Runtime and operational state

- server3 currently has LLaDA/VLLM processes on all four H200 GPUs and multiple existing monitors/orchestrators/watchdogs.
- Active tmux/process names still contain historical deadline/project labels. They are operational state, not canonical scientific source.
- V2R reference outputs are under `/var/tmp/kimhj-v2r-reference` (approximately 606M observed); independent dispatch metadata is under `/var/tmp/kimhj-v2r-independent` (approximately 88K observed).
- No existing process, job, worktree, or artifact was stopped, reset, overwritten, or deleted by this reconciliation.

## 6. Phase 2 storage prerequisite

No node currently has an approved primary-output reservation. Before any new primary trajectory execution, the execution plan must record for each selected server:

- approved output filesystem and owner;
- reserved free space of at least `max(200 GiB, 3 × projected maximum single-shard raw output)`;
- at least 10% free inode margin;
- projected shard output size, log size, and retention window;
- a verified cleanup/archive plan that does not target sealed or unclassified scientific artifacts.

The observed 95–99% filesystem utilization means Phase 2/3 execution remains storage-blocked until this reservation is explicitly approved.
