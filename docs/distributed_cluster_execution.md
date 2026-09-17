# Distributed Slurm execution across independent node filesystems

The four GPU nodes are in one Slurm cluster (`lab-cluster`), but their local
filesystems are not identical. A job submitted from one node must therefore
not assume that the submitter's absolute workspace, Python environment, HF
cache, or RFBA checkout exists on the allocated node.

## Roles

- GitHub is the source of truth for code, configs, and immutable job manifests.
- Slurm is the source of truth for running state, dependencies, retries, and
  node placement. A compute node does not need to act as a main node.
- Run artifacts are not stored in GitHub. Trajectories and pickle/JSONL outputs
  must be copied to a shared artifact collector or synchronized to the node
  where aggregation will run.

## Node bootstrap

For every target node, clone the exact commit into a node-local workspace and
prepare that node's model/runtime caches before submitting GPU jobs:

```bash
git clone https://github.com/imaimonkey/repairable-state-discovery.git \
  "$NODE_WORKSPACE"
git -C "$NODE_WORKSPACE" checkout "$EXPERIMENT_COMMIT"
```

Submit with explicit node-local values:

```bash
REPAIRABLE_ROOT="$NODE_WORKSPACE" \
PYTHON_BIN="$NODE_PYTHON" \
HF_HOME="$NODE_HF_HOME" \
RFBA_ROOT="$NODE_RFBA_ROOT" \
sbatch --chdir="$NODE_WORKSPACE" ... \
  scripts/run_protocol_repairability_final.sh
```

The launcher also discovers these values from `$HOME` and known local
locations when they are not explicitly exported. The exact commit, hostname,
CUDA assignment, HF cache, and RFBA root are written to each run log.

When the nodes do not share a filesystem, synchronize the lightweight
workspace before submitting there:

```bash
# First make sure the destination account accepts this user's SSH public key.
bash scripts/preflight_rsync_nodes.sh 10.0.12.121 10.0.12.163

# Copy code/configs/scripts, excluding model caches, logs, trajectories, and
# generated full-paper reports. The destination receives .experiment_commit.
bash scripts/rsync_node_workspace.sh 10.0.12.121 /home/kimhj
bash scripts/rsync_node_workspace.sh 10.0.12.163 /data/kimhj
```

The workspace script is resumable and does not delete destination files by
default. For a disposable destination clone only, `RSYNC_DELETE=1` enables
`--delete-delay`; do not use that option against a shared or manually managed
directory. After synchronization, submit from the destination workspace with
that node's local Python/HF/RFBA paths. The current server2/server4 setup is
not yet ready for this step until SSH public-key authentication is enabled.

## Artifact synchronization

Do not aggregate a distributed protocol until every run directory is visible
at the aggregation root. A safe pattern is:

1. run each GPU job in its node-local workspace;
2. submit an `afterok` `scripts/sync_run_artifacts.sh` job for that run to the
   artifact collector;
3. make the protocol aggregate depend on the synchronization jobs;
4. make the benchmark aggregate and paper finalize depend on all protocol
   aggregates.

GitHub status files can record completion and checksums, but GitHub should not
be used as the transport for large trajectory artifacts.

The sync wrapper uses resumable `rsync --partial --append-verify` and writes a
`.sync_complete` marker only after the required artifacts are present. The
aggregate job should require that marker, so an interrupted transfer cannot be
mistaken for a completed run. For an AR run, set
`SYNC_REQUIRED_FILES=ar_baseline_summary.json`.

For a distributed run, invoke `scripts/sync_run_artifacts.sh` from the node
that produced the run and point it at the aggregation node. It is deliberately
separate from workspace synchronization: code/config transfer happens before
submission, while run-artifact transfer happens only after the producing job
finishes successfully.

## Monitoring while Codex is offline

The dependency graph continues in Slurm after the submitting shell or Codex
session exits. Submit `scripts/monitor_full_paper_suite.sh` as a small CPU-only
Slurm job with the full job-ID list. It polls `squeue`/`sacct`, records state
to a Slurm output log, and exits nonzero if any job fails. From any login node
connected to this cluster, the same state is visible with:

```bash
squeue -u "$USER"
sacct -X -S today -u "$USER"
```

If the servers truly use separate Slurm controllers, run one monitor per
controller and push append-only status files to unique GitHub branches (or a
dedicated status repository). Do not have multiple jobs push directly to the
same `main` branch; concurrent pushes will race and can obscure failures.
