# V2R cluster inventory

2026-09-25T02:33:30.102320+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318969118720 available bytes; 82.21% used; 112480503 free inodes.

server1 `/home`: 318969118720 available bytes; 82.21% used; 112480503 free inodes.

server1 `/tmp`: 318969118720 available bytes; 82.21% used; 112480503 free inodes.

server1 `/var/tmp`: 318969118720 available bytes; 82.21% used; 112480503 free inodes.

server1 `/mnt/raid5`: 416205611008 available bytes; 98.09% used; 337605538 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23010390016 available bytes; 98.72% used; 110410437 free inodes.

server2 `/home`: 23010390016 available bytes; 98.72% used; 110410437 free inodes.

server2 `/tmp`: 23010390016 available bytes; 98.72% used; 110410437 free inodes.

server2 `/var/tmp`: 23010390016 available bytes; 98.72% used; 110410437 free inodes.

server2 `/mnt/raid5`: 482471280640 available bytes; 96.67% used; 445113623 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350898176 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84350898176 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145544126464 available bytes; 97.99% used; 225810984 free inodes.

server3 `/tmp`: 84350898176 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84350898176 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105895641088 available bytes; 94.09% used; 114350954 free inodes.

server4 `/home`: 105895641088 available bytes; 94.09% used; 114350954 free inodes.

server4 `/data`: 12774678528 available bytes; 99.82% used; 224969027 free inodes.

server4 `/tmp`: 105895641088 available bytes; 94.09% used; 114350954 free inodes.

server4 `/var/tmp`: 105895641088 available bytes; 94.09% used; 114350954 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
