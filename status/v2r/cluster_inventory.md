# V2R cluster inventory

2026-09-25T10:47:05.731038+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318982184960 available bytes; 82.21% used; 112479397 free inodes.

server1 `/home`: 318982184960 available bytes; 82.21% used; 112479397 free inodes.

server1 `/tmp`: 318982184960 available bytes; 82.21% used; 112479397 free inodes.

server1 `/var/tmp`: 318982184960 available bytes; 82.21% used; 112479397 free inodes.

server1 `/mnt/raid5`: 366748348416 available bytes; 98.32% used; 337555264 free inodes.
| server2 | True | ['1', '2', '3', '5', '6'] | [] |

server2 `/`: 22915334144 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22915334144 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22915334144 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22915334144 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 329479933952 available bytes; 97.72% used; 445089430 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84421398528 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84421398528 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142008631296 available bytes; 98.04% used; 225815443 free inodes.

server3 `/tmp`: 84421398528 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84421398528 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105612873728 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612873728 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238507020288 available bytes; 96.70% used; 224985575 free inodes.

server4 `/tmp`: 105612873728 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612873728 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
