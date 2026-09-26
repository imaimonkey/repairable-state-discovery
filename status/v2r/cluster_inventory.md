# V2R cluster inventory

2026-09-26T17:25:44.458915+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315598454784 available bytes; 82.39% used; 112445896 free inodes.

server1 `/home`: 315598454784 available bytes; 82.39% used; 112445896 free inodes.

server1 `/tmp`: 315598454784 available bytes; 82.39% used; 112445896 free inodes.

server1 `/var/tmp`: 315598454784 available bytes; 82.39% used; 112445896 free inodes.

server1 `/mnt/raid5`: 645853319168 available bytes; 97.04% used; 337467118 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18023247872 available bytes; 98.99% used; 110367567 free inodes.

server2 `/home`: 18023247872 available bytes; 98.99% used; 110367567 free inodes.

server2 `/tmp`: 18023247872 available bytes; 98.99% used; 110367567 free inodes.

server2 `/var/tmp`: 18023247872 available bytes; 98.99% used; 110367567 free inodes.

server2 `/mnt/raid5`: 605681324032 available bytes; 95.81% used; 444969860 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81273741312 available bytes; 95.46% used; 114065401 free inodes.

server3 `/home`: 81273741312 available bytes; 95.46% used; 114065401 free inodes.

server3 `/data`: 1349218205696 available bytes; 81.35% used; 225836254 free inodes.

server3 `/tmp`: 81273741312 available bytes; 95.46% used; 114065401 free inodes.

server3 `/var/tmp`: 81273741312 available bytes; 95.46% used; 114065401 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105952223232 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105952223232 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410516578304 available bytes; 94.33% used; 224824485 free inodes.

server4 `/tmp`: 105952223232 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105952223232 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
