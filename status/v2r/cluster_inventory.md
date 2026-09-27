# V2R cluster inventory

2026-09-27T07:13:53.279345+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314478956544 available bytes; 82.46% used; 112440783 free inodes.

server1 `/home`: 314478956544 available bytes; 82.46% used; 112440783 free inodes.

server1 `/tmp`: 314478956544 available bytes; 82.46% used; 112440783 free inodes.

server1 `/var/tmp`: 314478956544 available bytes; 82.46% used; 112440783 free inodes.

server1 `/mnt/raid5`: 634662416384 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17609256960 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17609256960 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17609256960 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17609256960 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 571873390592 available bytes; 96.05% used; 444874814 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 78572814336 available bytes; 95.62% used; 114062889 free inodes.

server3 `/home`: 78572814336 available bytes; 95.62% used; 114062889 free inodes.

server3 `/data`: 1333159972864 available bytes; 81.58% used; 225764437 free inodes.

server3 `/tmp`: 78572814336 available bytes; 95.62% used; 114062889 free inodes.

server3 `/var/tmp`: 78572814336 available bytes; 95.62% used; 114062889 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111070932992 available bytes; 93.80% used; 114372892 free inodes.

server4 `/home`: 111070932992 available bytes; 93.80% used; 114372892 free inodes.

server4 `/data`: 374387793920 available bytes; 94.83% used; 224771194 free inodes.

server4 `/tmp`: 111070932992 available bytes; 93.80% used; 114372892 free inodes.

server4 `/var/tmp`: 111070932992 available bytes; 93.80% used; 114372892 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
