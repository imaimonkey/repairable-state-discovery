# V2R cluster inventory

2026-09-23T22:33:39.733877+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325696856064 available bytes; 81.83% used; 112501390 free inodes.

server1 `/home`: 325696856064 available bytes; 81.83% used; 112501390 free inodes.

server1 `/tmp`: 325696856064 available bytes; 81.83% used; 112501390 free inodes.

server1 `/var/tmp`: 325696856064 available bytes; 81.83% used; 112501390 free inodes.

server1 `/mnt/raid5`: 1388102914048 available bytes; 93.63% used; 337739830 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41082572800 available bytes; 97.71% used; 110432629 free inodes.

server2 `/home`: 41082572800 available bytes; 97.71% used; 110432629 free inodes.

server2 `/tmp`: 41082572800 available bytes; 97.71% used; 110432629 free inodes.

server2 `/var/tmp`: 41082572800 available bytes; 97.71% used; 110432629 free inodes.

server2 `/mnt/raid5`: 536545218560 available bytes; 96.29% used; 445206628 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293045788672 available bytes; 83.65% used; 114223456 free inodes.

server3 `/home`: 293045788672 available bytes; 83.65% used; 114223456 free inodes.

server3 `/data`: 82429235200 available bytes; 98.86% used; 225847275 free inodes.

server3 `/tmp`: 293045788672 available bytes; 83.65% used; 114223456 free inodes.

server3 `/var/tmp`: 293045788672 available bytes; 83.65% used; 114223456 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106365399040 available bytes; 94.06% used; 114354407 free inodes.

server4 `/home`: 106365399040 available bytes; 94.06% used; 114354407 free inodes.

server4 `/data`: 300064346112 available bytes; 95.85% used; 225436532 free inodes.

server4 `/tmp`: 106365399040 available bytes; 94.06% used; 114354407 free inodes.

server4 `/var/tmp`: 106365399040 available bytes; 94.06% used; 114354407 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
