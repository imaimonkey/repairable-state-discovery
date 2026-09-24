# V2R cluster inventory

2026-09-24T05:32:09.394907+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324539551744 available bytes; 81.90% used; 112492338 free inodes.

server1 `/home`: 324539551744 available bytes; 81.90% used; 112492338 free inodes.

server1 `/tmp`: 324539551744 available bytes; 81.90% used; 112492338 free inodes.

server1 `/var/tmp`: 324539551744 available bytes; 81.90% used; 112492338 free inodes.

server1 `/mnt/raid5`: 517605842944 available bytes; 97.63% used; 337724021 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57917239296 available bytes; 96.77% used; 110431362 free inodes.

server2 `/home`: 57917239296 available bytes; 96.77% used; 110431362 free inodes.

server2 `/tmp`: 57917239296 available bytes; 96.77% used; 110431362 free inodes.

server2 `/var/tmp`: 57917239296 available bytes; 96.77% used; 110431362 free inodes.

server2 `/mnt/raid5`: 522302001152 available bytes; 96.39% used; 445193549 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127198679040 available bytes; 92.90% used; 114197413 free inodes.

server3 `/home`: 127198679040 available bytes; 92.90% used; 114197413 free inodes.

server3 `/data`: 185271410688 available bytes; 97.44% used; 225839537 free inodes.

server3 `/tmp`: 127198679040 available bytes; 92.90% used; 114197413 free inodes.

server3 `/var/tmp`: 127198679040 available bytes; 92.90% used; 114197413 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105816940544 available bytes; 94.10% used; 114349363 free inodes.

server4 `/home`: 105816940544 available bytes; 94.10% used; 114349363 free inodes.

server4 `/data`: 251527573504 available bytes; 96.52% used; 225358108 free inodes.

server4 `/tmp`: 105816940544 available bytes; 94.10% used; 114349363 free inodes.

server4 `/var/tmp`: 105816940544 available bytes; 94.10% used; 114349363 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
