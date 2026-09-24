# V2R cluster inventory

2026-09-24T01:57:41.782347+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325448265728 available bytes; 81.84% used; 112499324 free inodes.

server1 `/home`: 325448265728 available bytes; 81.84% used; 112499324 free inodes.

server1 `/tmp`: 325448265728 available bytes; 81.84% used; 112499324 free inodes.

server1 `/var/tmp`: 325448265728 available bytes; 81.84% used; 112499324 free inodes.

server1 `/mnt/raid5`: 783965904896 available bytes; 96.40% used; 337733666 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40922173440 available bytes; 97.72% used; 110431785 free inodes.

server2 `/home`: 40922173440 available bytes; 97.72% used; 110431785 free inodes.

server2 `/tmp`: 40922173440 available bytes; 97.72% used; 110431785 free inodes.

server2 `/var/tmp`: 40922173440 available bytes; 97.72% used; 110431785 free inodes.

server2 `/mnt/raid5`: 530034724864 available bytes; 96.34% used; 445200750 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292719833088 available bytes; 83.67% used; 114211080 free inodes.

server3 `/home`: 292719833088 available bytes; 83.67% used; 114211080 free inodes.

server3 `/data`: 60366454784 available bytes; 99.17% used; 225841729 free inodes.

server3 `/tmp`: 292719833088 available bytes; 83.67% used; 114211080 free inodes.

server3 `/var/tmp`: 292719833088 available bytes; 83.67% used; 114211080 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105938518016 available bytes; 94.09% used; 114348472 free inodes.

server4 `/home`: 105938518016 available bytes; 94.09% used; 114348472 free inodes.

server4 `/data`: 289772343296 available bytes; 96.00% used; 225388490 free inodes.

server4 `/tmp`: 105938518016 available bytes; 94.09% used; 114348472 free inodes.

server4 `/var/tmp`: 105938518016 available bytes; 94.09% used; 114348472 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
