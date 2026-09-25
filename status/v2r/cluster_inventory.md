# V2R cluster inventory

2026-09-25T10:14:55.802366+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318834282496 available bytes; 82.21% used; 112480388 free inodes.

server1 `/home`: 318834282496 available bytes; 82.21% used; 112480388 free inodes.

server1 `/tmp`: 318834282496 available bytes; 82.21% used; 112480388 free inodes.

server1 `/var/tmp`: 318834282496 available bytes; 82.21% used; 112480388 free inodes.

server1 `/mnt/raid5`: 371893878784 available bytes; 98.29% used; 337556521 free inodes.
| server2 | True | ['3', '6'] | [] |

server2 `/`: 22835113984 available bytes; 98.73% used; 110410480 free inodes.

server2 `/home`: 22835113984 available bytes; 98.73% used; 110410480 free inodes.

server2 `/tmp`: 22835113984 available bytes; 98.73% used; 110410480 free inodes.

server2 `/var/tmp`: 22835113984 available bytes; 98.73% used; 110410480 free inodes.

server2 `/mnt/raid5`: 316077838336 available bytes; 97.82% used; 445090986 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84417392640 available bytes; 95.29% used; 114156045 free inodes.

server3 `/home`: 84417392640 available bytes; 95.29% used; 114156045 free inodes.

server3 `/data`: 142026940416 available bytes; 98.04% used; 225816140 free inodes.

server3 `/tmp`: 84417392640 available bytes; 95.29% used; 114156045 free inodes.

server3 `/var/tmp`: 84417392640 available bytes; 95.29% used; 114156045 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105613967360 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105613967360 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240066752512 available bytes; 96.68% used; 224989418 free inodes.

server4 `/tmp`: 105613967360 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105613967360 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
