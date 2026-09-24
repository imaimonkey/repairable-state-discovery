# V2R cluster inventory

2026-09-24T02:08:39.769817+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325447401472 available bytes; 81.84% used; 112499245 free inodes.

server1 `/home`: 325447401472 available bytes; 81.84% used; 112499245 free inodes.

server1 `/tmp`: 325447401472 available bytes; 81.84% used; 112499245 free inodes.

server1 `/var/tmp`: 325447401472 available bytes; 81.84% used; 112499245 free inodes.

server1 `/mnt/raid5`: 737966866432 available bytes; 96.61% used; 337733532 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40908726272 available bytes; 97.72% used; 110431690 free inodes.

server2 `/home`: 40908726272 available bytes; 97.72% used; 110431690 free inodes.

server2 `/tmp`: 40908726272 available bytes; 97.72% used; 110431690 free inodes.

server2 `/var/tmp`: 40908726272 available bytes; 97.72% used; 110431690 free inodes.

server2 `/mnt/raid5`: 529669373952 available bytes; 96.34% used; 445200190 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292685742080 available bytes; 83.67% used; 114210525 free inodes.

server3 `/home`: 292685742080 available bytes; 83.67% used; 114210525 free inodes.

server3 `/data`: 60185976832 available bytes; 99.17% used; 225841469 free inodes.

server3 `/tmp`: 292685742080 available bytes; 83.67% used; 114210525 free inodes.

server3 `/var/tmp`: 292685742080 available bytes; 83.67% used; 114210525 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105937920000 available bytes; 94.09% used; 114348445 free inodes.

server4 `/home`: 105937920000 available bytes; 94.09% used; 114348445 free inodes.

server4 `/data`: 289764847616 available bytes; 96.00% used; 225388467 free inodes.

server4 `/tmp`: 105937920000 available bytes; 94.09% used; 114348445 free inodes.

server4 `/var/tmp`: 105937920000 available bytes; 94.09% used; 114348445 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
