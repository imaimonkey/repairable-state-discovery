# V2R cluster inventory

2026-09-27T08:43:50.473857+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314469986304 available bytes; 82.46% used; 112440727 free inodes.

server1 `/home`: 314469986304 available bytes; 82.46% used; 112440727 free inodes.

server1 `/tmp`: 314469986304 available bytes; 82.46% used; 112440727 free inodes.

server1 `/var/tmp`: 314469986304 available bytes; 82.46% used; 112440727 free inodes.

server1 `/mnt/raid5`: 634583756800 available bytes; 97.09% used; 337400005 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 17601880064 available bytes; 99.02% used; 110364834 free inodes.

server2 `/home`: 17601880064 available bytes; 99.02% used; 110364834 free inodes.

server2 `/tmp`: 17601880064 available bytes; 99.02% used; 110364834 free inodes.

server2 `/var/tmp`: 17601880064 available bytes; 99.02% used; 110364834 free inodes.

server2 `/mnt/raid5`: 575677132800 available bytes; 96.02% used; 444749994 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78572470272 available bytes; 95.62% used; 114062867 free inodes.

server3 `/home`: 78572470272 available bytes; 95.62% used; 114062867 free inodes.

server3 `/data`: 1332615839744 available bytes; 81.58% used; 225763142 free inodes.

server3 `/tmp`: 78572470272 available bytes; 95.62% used; 114062867 free inodes.

server3 `/var/tmp`: 78572470272 available bytes; 95.62% used; 114062867 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111051808768 available bytes; 93.80% used; 114372882 free inodes.

server4 `/home`: 111051808768 available bytes; 93.80% used; 114372882 free inodes.

server4 `/data`: 366204018688 available bytes; 94.94% used; 224769867 free inodes.

server4 `/tmp`: 111051808768 available bytes; 93.80% used; 114372882 free inodes.

server4 `/var/tmp`: 111051808768 available bytes; 93.80% used; 114372882 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
