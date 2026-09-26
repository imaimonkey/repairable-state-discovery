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
| server2 `/home/kimhj/repairable-state-discovery` | not a Git repository | 9 directories observed | legacy/source copy; exact source identity unresolved |
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

## 3. Source identity evidence

The tracked source hashes establish at least these distinct committed source families:

1. Legacy/V1 `f45569d…` (plus an unidentifiable non-Git server2 copy).
2. V2 baseline `0dd161c…` (`v2/backends.py` hash `5d445d…`, validator `82717e…`).
3. V2 boundary/provenance `435e24e…` (`v2/backends.py` `c460ac…`, validator `5e6674…`, provenance changes).
4. V2 unified/Dream `8b1361d…` and server4 hotfix `15f40e…` (same key V2 hash family, different commit ancestry/packaging).
5. Active measurement overlay `926495e…` with uncommitted submission and result state.
6. V2R reference execution pinned at `78fe5d7…`, with a separate dynamic development/status checkout.

Thus the defensible answer is **six committed source families plus uncommitted overlays**. The exact count of all physical copies is larger; the server2 non-Git copy prevents an exact whole-filesystem count without changing it into a Git checkout.

## 4. Runtime and operational state

- server3 currently has LLaDA/VLLM processes on all four H200 GPUs and multiple existing monitors/orchestrators/watchdogs.
- Active tmux/process names still contain historical deadline/project labels. They are operational state, not canonical scientific source.
- V2R reference outputs are under `/var/tmp/kimhj-v2r-reference` (approximately 606M observed); independent dispatch metadata is under `/var/tmp/kimhj-v2r-independent` (approximately 88K observed).
- No existing process, job, worktree, or artifact was stopped, reset, overwritten, or deleted by this reconciliation.
