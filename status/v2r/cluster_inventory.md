# V2R cluster inventory

2026-09-24T22:54:39.857902+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323925270528 available bytes; 81.93% used; 112481391 free inodes.

server1 `/home`: 323925270528 available bytes; 81.93% used; 112481391 free inodes.

server1 `/tmp`: 323925270528 available bytes; 81.93% used; 112481391 free inodes.

server1 `/var/tmp`: 323925270528 available bytes; 81.93% used; 112481391 free inodes.

server1 `/mnt/raid5`: 415308054528 available bytes; 98.09% used; 337617429 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23131729920 available bytes; 98.71% used; 110410913 free inodes.

server2 `/home`: 23131729920 available bytes; 98.71% used; 110410913 free inodes.

server2 `/tmp`: 23131729920 available bytes; 98.71% used; 110410913 free inodes.

server2 `/var/tmp`: 23131729920 available bytes; 98.71% used; 110410913 free inodes.

server2 `/mnt/raid5`: 467153784832 available bytes; 96.77% used; 445152552 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84370804736 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84370804736 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148868849664 available bytes; 97.94% used; 225801616 free inodes.

server3 `/tmp`: 84370804736 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84370804736 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105801035776 available bytes; 94.10% used; 114348320 free inodes.

server4 `/home`: 105801035776 available bytes; 94.10% used; 114348320 free inodes.

server4 `/data`: 62683156480 available bytes; 99.13% used; 225199028 free inodes.

server4 `/tmp`: 105801035776 available bytes; 94.10% used; 114348320 free inodes.

server4 `/var/tmp`: 105801035776 available bytes; 94.10% used; 114348320 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
