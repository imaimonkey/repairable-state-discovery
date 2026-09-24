# V2R cluster inventory

2026-09-24T21:01:59.275665+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/home`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/tmp`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/var/tmp`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/mnt/raid5`: 415557050368 available bytes; 98.09% used; 337630737 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30142246912 available bytes; 98.32% used; 110411380 free inodes.

server2 `/home`: 30142246912 available bytes; 98.32% used; 110411380 free inodes.

server2 `/tmp`: 30142246912 available bytes; 98.32% used; 110411380 free inodes.

server2 `/var/tmp`: 30142246912 available bytes; 98.32% used; 110411380 free inodes.

server2 `/mnt/raid5`: 491279110144 available bytes; 96.61% used; 445156214 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84386889728 available bytes; 95.29% used; 114156095 free inodes.

server3 `/home`: 84386889728 available bytes; 95.29% used; 114156095 free inodes.

server3 `/data`: 150854225920 available bytes; 97.92% used; 225803728 free inodes.

server3 `/tmp`: 84386889728 available bytes; 95.29% used; 114156095 free inodes.

server3 `/var/tmp`: 84386889728 available bytes; 95.29% used; 114156095 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638846464 available bytes; 94.10% used; 114348366 free inodes.

server4 `/home`: 105638846464 available bytes; 94.10% used; 114348366 free inodes.

server4 `/data`: 75756548096 available bytes; 98.95% used; 225255087 free inodes.

server4 `/tmp`: 105638846464 available bytes; 94.10% used; 114348366 free inodes.

server4 `/var/tmp`: 105638846464 available bytes; 94.10% used; 114348366 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
