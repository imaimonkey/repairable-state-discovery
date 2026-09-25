# V2R cluster inventory

2026-09-25T07:03:04.706249+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872051712 available bytes; 82.21% used; 112480377 free inodes.

server1 `/home`: 318872051712 available bytes; 82.21% used; 112480377 free inodes.

server1 `/tmp`: 318872051712 available bytes; 82.21% used; 112480377 free inodes.

server1 `/var/tmp`: 318872051712 available bytes; 82.21% used; 112480377 free inodes.

server1 `/mnt/raid5`: 399694585856 available bytes; 98.17% used; 337560444 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22879145984 available bytes; 98.72% used; 110410548 free inodes.

server2 `/home`: 22879145984 available bytes; 98.72% used; 110410548 free inodes.

server2 `/tmp`: 22879145984 available bytes; 98.72% used; 110410548 free inodes.

server2 `/var/tmp`: 22879145984 available bytes; 98.72% used; 110410548 free inodes.

server2 `/mnt/raid5`: 330486669312 available bytes; 97.72% used; 445098049 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84447027200 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84447027200 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142456139776 available bytes; 98.03% used; 225813161 free inodes.

server3 `/tmp`: 84447027200 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84447027200 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638694912 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638694912 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249494958080 available bytes; 96.55% used; 225017040 free inodes.

server4 `/tmp`: 105638694912 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638694912 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
