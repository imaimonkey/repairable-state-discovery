# Current Job Inventory

Snapshot: 2026-09-26 KST from Slurm scheduler plus existing V2R status/manifests. Slurm is authoritative for current state. No job was cancelled, held, released, requeued, or modified by this reconciliation.

## Current `kimhj` jobs

| Job ID | Name | State | Server | GPU/workdir | Command/config and SHA | Output | Purpose/progress | Decision |
|---:|---|---|---|---|---|---|---|---|
| 53067 | `v2r-ind-server1-math500-temporal-v2-008` | PENDING, requeued held | server1 | 1 x A6000; `/var/tmp/kimhj-v2r-reference/execution/gates-78fe5d7-s1` | `runtime/v2r_independent_worker.sbatch`; `V2R_EXECUTION_SHA=78fe5d7c1829b67d1bb1416b7205edfa647bb2fa`; shard 8 | `/var/tmp/kimhj-v2r-independent/server1/outputs/v2r_reference/deep/math500/temporal_replan_v2/.../slurm-53067.{out,err}` | independent reference replay gate; no completion yet | KEEP / reference-critical |
| 53069 | `v2r-ind-server1-math500-temporal-v2-010` | PENDING, requeued held | server1 | 1 x A6000; corresponding `gates-78fe5d7-s1` workdir | same worker/SHA; shard 10 | corresponding independent output/log path | independent reference replay gate | KEEP / reference-critical |
| 53070 | `v2r-ind-server1-math500-temporal-v2-011` | PENDING, user held | server1 | 1 x A6000; corresponding workdir | same worker/SHA; shard 11 | corresponding independent output/log path | independent reference replay gate | KEEP / reference-critical |
| 53071 | `v2r-ind-server1-math500-temporal-v2-012` | PENDING, user held | server1 | 1 x A6000; corresponding workdir | same worker/SHA; shard 12 | corresponding independent output/log path | independent reference replay gate | KEEP / reference-critical |
| 53072 | `v2r-ind-server1-math500-temporal-v2-013` | PENDING, user held | server1 | 1 x A6000; corresponding workdir | same worker/SHA; shard 13 | corresponding independent output/log path | independent reference replay gate | KEEP / reference-critical |
| 53073 | `v2r-ind-server1-math500-temporal-v2-014` | PENDING, user held | server1 | 1 x A6000; corresponding workdir | same worker/SHA; shard 14 | corresponding independent output/log path | independent reference replay gate | KEEP / reference-critical |
| 53074 | `v2r-ind-server1-math500-temporal-v2-015` | PENDING, user held | server1 | 1 x A6000; corresponding workdir | same worker/SHA; shard 15 | corresponding independent output/log path | independent reference replay gate | KEEP / reference-critical |
| 53262 | `v2full-gsm8k` | RUNNING | server3 | 1 GPU; `/data/kimhj/repairable-state-discovery-v2-exec-20260925` | `full_gsm8k_llada.yaml`; SHA `926495e78f9558ee2c0a606ef9f9f641cacb78da` | `logs/v2_measurement/v2full-gsm8k-53262.{out,err}`; V2 output `v2_gsm8k_llada` | model loaded; trajectory bank ready; final report absent at snapshot | UNKNOWN_NEEDS_FORENSIC / keep running |
| 53266 | `v2-v2_bbh_logical7_llada` | RUNNING | server3 | 1 GPU; same active workdir | `full_bbh_logical7_llada.yaml`; SHA `926495e…` | `logs/v2_measurement/v2-v2_bbh_logical7_llada-53266.{out,err}`; `v2_bbh_logical7_llada` | trajectory bank ready; final report absent | UNKNOWN_NEEDS_FORENSIC / keep running |
| 53267 | `v2-v2_mbpp_llada` | PENDING, QOSMaxGRESPerUser | server3 | 1 GPU; same active workdir | `full_mbpp_llada.yaml`; SHA `926495e…` | corresponding V2 measurement log/output path | queued measurement; no run progress | UNKNOWN_NEEDS_FORENSIC / do not cancel yet |
| 53268 | `v2-gate-dream` | PENDING, QOSMaxGRESPerUser | server3 | 1 GPU; same active workdir | `scripts/validate_v2_backends.py --backend dream`; SHA `926495e…` | corresponding V2 measurement log/output path | Dream readiness gate queued | UNKNOWN_NEEDS_FORENSIC / do not cancel yet |
| 53275 | `v2full-math500` | PENDING, QOSMaxGRESPerUser | server3 | 1 GPU; same active workdir | `full_math500_llada.yaml`; SHA `926495e…` | corresponding V2 measurement log/output path | queued 30-day measurement | UNKNOWN_NEEDS_FORENSIC / do not cancel yet |

The seven reference jobs are named with neutral `v2r` identifiers and map to the sealed reference execution SHA. The five V2 measurement jobs are not assumed scientifically valid until their manifests, backend gate, progress, and final reports are reconciled.

## Completed audit probes

Read-only Slurm probes used to inspect inaccessible nodes completed or were stopped after a resource wait: jobs `53537`–`53546` (server2/server4 filesystem, node, repository, GPU, and hash probes). They were infrastructure probes, not scientific jobs. The server2 GPU probe was force-terminated after waiting for unavailable capacity; no baseline user job was changed. These probe records should be retained in scheduler history as audit context.

## Existing monitor drift

`status/v2r/attention_required.md` listed the same 12 scheduler jobs as current but marked all 12 as monitor drift because the legacy monitor state did not mention them. This confirms that monitor state is not authoritative. The scheduler, job manifests, and output manifests must be reconciled before any KEEP/CANCEL decision.

## Historical jobs

Existing status records identify 49256, 49257, 50668, 50669, 52594, and 52595 as already cancelled/reallocated or reset for reference-primary work. This reconciliation does not repeat or alter those actions. Their records are historical operational evidence.
