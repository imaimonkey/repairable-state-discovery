# V2R cluster inventory

2026-09-26T15:22:30.251507+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318158295040 available bytes; 82.25% used; 112473932 free inodes.

server1 `/home`: 318158295040 available bytes; 82.25% used; 112473932 free inodes.

server1 `/tmp`: 318158295040 available bytes; 82.25% used; 112473932 free inodes.

server1 `/var/tmp`: 318158295040 available bytes; 82.25% used; 112473932 free inodes.

server1 `/mnt/raid5`: 654124625920 available bytes; 97.00% used; 337531534 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18029133824 available bytes; 98.99% used; 110367500 free inodes.

server2 `/home`: 18029133824 available bytes; 98.99% used; 110367500 free inodes.

server2 `/tmp`: 18029133824 available bytes; 98.99% used; 110367500 free inodes.

server2 `/var/tmp`: 18029133824 available bytes; 98.99% used; 110367500 free inodes.

server2 `/mnt/raid5`: 609634586624 available bytes; 95.79% used; 444973128 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82442399744 available bytes; 95.40% used; 114101911 free inodes.

server3 `/home`: 82442399744 available bytes; 95.40% used; 114101911 free inodes.

server3 `/data`: 1347190820864 available bytes; 81.38% used; 225809932 free inodes.

server3 `/tmp`: 82442399744 available bytes; 95.40% used; 114101911 free inodes.

server3 `/var/tmp`: 82442399744 available bytes; 95.40% used; 114101911 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954869248 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105954869248 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410801156096 available bytes; 94.32% used; 224826028 free inodes.

server4 `/tmp`: 105954869248 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105954869248 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
