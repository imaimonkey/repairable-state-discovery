# V2R cluster inventory

2026-09-27T06:23:33.089734+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314497556480 available bytes; 82.46% used; 112440805 free inodes.

server1 `/home`: 314497556480 available bytes; 82.46% used; 112440805 free inodes.

server1 `/tmp`: 314497556480 available bytes; 82.46% used; 112440805 free inodes.

server1 `/var/tmp`: 314497556480 available bytes; 82.46% used; 112440805 free inodes.

server1 `/mnt/raid5`: 634691244032 available bytes; 97.09% used; 337400008 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17626750976 available bytes; 99.02% used; 110365006 free inodes.

server2 `/home`: 17626750976 available bytes; 99.02% used; 110365006 free inodes.

server2 `/tmp`: 17626750976 available bytes; 99.02% used; 110365006 free inodes.

server2 `/var/tmp`: 17626750976 available bytes; 99.02% used; 110365006 free inodes.

server2 `/mnt/raid5`: 573368963072 available bytes; 96.04% used; 444876250 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78580355072 available bytes; 95.61% used; 114062893 free inodes.

server3 `/home`: 78580355072 available bytes; 95.61% used; 114062893 free inodes.

server3 `/data`: 1333249523712 available bytes; 81.57% used; 225765252 free inodes.

server3 `/tmp`: 78580355072 available bytes; 95.61% used; 114062893 free inodes.

server3 `/var/tmp`: 78580355072 available bytes; 95.61% used; 114062893 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 110998282240 available bytes; 93.81% used; 114372889 free inodes.

server4 `/home`: 110998282240 available bytes; 93.81% used; 114372889 free inodes.

server4 `/data`: 374467837952 available bytes; 94.82% used; 224771143 free inodes.

server4 `/tmp`: 110998282240 available bytes; 93.81% used; 114372889 free inodes.

server4 `/var/tmp`: 110998282240 available bytes; 93.81% used; 114372889 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
