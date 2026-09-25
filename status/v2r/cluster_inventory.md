# V2R cluster inventory

2026-09-25T02:04:12.638156+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319024017408 available bytes; 82.20% used; 112480576 free inodes.

server1 `/home`: 319024017408 available bytes; 82.20% used; 112480576 free inodes.

server1 `/tmp`: 319024017408 available bytes; 82.20% used; 112480576 free inodes.

server1 `/var/tmp`: 319024017408 available bytes; 82.20% used; 112480576 free inodes.

server1 `/mnt/raid5`: 416263110656 available bytes; 98.09% used; 337608956 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23025750016 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 23025750016 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 23025750016 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 23025750016 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 484195684352 available bytes; 96.65% used; 445114485 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352425984 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84352425984 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 146039484416 available bytes; 97.98% used; 225811647 free inodes.

server3 `/tmp`: 84352425984 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84352425984 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761030144 available bytes; 94.10% used; 114348250 free inodes.

server4 `/home`: 105761030144 available bytes; 94.10% used; 114348250 free inodes.

server4 `/data`: 48495403008 available bytes; 99.33% used; 225030318 free inodes.

server4 `/tmp`: 105761030144 available bytes; 94.10% used; 114348250 free inodes.

server4 `/var/tmp`: 105761030144 available bytes; 94.10% used; 114348250 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
