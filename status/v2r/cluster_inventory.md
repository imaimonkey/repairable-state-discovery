# V2R cluster inventory

2026-09-27T05:17:01.570378+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314755641344 available bytes; 82.44% used; 112443000 free inodes.

server1 `/home`: 314755641344 available bytes; 82.44% used; 112443000 free inodes.

server1 `/tmp`: 314755641344 available bytes; 82.44% used; 112443000 free inodes.

server1 `/var/tmp`: 314755641344 available bytes; 82.44% used; 112443000 free inodes.

server1 `/mnt/raid5`: 634728882176 available bytes; 97.09% used; 337400246 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17628704768 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17628704768 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17628704768 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17628704768 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 575494365184 available bytes; 96.02% used; 444878240 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78576799744 available bytes; 95.62% used; 114062915 free inodes.

server3 `/home`: 78576799744 available bytes; 95.62% used; 114062915 free inodes.

server3 `/data`: 1332928565248 available bytes; 81.58% used; 225758147 free inodes.

server3 `/tmp`: 78576799744 available bytes; 95.62% used; 114062915 free inodes.

server3 `/var/tmp`: 78576799744 available bytes; 95.62% used; 114062915 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111000023040 available bytes; 93.81% used; 114372910 free inodes.

server4 `/home`: 111000023040 available bytes; 93.81% used; 114372910 free inodes.

server4 `/data`: 381935026176 available bytes; 94.72% used; 224777359 free inodes.

server4 `/tmp`: 111000023040 available bytes; 93.81% used; 114372910 free inodes.

server4 `/var/tmp`: 111000023040 available bytes; 93.81% used; 114372910 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
