# V2R cluster inventory

2026-09-27T07:35:36.846111+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314468798464 available bytes; 82.46% used; 112440794 free inodes.

server1 `/home`: 314468798464 available bytes; 82.46% used; 112440794 free inodes.

server1 `/tmp`: 314468798464 available bytes; 82.46% used; 112440794 free inodes.

server1 `/var/tmp`: 314468798464 available bytes; 82.46% used; 112440794 free inodes.

server1 `/mnt/raid5`: 634659377152 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['0', '1'] | [] | reference_compatible=False |

server2 `/`: 17613905920 available bytes; 99.02% used; 110365012 free inodes.

server2 `/home`: 17613905920 available bytes; 99.02% used; 110365012 free inodes.

server2 `/tmp`: 17613905920 available bytes; 99.02% used; 110365012 free inodes.

server2 `/var/tmp`: 17613905920 available bytes; 99.02% used; 110365012 free inodes.

server2 `/mnt/raid5`: 571218612224 available bytes; 96.05% used; 444873943 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 78573133824 available bytes; 95.62% used; 114062882 free inodes.

server3 `/home`: 78573133824 available bytes; 95.62% used; 114062882 free inodes.

server3 `/data`: 1333021667328 available bytes; 81.58% used; 225764025 free inodes.

server3 `/tmp`: 78573133824 available bytes; 95.62% used; 114062882 free inodes.

server3 `/var/tmp`: 78573133824 available bytes; 95.62% used; 114062882 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111070363648 available bytes; 93.80% used; 114372886 free inodes.

server4 `/home`: 111070363648 available bytes; 93.80% used; 114372886 free inodes.

server4 `/data`: 374316961792 available bytes; 94.83% used; 224770993 free inodes.

server4 `/tmp`: 111070363648 available bytes; 93.80% used; 114372886 free inodes.

server4 `/var/tmp`: 111070363648 available bytes; 93.80% used; 114372886 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
