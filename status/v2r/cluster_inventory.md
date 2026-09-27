# V2R cluster inventory

2026-09-27T07:21:54.079749+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314478329856 available bytes; 82.46% used; 112440786 free inodes.

server1 `/home`: 314478329856 available bytes; 82.46% used; 112440786 free inodes.

server1 `/tmp`: 314478329856 available bytes; 82.46% used; 112440786 free inodes.

server1 `/var/tmp`: 314478329856 available bytes; 82.46% used; 112440786 free inodes.

server1 `/mnt/raid5`: 634663100416 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17609707520 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17609707520 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17609707520 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17609707520 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 571621879808 available bytes; 96.05% used; 444874458 free inodes.
| server3 | True | ['2', '3'] | [] | reference_compatible=True |

server3 `/`: 78577950720 available bytes; 95.62% used; 114062890 free inodes.

server3 `/home`: 78577950720 available bytes; 95.62% used; 114062890 free inodes.

server3 `/data`: 1333141618688 available bytes; 81.58% used; 225764294 free inodes.

server3 `/tmp`: 78577950720 available bytes; 95.62% used; 114062890 free inodes.

server3 `/var/tmp`: 78577950720 available bytes; 95.62% used; 114062890 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111070720000 available bytes; 93.80% used; 114372889 free inodes.

server4 `/home`: 111070720000 available bytes; 93.80% used; 114372889 free inodes.

server4 `/data`: 374350823424 available bytes; 94.83% used; 224771152 free inodes.

server4 `/tmp`: 111070720000 available bytes; 93.80% used; 114372889 free inodes.

server4 `/var/tmp`: 111070720000 available bytes; 93.80% used; 114372889 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
