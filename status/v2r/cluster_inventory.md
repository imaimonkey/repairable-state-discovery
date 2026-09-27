# V2R cluster inventory

2026-09-27T05:11:53.777719+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314762620928 available bytes; 82.44% used; 112443004 free inodes.

server1 `/home`: 314762620928 available bytes; 82.44% used; 112443004 free inodes.

server1 `/tmp`: 314762620928 available bytes; 82.44% used; 112443004 free inodes.

server1 `/var/tmp`: 314762620928 available bytes; 82.44% used; 112443004 free inodes.

server1 `/mnt/raid5`: 634730037248 available bytes; 97.09% used; 337400248 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17631109120 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17631109120 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17631109120 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17631109120 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 575623766016 available bytes; 96.02% used; 444878215 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 78575693824 available bytes; 95.62% used; 114062919 free inodes.

server3 `/home`: 78575693824 available bytes; 95.62% used; 114062919 free inodes.

server3 `/data`: 1332937883648 available bytes; 81.58% used; 225758208 free inodes.

server3 `/tmp`: 78575693824 available bytes; 95.62% used; 114062919 free inodes.

server3 `/var/tmp`: 78575693824 available bytes; 95.62% used; 114062919 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111000190976 available bytes; 93.81% used; 114372914 free inodes.

server4 `/home`: 111000190976 available bytes; 93.81% used; 114372914 free inodes.

server4 `/data`: 382061158400 available bytes; 94.72% used; 224778177 free inodes.

server4 `/tmp`: 111000190976 available bytes; 93.81% used; 114372914 free inodes.

server4 `/var/tmp`: 111000190976 available bytes; 93.81% used; 114372914 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
