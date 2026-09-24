# V2R cluster inventory

2026-09-24T22:51:32.409913+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323932237824 available bytes; 81.93% used; 112481413 free inodes.

server1 `/home`: 323932237824 available bytes; 81.93% used; 112481413 free inodes.

server1 `/tmp`: 323932237824 available bytes; 81.93% used; 112481413 free inodes.

server1 `/var/tmp`: 323932237824 available bytes; 81.93% used; 112481413 free inodes.

server1 `/mnt/raid5`: 415327281152 available bytes; 98.09% used; 337617800 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23152726016 available bytes; 98.71% used; 110410908 free inodes.

server2 `/home`: 23152726016 available bytes; 98.71% used; 110410908 free inodes.

server2 `/tmp`: 23152726016 available bytes; 98.71% used; 110410908 free inodes.

server2 `/var/tmp`: 23152726016 available bytes; 98.71% used; 110410908 free inodes.

server2 `/mnt/raid5`: 487883595776 available bytes; 96.63% used; 445152493 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84371341312 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84371341312 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148924887040 available bytes; 97.94% used; 225801675 free inodes.

server3 `/tmp`: 84371341312 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84371341312 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105801093120 available bytes; 94.10% used; 114348320 free inodes.

server4 `/home`: 105801093120 available bytes; 94.10% used; 114348320 free inodes.

server4 `/data`: 62726402048 available bytes; 99.13% used; 225202662 free inodes.

server4 `/tmp`: 105801093120 available bytes; 94.10% used; 114348320 free inodes.

server4 `/var/tmp`: 105801093120 available bytes; 94.10% used; 114348320 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
