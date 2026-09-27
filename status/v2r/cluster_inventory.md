# V2R cluster inventory

2026-09-27T06:51:26.109726+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314487369728 available bytes; 82.46% used; 112440812 free inodes.

server1 `/home`: 314487369728 available bytes; 82.46% used; 112440812 free inodes.

server1 `/tmp`: 314487369728 available bytes; 82.46% used; 112440812 free inodes.

server1 `/var/tmp`: 314487369728 available bytes; 82.46% used; 112440812 free inodes.

server1 `/mnt/raid5`: 634671308800 available bytes; 97.09% used; 337400010 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17610756096 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17610756096 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17610756096 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17610756096 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 572498886656 available bytes; 96.04% used; 444875166 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78586855424 available bytes; 95.61% used; 114062885 free inodes.

server3 `/home`: 78586855424 available bytes; 95.61% used; 114062885 free inodes.

server3 `/data`: 1333241266176 available bytes; 81.57% used; 225764879 free inodes.

server3 `/tmp`: 78586855424 available bytes; 95.61% used; 114062885 free inodes.

server3 `/var/tmp`: 78586855424 available bytes; 95.61% used; 114062885 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110980755456 available bytes; 93.81% used; 114372897 free inodes.

server4 `/home`: 110980755456 available bytes; 93.81% used; 114372897 free inodes.

server4 `/data`: 374440030208 available bytes; 94.83% used; 224771150 free inodes.

server4 `/tmp`: 110980755456 available bytes; 93.81% used; 114372897 free inodes.

server4 `/var/tmp`: 110980755456 available bytes; 93.81% used; 114372897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
