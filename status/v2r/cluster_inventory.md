# V2R cluster inventory

2026-09-27T06:43:49.439442+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314496946176 available bytes; 82.46% used; 112440812 free inodes.

server1 `/home`: 314496946176 available bytes; 82.46% used; 112440812 free inodes.

server1 `/tmp`: 314496946176 available bytes; 82.46% used; 112440812 free inodes.

server1 `/var/tmp`: 314496946176 available bytes; 82.46% used; 112440812 free inodes.

server1 `/mnt/raid5`: 634672599040 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17611243520 available bytes; 99.02% used; 110365003 free inodes.

server2 `/home`: 17611243520 available bytes; 99.02% used; 110365003 free inodes.

server2 `/tmp`: 17611243520 available bytes; 99.02% used; 110365003 free inodes.

server2 `/var/tmp`: 17611243520 available bytes; 99.02% used; 110365003 free inodes.

server2 `/mnt/raid5`: 572712214528 available bytes; 96.04% used; 444875499 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 78582697984 available bytes; 95.61% used; 114062902 free inodes.

server3 `/home`: 78582697984 available bytes; 95.61% used; 114062902 free inodes.

server3 `/data`: 1333256069120 available bytes; 81.57% used; 225765138 free inodes.

server3 `/tmp`: 78582697984 available bytes; 95.61% used; 114062902 free inodes.

server3 `/var/tmp`: 78582697984 available bytes; 95.61% used; 114062902 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110997778432 available bytes; 93.81% used; 114372897 free inodes.

server4 `/home`: 110997778432 available bytes; 93.81% used; 114372897 free inodes.

server4 `/data`: 374448607232 available bytes; 94.82% used; 224771165 free inodes.

server4 `/tmp`: 110997778432 available bytes; 93.81% used; 114372897 free inodes.

server4 `/var/tmp`: 110997778432 available bytes; 93.81% used; 114372897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
