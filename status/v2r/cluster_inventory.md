# V2R cluster inventory

2026-09-27T08:41:06.702955+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314469179392 available bytes; 82.46% used; 112440730 free inodes.

server1 `/home`: 314469179392 available bytes; 82.46% used; 112440730 free inodes.

server1 `/tmp`: 314469179392 available bytes; 82.46% used; 112440730 free inodes.

server1 `/var/tmp`: 314469179392 available bytes; 82.46% used; 112440730 free inodes.

server1 `/mnt/raid5`: 634584629248 available bytes; 97.09% used; 337400005 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17602379776 available bytes; 99.02% used; 110364834 free inodes.

server2 `/home`: 17602379776 available bytes; 99.02% used; 110364834 free inodes.

server2 `/tmp`: 17602379776 available bytes; 99.02% used; 110364834 free inodes.

server2 `/var/tmp`: 17602379776 available bytes; 99.02% used; 110364834 free inodes.

server2 `/mnt/raid5`: 575223652352 available bytes; 96.03% used; 444751231 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78571929600 available bytes; 95.62% used; 114062865 free inodes.

server3 `/home`: 78571929600 available bytes; 95.62% used; 114062865 free inodes.

server3 `/data`: 1332619886592 available bytes; 81.58% used; 225763186 free inodes.

server3 `/tmp`: 78571929600 available bytes; 95.62% used; 114062865 free inodes.

server3 `/var/tmp`: 78571929600 available bytes; 95.62% used; 114062865 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111051870208 available bytes; 93.80% used; 114372882 free inodes.

server4 `/home`: 111051870208 available bytes; 93.80% used; 114372882 free inodes.

server4 `/data`: 366208548864 available bytes; 94.94% used; 224770055 free inodes.

server4 `/tmp`: 111051870208 available bytes; 93.80% used; 114372882 free inodes.

server4 `/var/tmp`: 111051870208 available bytes; 93.80% used; 114372882 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
