# V2R cluster inventory

2026-09-24T02:02:23.426280+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325447942144 available bytes; 81.84% used; 112499295 free inodes.

server1 `/home`: 325447942144 available bytes; 81.84% used; 112499295 free inodes.

server1 `/tmp`: 325447942144 available bytes; 81.84% used; 112499295 free inodes.

server1 `/var/tmp`: 325447942144 available bytes; 81.84% used; 112499295 free inodes.

server1 `/mnt/raid5`: 764534136832 available bytes; 96.49% used; 337733626 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40918769664 available bytes; 97.72% used; 110431738 free inodes.

server2 `/home`: 40918769664 available bytes; 97.72% used; 110431738 free inodes.

server2 `/tmp`: 40918769664 available bytes; 97.72% used; 110431738 free inodes.

server2 `/var/tmp`: 40918769664 available bytes; 97.72% used; 110431738 free inodes.

server2 `/mnt/raid5`: 529862307840 available bytes; 96.34% used; 445200371 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292710379520 available bytes; 83.67% used; 114211146 free inodes.

server3 `/home`: 292710379520 available bytes; 83.67% used; 114211146 free inodes.

server3 `/data`: 60357443584 available bytes; 99.17% used; 225841632 free inodes.

server3 `/tmp`: 292710379520 available bytes; 83.67% used; 114211146 free inodes.

server3 `/var/tmp`: 292710379520 available bytes; 83.67% used; 114211146 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105938231296 available bytes; 94.09% used; 114348463 free inodes.

server4 `/home`: 105938231296 available bytes; 94.09% used; 114348463 free inodes.

server4 `/data`: 289778204672 available bytes; 96.00% used; 225388486 free inodes.

server4 `/tmp`: 105938231296 available bytes; 94.09% used; 114348463 free inodes.

server4 `/var/tmp`: 105938231296 available bytes; 94.09% used; 114348463 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
