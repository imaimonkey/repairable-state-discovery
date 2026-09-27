# V2R cluster inventory

2026-09-27T06:09:49.929708+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314498502656 available bytes; 82.46% used; 112440824 free inodes.

server1 `/home`: 314498502656 available bytes; 82.46% used; 112440824 free inodes.

server1 `/tmp`: 314498502656 available bytes; 82.46% used; 112440824 free inodes.

server1 `/var/tmp`: 314498502656 available bytes; 82.46% used; 112440824 free inodes.

server1 `/mnt/raid5`: 634708516864 available bytes; 97.09% used; 337400011 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17621123072 available bytes; 99.02% used; 110365004 free inodes.

server2 `/home`: 17621123072 available bytes; 99.02% used; 110365004 free inodes.

server2 `/tmp`: 17621123072 available bytes; 99.02% used; 110365004 free inodes.

server2 `/var/tmp`: 17621123072 available bytes; 99.02% used; 110365004 free inodes.

server2 `/mnt/raid5`: 573761650688 available bytes; 96.04% used; 444876756 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78576463872 available bytes; 95.62% used; 114062896 free inodes.

server3 `/home`: 78576463872 available bytes; 95.62% used; 114062896 free inodes.

server3 `/data`: 1333262225408 available bytes; 81.57% used; 225765715 free inodes.

server3 `/tmp`: 78576463872 available bytes; 95.62% used; 114062896 free inodes.

server3 `/var/tmp`: 78576463872 available bytes; 95.62% used; 114062896 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 110998675456 available bytes; 93.81% used; 114372891 free inodes.

server4 `/home`: 110998675456 available bytes; 93.81% used; 114372891 free inodes.

server4 `/data`: 374486745088 available bytes; 94.82% used; 224771189 free inodes.

server4 `/tmp`: 110998675456 available bytes; 93.81% used; 114372891 free inodes.

server4 `/var/tmp`: 110998675456 available bytes; 93.81% used; 114372891 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
