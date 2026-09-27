# V2R cluster inventory

2026-09-27T08:01:30.138048+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314470248448 available bytes; 82.46% used; 112440804 free inodes.

server1 `/home`: 314470248448 available bytes; 82.46% used; 112440804 free inodes.

server1 `/tmp`: 314470248448 available bytes; 82.46% used; 112440804 free inodes.

server1 `/var/tmp`: 314470248448 available bytes; 82.46% used; 112440804 free inodes.

server1 `/mnt/raid5`: 634653904896 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17617174528 available bytes; 99.02% used; 110365014 free inodes.

server2 `/home`: 17617174528 available bytes; 99.02% used; 110365014 free inodes.

server2 `/tmp`: 17617174528 available bytes; 99.02% used; 110365014 free inodes.

server2 `/var/tmp`: 17617174528 available bytes; 99.02% used; 110365014 free inodes.

server2 `/mnt/raid5`: 570447732736 available bytes; 96.06% used; 444873296 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78573273088 available bytes; 95.62% used; 114062876 free inodes.

server3 `/home`: 78573273088 available bytes; 95.62% used; 114062876 free inodes.

server3 `/data`: 1332891774976 available bytes; 81.58% used; 225763754 free inodes.

server3 `/tmp`: 78573273088 available bytes; 95.62% used; 114062876 free inodes.

server3 `/var/tmp`: 78573273088 available bytes; 95.62% used; 114062876 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111069679616 available bytes; 93.80% used; 114372878 free inodes.

server4 `/home`: 111069679616 available bytes; 93.80% used; 114372878 free inodes.

server4 `/data`: 374264958976 available bytes; 94.83% used; 224770944 free inodes.

server4 `/tmp`: 111069679616 available bytes; 93.80% used; 114372878 free inodes.

server4 `/var/tmp`: 111069679616 available bytes; 93.80% used; 114372878 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
