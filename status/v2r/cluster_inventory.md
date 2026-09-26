# V2R cluster inventory

2026-09-26T20:53:22.350870+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315482591232 available bytes; 82.40% used; 112444685 free inodes.

server1 `/home`: 315482591232 available bytes; 82.40% used; 112444685 free inodes.

server1 `/tmp`: 315482591232 available bytes; 82.40% used; 112444685 free inodes.

server1 `/var/tmp`: 315482591232 available bytes; 82.40% used; 112444685 free inodes.

server1 `/mnt/raid5`: 645854806016 available bytes; 97.04% used; 337467121 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17974558720 available bytes; 99.00% used; 110367105 free inodes.

server2 `/home`: 17974558720 available bytes; 99.00% used; 110367105 free inodes.

server2 `/tmp`: 17974558720 available bytes; 99.00% used; 110367105 free inodes.

server2 `/var/tmp`: 17974558720 available bytes; 99.00% used; 110367105 free inodes.

server2 `/mnt/raid5`: 600031596544 available bytes; 95.85% used; 444964021 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81262379008 available bytes; 95.47% used; 114065289 free inodes.

server3 `/home`: 81262379008 available bytes; 95.47% used; 114065289 free inodes.

server3 `/data`: 1348593582080 available bytes; 81.36% used; 225831033 free inodes.

server3 `/tmp`: 81262379008 available bytes; 95.47% used; 114065289 free inodes.

server3 `/var/tmp`: 81262379008 available bytes; 95.47% used; 114065289 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918455808 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105918455808 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409966776320 available bytes; 94.33% used; 224823708 free inodes.

server4 `/tmp`: 105918455808 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105918455808 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
