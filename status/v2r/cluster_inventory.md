# V2R cluster inventory

2026-09-24T21:45:23.469635+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323949289472 available bytes; 81.93% used; 112481413 free inodes.

server1 `/home`: 323949289472 available bytes; 81.93% used; 112481413 free inodes.

server1 `/tmp`: 323949289472 available bytes; 81.93% used; 112481413 free inodes.

server1 `/var/tmp`: 323949289472 available bytes; 81.93% used; 112481413 free inodes.

server1 `/mnt/raid5`: 415465799680 available bytes; 98.09% used; 337625660 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30129643520 available bytes; 98.32% used; 110411302 free inodes.

server2 `/home`: 30129643520 available bytes; 98.32% used; 110411302 free inodes.

server2 `/tmp`: 30129643520 available bytes; 98.32% used; 110411302 free inodes.

server2 `/var/tmp`: 30129643520 available bytes; 98.32% used; 110411302 free inodes.

server2 `/mnt/raid5`: 489941819392 available bytes; 96.61% used; 445154647 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380442624 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84380442624 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 150045212672 available bytes; 97.93% used; 225802915 free inodes.

server3 `/tmp`: 84380442624 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84380442624 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105311514624 available bytes; 94.12% used; 114320539 free inodes.

server4 `/home`: 105311514624 available bytes; 94.12% used; 114320539 free inodes.

server4 `/data`: 80502718464 available bytes; 98.89% used; 225243872 free inodes.

server4 `/tmp`: 105311514624 available bytes; 94.12% used; 114320539 free inodes.

server4 `/var/tmp`: 105311514624 available bytes; 94.12% used; 114320539 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
