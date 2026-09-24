# V2R cluster inventory

2026-09-24T21:00:26.903888+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323981066240 available bytes; 81.93% used; 112481437 free inodes.

server1 `/home`: 323981066240 available bytes; 81.93% used; 112481437 free inodes.

server1 `/tmp`: 323981066240 available bytes; 81.93% used; 112481437 free inodes.

server1 `/var/tmp`: 323981066240 available bytes; 81.93% used; 112481437 free inodes.

server1 `/mnt/raid5`: 415555371008 available bytes; 98.09% used; 337630913 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30142791680 available bytes; 98.32% used; 110411380 free inodes.

server2 `/home`: 30142791680 available bytes; 98.32% used; 110411380 free inodes.

server2 `/tmp`: 30142791680 available bytes; 98.32% used; 110411380 free inodes.

server2 `/var/tmp`: 30142791680 available bytes; 98.32% used; 110411380 free inodes.

server2 `/mnt/raid5`: 491323674624 available bytes; 96.61% used; 445155867 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84386336768 available bytes; 95.29% used; 114156103 free inodes.

server3 `/home`: 84386336768 available bytes; 95.29% used; 114156103 free inodes.

server3 `/data`: 150876057600 available bytes; 97.91% used; 225803749 free inodes.

server3 `/tmp`: 84386336768 available bytes; 95.29% used; 114156103 free inodes.

server3 `/var/tmp`: 84386336768 available bytes; 95.29% used; 114156103 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638977536 available bytes; 94.10% used; 114348371 free inodes.

server4 `/home`: 105638977536 available bytes; 94.10% used; 114348371 free inodes.

server4 `/data`: 76393820160 available bytes; 98.94% used; 225255219 free inodes.

server4 `/tmp`: 105638977536 available bytes; 94.10% used; 114348371 free inodes.

server4 `/var/tmp`: 105638977536 available bytes; 94.10% used; 114348371 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
