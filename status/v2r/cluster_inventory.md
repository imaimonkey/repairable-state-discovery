# V2R cluster inventory

2026-09-27T05:57:38.125899+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314499588096 available bytes; 82.46% used; 112440827 free inodes.

server1 `/home`: 314499588096 available bytes; 82.46% used; 112440827 free inodes.

server1 `/tmp`: 314499588096 available bytes; 82.46% used; 112440827 free inodes.

server1 `/var/tmp`: 314499588096 available bytes; 82.46% used; 112440827 free inodes.

server1 `/mnt/raid5`: 634712838144 available bytes; 97.09% used; 337400013 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17626701824 available bytes; 99.02% used; 110365008 free inodes.

server2 `/home`: 17626701824 available bytes; 99.02% used; 110365008 free inodes.

server2 `/tmp`: 17626701824 available bytes; 99.02% used; 110365008 free inodes.

server2 `/var/tmp`: 17626701824 available bytes; 99.02% used; 110365008 free inodes.

server2 `/mnt/raid5`: 574116941824 available bytes; 96.03% used; 444876826 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78576324608 available bytes; 95.62% used; 114062902 free inodes.

server3 `/home`: 78576324608 available bytes; 95.62% used; 114062902 free inodes.

server3 `/data`: 1333298225152 available bytes; 81.57% used; 225765885 free inodes.

server3 `/tmp`: 78576324608 available bytes; 95.62% used; 114062902 free inodes.

server3 `/var/tmp`: 78576324608 available bytes; 95.62% used; 114062902 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 110998966272 available bytes; 93.81% used; 114372894 free inodes.

server4 `/home`: 110998966272 available bytes; 93.81% used; 114372894 free inodes.

server4 `/data`: 374528536576 available bytes; 94.82% used; 224771214 free inodes.

server4 `/tmp`: 110998966272 available bytes; 93.81% used; 114372894 free inodes.

server4 `/var/tmp`: 110998966272 available bytes; 93.81% used; 114372894 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
