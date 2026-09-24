# V2R cluster inventory

2026-09-24T04:29:34.870551+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324697743360 available bytes; 81.89% used; 112493178 free inodes.

server1 `/home`: 324697743360 available bytes; 81.89% used; 112493178 free inodes.

server1 `/tmp`: 324697743360 available bytes; 81.89% used; 112493178 free inodes.

server1 `/var/tmp`: 324697743360 available bytes; 81.89% used; 112493178 free inodes.

server1 `/mnt/raid5`: 445657899008 available bytes; 97.96% used; 337724689 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40783339520 available bytes; 97.72% used; 110430550 free inodes.

server2 `/home`: 40783339520 available bytes; 97.72% used; 110430550 free inodes.

server2 `/tmp`: 40783339520 available bytes; 97.72% used; 110430550 free inodes.

server2 `/var/tmp`: 40783339520 available bytes; 97.72% used; 110430550 free inodes.

server2 `/mnt/raid5`: 524878356480 available bytes; 96.37% used; 445196225 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292001640448 available bytes; 83.71% used; 114176140 free inodes.

server3 `/home`: 292001640448 available bytes; 83.71% used; 114176140 free inodes.

server3 `/data`: 27534262272 available bytes; 99.62% used; 225840981 free inodes.

server3 `/tmp`: 292001640448 available bytes; 83.71% used; 114176140 free inodes.

server3 `/var/tmp`: 292001640448 available bytes; 83.71% used; 114176140 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105844547584 available bytes; 94.09% used; 114349421 free inodes.

server4 `/home`: 105844547584 available bytes; 94.09% used; 114349421 free inodes.

server4 `/data`: 253409349632 available bytes; 96.50% used; 225366921 free inodes.

server4 `/tmp`: 105844547584 available bytes; 94.09% used; 114349421 free inodes.

server4 `/var/tmp`: 105844547584 available bytes; 94.09% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
