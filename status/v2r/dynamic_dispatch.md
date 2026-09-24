# ICLR 2027 V2R dynamic dispatch

Updated: `2026-09-24T05:14:56.548978+00:00`; next inventory interval: `90s`.

This is a read-only placement decision. It does not cancel, preempt, or delete jobs/artifacts.

| Server | Observed | Idle GPUs | Safe FS | Reference compatible | Eligible | Reasons |
|---|---:|---|---|---:|---:|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | False | False | exact_native_replay_failed |
| server2 | True | [] | [] | False | False | no_idle_gpu_candidate, no_safe_filesystem, exact_native_replay_failed;_safe_scratch_is_non_authoritative |
| server3 | True | ['1', '2'] | ['/tmp', '/var/tmp'] | True | True | READY |
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | False | False | exact_native_replay_failed;_reference_torch_2_1_2_is_sm120_incompatible |

**Next batch:** `PLACE_NEXT_PRIORITY_SHARD` — eligible servers: server3

Running reference jobs: `9`; pending/configuring: `90`.
