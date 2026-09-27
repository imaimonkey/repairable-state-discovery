# V2R cluster inventory

2026-09-27T08:17:55.312962+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314469572608 available bytes; 82.46% used; 112440797 free inodes.

server1 `/home`: 314469572608 available bytes; 82.46% used; 112440797 free inodes.

server1 `/tmp`: 314469572608 available bytes; 82.46% used; 112440797 free inodes.

server1 `/var/tmp`: 314469572608 available bytes; 82.46% used; 112440797 free inodes.

server1 `/mnt/raid5`: 634646872064 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 17608814592 available bytes; 99.02% used; 110365012 free inodes.

server2 `/home`: 17608814592 available bytes; 99.02% used; 110365012 free inodes.

server2 `/tmp`: 17608814592 available bytes; 99.02% used; 110365012 free inodes.

server2 `/var/tmp`: 17608814592 available bytes; 99.02% used; 110365012 free inodes.

server2 `/mnt/raid5`: 578309509120 available bytes; 96.00% used; 444873357 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78571536384 available bytes; 95.62% used; 114062871 free inodes.

server3 `/home`: 78571536384 available bytes; 95.62% used; 114062871 free inodes.

server3 `/data`: 1332716421120 available bytes; 81.58% used; 225763509 free inodes.

server3 `/tmp`: 78571536384 available bytes; 95.62% used; 114062871 free inodes.

server3 `/var/tmp`: 78571536384 available bytes; 95.62% used; 114062871 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111052500992 available bytes; 93.80% used; 114372881 free inodes.

server4 `/home`: 111052500992 available bytes; 93.80% used; 114372881 free inodes.

server4 `/data`: 368336441344 available bytes; 94.91% used; 224770895 free inodes.

server4 `/tmp`: 111052500992 available bytes; 93.80% used; 114372881 free inodes.

server4 `/var/tmp`: 111052500992 available bytes; 93.80% used; 114372881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
