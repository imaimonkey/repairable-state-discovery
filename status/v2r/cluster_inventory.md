# V2R cluster inventory

2026-09-24T22:53:04.573764+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323928920064 available bytes; 81.93% used; 112481413 free inodes.

server1 `/home`: 323928920064 available bytes; 81.93% used; 112481413 free inodes.

server1 `/tmp`: 323928920064 available bytes; 81.93% used; 112481413 free inodes.

server1 `/var/tmp`: 323928920064 available bytes; 81.93% used; 112481413 free inodes.

server1 `/mnt/raid5`: 415310196736 available bytes; 98.09% used; 337617611 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23151419392 available bytes; 98.71% used; 110410908 free inodes.

server2 `/home`: 23151419392 available bytes; 98.71% used; 110410908 free inodes.

server2 `/tmp`: 23151419392 available bytes; 98.71% used; 110410908 free inodes.

server2 `/var/tmp`: 23151419392 available bytes; 98.71% used; 110410908 free inodes.

server2 `/mnt/raid5`: 484573224960 available bytes; 96.65% used; 445152708 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84371267584 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84371267584 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148900163584 available bytes; 97.94% used; 225801642 free inodes.

server3 `/tmp`: 84371267584 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84371267584 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105801064448 available bytes; 94.10% used; 114348320 free inodes.

server4 `/home`: 105801064448 available bytes; 94.10% used; 114348320 free inodes.

server4 `/data`: 62706692096 available bytes; 99.13% used; 225200838 free inodes.

server4 `/tmp`: 105801064448 available bytes; 94.10% used; 114348320 free inodes.

server4 `/var/tmp`: 105801064448 available bytes; 94.10% used; 114348320 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
