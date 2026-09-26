# Commit and Diff Matrix

`origin/main` at `0dd161c8cf4bf3e7dbe4042234a0954950ce870e` is the clean, reproducible baseline observed in the local clone and remote ref. The matrix separates source changes from evidence, status, and paper/deadline material.

## Source and scientific-protocol changes

| Commit/family | Observed content | Classification | Disposition |
|---|---|---|---|
| `14c5a4a28` | Dream terminal snapshot intervention handling | `BUG_FIX_REQUIRED`, `SCIENTIFIC_REQUIRED` | retain; port after boundary tests |
| `baefbe775` | tests for Dream terminal intervention eligibility | `BUG_FIX_REQUIRED` | retain with the corresponding fix |
| `8b1361d3d` | Dream terminal intervention boundary validation | `SCIENTIFIC_REQUIRED` | retain with tests |
| `435e24ea1` | freeze V2 execution provenance at run start; run/seal changes and tests | `SCIENTIFIC_REQUIRED`, `INFRASTRUCTURE_REQUIRED` | retain; candidate cherry-pick onto canonical base |
| `e1b56311e` | seed-collision forensic audit | `SCIENTIFIC_REQUIRED` evidence | preserve audit artifact; do not treat report files as source |
| `88127ca1c`, `a9b390d34` | V2R design/upstream recipe and design identity | `SCIENTIFIC_REQUIRED` / design record | retain protocol intent; reimplement neutrally |
| `45c295fbb` | source-pinned reference gates and atomic shard infrastructure | `SCIENTIFIC_REQUIRED`, `INFRASTRUCTURE_REQUIRED` | retain/reimplement; inspect each file before porting |
| `cd1429803` | model code hashes and cache isolation | `SCIENTIFIC_REQUIRED`, `INFRASTRUCTURE_REQUIRED` | retain |
| `d7163201` | immutable shard planner | `SCIENTIFIC_REQUIRED` | retain |
| `c7a027bc` | bind scientific manifests to a reference contract | `SCIENTIFIC_REQUIRED` | retain |
| `e1b4a699b` | frozen repairability subsets from base bank | `SCIENTIFIC_REQUIRED` | retain |
| `d46aa887` | stage-aware reduction/sealing | `SCIENTIFIC_REQUIRED`, `INFRASTRUCTURE_REQUIRED` | retain |
| `4ba56a0a` | idle-GPU gate based on reference replay compatibility | `INFRASTRUCTURE_REQUIRED` | retain after neutralizing policy labels |
| `87718fa19` | import-path correction | `BUG_FIX_REQUIRED` | retain if still required by clean base |

## Operational and monitoring changes

| Commit/family | Observed content | Classification | Disposition |
|---|---|---|---|
| `78fe5d7c1` | unified scheduler observation, legacy recovery, merge/plan/monitor/watchdog/worker additions | `INFRASTRUCTURE_REQUIRED` plus `MONITORING_REQUIRED` and legacy operations | split: retain generic scheduler/artifact logic; reimplement neutral monitor; archive legacy recovery record |
| `05ffb3117` | automate base shard unlock after R2 | `INFRASTRUCTURE_REQUIRED` | retain only with explicit gate and single-writer tests |
| live-monitor branch (hundreds of `monitor:` commits) | readiness, heartbeat, drift, status loops | `MONITORING_REQUIRED` | archive history; reimplement from clean source with neutral names |
| `codex/current-job-status-20260921` | current execution status and analysis handoff snapshots | `AUXILIARY` / operational state | preserve snapshots; archive from canonical source |
| `codex/iclr2027-analysis-bundle-20260923` | distributed result/status bundle | `AUXILIARY`, `PAPER_DEADLINE_ONLY` | preserve as evidence bundle; archive from source |

## Paper/deadline and legacy material

| Family | Observed content | Classification | Disposition |
|---|---|---|---|
| `codex/reference-primary-paper-20260923` | paper structure, sealed evidence importer, PDF audit | `PAPER_DEADLINE_ONLY` | preserve for audit/paper; archive from canonical runtime |
| `codex/iclr2027-reference-live-20260923` status/paper tail | paper state, deadline status, old job cancellation/recovery | `PAPER_DEADLINE_ONLY`, `UNSAFE_OR_OBSOLETE` for generic runtime | preserve immutable evidence; reimplement only generic scientific core |
| `codex/iclr2027-live-monitor-20260923` old labels | monitor state tied to a named deadline/project | `MONITORING_REQUIRED` but deadline-bound | archive history; neutral reimplementation required |
| `f45569d…` and server2 non-Git copy | V1/legacy `run_protocol` family and generated overlays | `LEGACY_EXPERIMENT_ONLY` / `UNKNOWN` | retain for reproducibility; do not merge into V2 canonical source |
| old V2/reference-primary/MATH-500/GSM8K/Dream/BBH/MBPP outputs | prior pilots, reports, manifests, sealed evidence | `LEGACY_PILOT`, `SEALED_REFERENCE_PILOT`, `AUXILIARY`, or `INCOMPLETE` per artifact | preserve and classify; no deletion in Phase 1 |

## Key file-level differences

The source hash audit found:

- V2 baseline and unified variants share `run_protocol.py` (`60a2223c…`) but differ in `repairable_diffusion/src/v2/backends.py`: baseline `5d445d…` versus unified/provenance family `c460ac…`.
- `run_measurement.py` is identical in the inspected baseline/unified checkouts (`7f6aef…`), while the provenance-fix branch has a distinct implementation (`4c9472…`).
- `validate_v2_backends.py` differs between baseline (`82717e…`) and unified/provenance (`5e6674…`).
- Legacy V1 `run_protocol.py` hashes differ from the V2 family on server1/server2/server4, confirming that these are not interchangeable source states.

No branch is merged blindly. The matrix is a candidate set for the canonical build plan, not an authorization to rewrite live worktrees.
