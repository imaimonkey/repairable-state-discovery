# V2R cluster inventory

2026-09-27T07:37:08.200713+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314472681472 available bytes; 82.46% used; 112440798 free inodes.

server1 `/home`: 314472681472 available bytes; 82.46% used; 112440798 free inodes.

server1 `/tmp`: 314472681472 available bytes; 82.46% used; 112440798 free inodes.

server1 `/var/tmp`: 314472681472 available bytes; 82.46% used; 112440798 free inodes.

server1 `/mnt/raid5`: 634658721792 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['0', '1'] | [] | reference_compatible=False |

server2 `/`: 17613717504 available bytes; 99.02% used; 110365012 free inodes.

server2 `/home`: 17613717504 available bytes; 99.02% used; 110365012 free inodes.

server2 `/tmp`: 17613717504 available bytes; 99.02% used; 110365012 free inodes.

server2 `/var/tmp`: 17613717504 available bytes; 99.02% used; 110365012 free inodes.

server2 `/mnt/raid5`: 570104909824 available bytes; 96.06% used; 444873895 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 78573031424 available bytes; 95.62% used; 114062878 free inodes.

server3 `/home`: 78573031424 available bytes; 95.62% used; 114062878 free inodes.

server3 `/data`: 1333023907840 available bytes; 81.58% used; 225764009 free inodes.

server3 `/tmp`: 78573031424 available bytes; 95.62% used; 114062878 free inodes.

server3 `/var/tmp`: 78573031424 available bytes; 95.62% used; 114062878 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111070334976 available bytes; 93.80% used; 114372886 free inodes.

server4 `/home`: 111070334976 available bytes; 93.80% used; 114372886 free inodes.

server4 `/data`: 374311956480 available bytes; 94.83% used; 224770985 free inodes.

server4 `/tmp`: 111070334976 available bytes; 93.80% used; 114372886 free inodes.

server4 `/var/tmp`: 111070334976 available bytes; 93.80% used; 114372886 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
