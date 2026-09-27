# V2R cluster inventory

2026-09-27T07:33:42.465995+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314477514752 available bytes; 82.46% used; 112440791 free inodes.

server1 `/home`: 314477514752 available bytes; 82.46% used; 112440791 free inodes.

server1 `/tmp`: 314477514752 available bytes; 82.46% used; 112440791 free inodes.

server1 `/var/tmp`: 314477514752 available bytes; 82.46% used; 112440791 free inodes.

server1 `/mnt/raid5`: 634661232640 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['0', '1'] | [] |

server2 `/`: 17614209024 available bytes; 99.02% used; 110365012 free inodes.

server2 `/home`: 17614209024 available bytes; 99.02% used; 110365012 free inodes.

server2 `/tmp`: 17614209024 available bytes; 99.02% used; 110365012 free inodes.

server2 `/var/tmp`: 17614209024 available bytes; 99.02% used; 110365012 free inodes.

server2 `/mnt/raid5`: 571278745600 available bytes; 96.05% used; 444874132 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 78572498944 available bytes; 95.62% used; 114062876 free inodes.

server3 `/home`: 78572498944 available bytes; 95.62% used; 114062876 free inodes.

server3 `/data`: 1333024735232 available bytes; 81.58% used; 225764047 free inodes.

server3 `/tmp`: 78572498944 available bytes; 95.62% used; 114062876 free inodes.

server3 `/var/tmp`: 78572498944 available bytes; 95.62% used; 114062876 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111070416896 available bytes; 93.80% used; 114372886 free inodes.

server4 `/home`: 111070416896 available bytes; 93.80% used; 114372886 free inodes.

server4 `/data`: 374319525888 available bytes; 94.83% used; 224770993 free inodes.

server4 `/tmp`: 111070416896 available bytes; 93.80% used; 114372886 free inodes.

server4 `/var/tmp`: 111070416896 available bytes; 93.80% used; 114372886 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
