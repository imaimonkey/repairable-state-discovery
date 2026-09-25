# V2R cluster inventory

2026-09-25T02:05:44.841197+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319023427584 available bytes; 82.20% used; 112480576 free inodes.

server1 `/home`: 319023427584 available bytes; 82.20% used; 112480576 free inodes.

server1 `/tmp`: 319023427584 available bytes; 82.20% used; 112480576 free inodes.

server1 `/var/tmp`: 319023427584 available bytes; 82.20% used; 112480576 free inodes.

server1 `/mnt/raid5`: 416259485696 available bytes; 98.09% used; 337608778 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23025180672 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 23025180672 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 23025180672 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 23025180672 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 484166889472 available bytes; 96.65% used; 445114764 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352188416 available bytes; 95.29% used; 114156074 free inodes.

server3 `/home`: 84352188416 available bytes; 95.29% used; 114156074 free inodes.

server3 `/data`: 146014306304 available bytes; 97.98% used; 225811612 free inodes.

server3 `/tmp`: 84352188416 available bytes; 95.29% used; 114156074 free inodes.

server3 `/var/tmp`: 84352188416 available bytes; 95.29% used; 114156074 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105752567808 available bytes; 94.10% used; 114348244 free inodes.

server4 `/home`: 105752567808 available bytes; 94.10% used; 114348244 free inodes.

server4 `/data`: 48499175424 available bytes; 99.33% used; 225030318 free inodes.

server4 `/tmp`: 105752567808 available bytes; 94.10% used; 114348244 free inodes.

server4 `/var/tmp`: 105752567808 available bytes; 94.10% used; 114348244 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
