# V2R cluster inventory

2026-09-25T01:01:04.489832+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319086891008 available bytes; 82.20% used; 112480777 free inodes.

server1 `/home`: 319086891008 available bytes; 82.20% used; 112480777 free inodes.

server1 `/tmp`: 319086891008 available bytes; 82.20% used; 112480777 free inodes.

server1 `/var/tmp`: 319086891008 available bytes; 82.20% used; 112480777 free inodes.

server1 `/mnt/raid5`: 416791904256 available bytes; 98.09% used; 337616347 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23067013120 available bytes; 98.71% used; 110410764 free inodes.

server2 `/home`: 23067013120 available bytes; 98.71% used; 110410764 free inodes.

server2 `/tmp`: 23067013120 available bytes; 98.71% used; 110410764 free inodes.

server2 `/var/tmp`: 23067013120 available bytes; 98.71% used; 110410764 free inodes.

server2 `/mnt/raid5`: 498388418560 available bytes; 96.56% used; 445162643 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84354859008 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84354859008 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148371308544 available bytes; 97.95% used; 225812859 free inodes.

server3 `/tmp`: 84354859008 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84354859008 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788125184 available bytes; 94.10% used; 114348302 free inodes.

server4 `/home`: 105788125184 available bytes; 94.10% used; 114348302 free inodes.

server4 `/data`: 55625773056 available bytes; 99.23% used; 225031190 free inodes.

server4 `/tmp`: 105788125184 available bytes; 94.10% used; 114348302 free inodes.

server4 `/var/tmp`: 105788125184 available bytes; 94.10% used; 114348302 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
