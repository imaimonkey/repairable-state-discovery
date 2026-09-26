# V2R cluster inventory

2026-09-26T23:39:31.971240+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315455770624 available bytes; 82.40% used; 112445625 free inodes.

server1 `/home`: 315455770624 available bytes; 82.40% used; 112445625 free inodes.

server1 `/tmp`: 315455770624 available bytes; 82.40% used; 112445625 free inodes.

server1 `/var/tmp`: 315455770624 available bytes; 82.40% used; 112445625 free inodes.

server1 `/mnt/raid5`: 645841399808 available bytes; 97.04% used; 337467028 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17939197952 available bytes; 99.00% used; 110367450 free inodes.

server2 `/home`: 17939197952 available bytes; 99.00% used; 110367450 free inodes.

server2 `/tmp`: 17939197952 available bytes; 99.00% used; 110367450 free inodes.

server2 `/var/tmp`: 17939197952 available bytes; 99.00% used; 110367450 free inodes.

server2 `/mnt/raid5`: 594793787392 available bytes; 95.89% used; 444958902 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 81080672256 available bytes; 95.48% used; 114069881 free inodes.

server3 `/home`: 81080672256 available bytes; 95.48% used; 114069881 free inodes.

server3 `/data`: 1349227843584 available bytes; 81.35% used; 225826305 free inodes.

server3 `/tmp`: 81080672256 available bytes; 95.48% used; 114069881 free inodes.

server3 `/var/tmp`: 81080672256 available bytes; 95.48% used; 114069881 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105880682496 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105880682496 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409592451072 available bytes; 94.34% used; 224823790 free inodes.

server4 `/tmp`: 105880682496 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105880682496 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
