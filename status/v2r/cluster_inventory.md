# V2R cluster inventory

2026-09-26T20:59:28.361681+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315488382976 available bytes; 82.40% used; 112445678 free inodes.

server1 `/home`: 315488382976 available bytes; 82.40% used; 112445678 free inodes.

server1 `/tmp`: 315488382976 available bytes; 82.40% used; 112445678 free inodes.

server1 `/var/tmp`: 315488382976 available bytes; 82.40% used; 112445678 free inodes.

server1 `/mnt/raid5`: 645855031296 available bytes; 97.04% used; 337467123 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17940148224 available bytes; 99.00% used; 110367529 free inodes.

server2 `/home`: 17940148224 available bytes; 99.00% used; 110367529 free inodes.

server2 `/tmp`: 17940148224 available bytes; 99.00% used; 110367529 free inodes.

server2 `/var/tmp`: 17940148224 available bytes; 99.00% used; 110367529 free inodes.

server2 `/mnt/raid5`: 599571357696 available bytes; 95.86% used; 444963584 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81263407104 available bytes; 95.47% used; 114065293 free inodes.

server3 `/home`: 81263407104 available bytes; 95.47% used; 114065293 free inodes.

server3 `/data`: 1351236874240 available bytes; 81.33% used; 225832414 free inodes.

server3 `/tmp`: 81263407104 available bytes; 95.47% used; 114065293 free inodes.

server3 `/var/tmp`: 81263407104 available bytes; 95.47% used; 114065293 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918275584 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105918275584 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409924661248 available bytes; 94.33% used; 224823837 free inodes.

server4 `/tmp`: 105918275584 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105918275584 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
