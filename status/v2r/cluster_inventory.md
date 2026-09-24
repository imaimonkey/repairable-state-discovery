# V2R cluster inventory

2026-09-24T20:09:26.066420+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323989749760 available bytes; 81.93% used; 112481427 free inodes.

server1 `/home`: 323989749760 available bytes; 81.93% used; 112481427 free inodes.

server1 `/tmp`: 323989749760 available bytes; 81.93% used; 112481427 free inodes.

server1 `/var/tmp`: 323989749760 available bytes; 81.93% used; 112481427 free inodes.

server1 `/mnt/raid5`: 415537483776 available bytes; 98.09% used; 337627777 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30175608832 available bytes; 98.32% used; 110411376 free inodes.

server2 `/home`: 30175608832 available bytes; 98.32% used; 110411376 free inodes.

server2 `/tmp`: 30175608832 available bytes; 98.32% used; 110411376 free inodes.

server2 `/var/tmp`: 30175608832 available bytes; 98.32% used; 110411376 free inodes.

server2 `/mnt/raid5`: 493524238336 available bytes; 96.59% used; 445157460 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84399960064 available bytes; 95.29% used; 114156132 free inodes.

server3 `/home`: 84399960064 available bytes; 95.29% used; 114156132 free inodes.

server3 `/data`: 151769690112 available bytes; 97.90% used; 225798773 free inodes.

server3 `/tmp`: 84399960064 available bytes; 95.29% used; 114156132 free inodes.

server3 `/var/tmp`: 84399960064 available bytes; 95.29% used; 114156132 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105641308160 available bytes; 94.10% used; 114348411 free inodes.

server4 `/home`: 105641308160 available bytes; 94.10% used; 114348411 free inodes.

server4 `/data`: 89791639552 available bytes; 98.76% used; 225266160 free inodes.

server4 `/tmp`: 105641308160 available bytes; 94.10% used; 114348411 free inodes.

server4 `/var/tmp`: 105641308160 available bytes; 94.10% used; 114348411 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
