# ICLR 2027 V2R dynamic dispatch

Updated: `2026-09-26T16:26:34.378052+00:00`; next inventory interval: `90s`.

This is a read-only placement decision. It does not cancel, preempt, or delete jobs/artifacts.

| Server | Observed | Idle GPUs | Safe FS | Reference compatible | Eligible | Reasons |
|---|---:|---|---|---:|---:|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | False | False | exact_native_replay_failed |
| server2 | True | ['2', '7'] | [] | False | False | no_safe_filesystem, exact_native_replay_failed;_safe_scratch_is_non_authoritative |
| server3 | True | [] | [] | True | False | no_idle_gpu_candidate, no_safe_filesystem |
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | False | False | exact_native_replay_failed;_reference_torch_2_1_2_is_sm120_incompatible |

**Next batch:** `NO_REFERENCE_SHARD_PENDING` — No pending reference shard was observed.

Running reference jobs: `0`; pending/configuring: `0`.
