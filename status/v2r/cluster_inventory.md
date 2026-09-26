# V2R cluster inventory

2026-09-26T06:24:54.623131+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318770085888 available bytes; 82.22% used; 112476280 free inodes.

server1 `/home`: 318770085888 available bytes; 82.22% used; 112476280 free inodes.

server1 `/tmp`: 318770085888 available bytes; 82.22% used; 112476280 free inodes.

server1 `/var/tmp`: 318770085888 available bytes; 82.22% used; 112476280 free inodes.

server1 `/mnt/raid5`: 219691573248 available bytes; 98.99% used; 337539824 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22316027904 available bytes; 98.76% used; 110403845 free inodes.

server2 `/home`: 22316027904 available bytes; 98.76% used; 110403845 free inodes.

server2 `/tmp`: 22316027904 available bytes; 98.76% used; 110403845 free inodes.

server2 `/var/tmp`: 22316027904 available bytes; 98.76% used; 110403845 free inodes.

server2 `/mnt/raid5`: 273178836992 available bytes; 98.11% used; 445028777 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82565644288 available bytes; 95.39% used; 114110899 free inodes.

server3 `/home`: 82565644288 available bytes; 95.39% used; 114110899 free inodes.

server3 `/data`: 123999588352 available bytes; 98.29% used; 225822379 free inodes.

server3 `/tmp`: 82565644288 available bytes; 95.39% used; 114110899 free inodes.

server3 `/var/tmp`: 82565644288 available bytes; 95.39% used; 114110899 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105914331136 available bytes; 94.09% used; 114346888 free inodes.

server4 `/home`: 105914331136 available bytes; 94.09% used; 114346888 free inodes.

server4 `/data`: 106563284992 available bytes; 98.53% used; 224923519 free inodes.

server4 `/tmp`: 105914331136 available bytes; 94.09% used; 114346888 free inodes.

server4 `/var/tmp`: 105914331136 available bytes; 94.09% used; 114346888 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
