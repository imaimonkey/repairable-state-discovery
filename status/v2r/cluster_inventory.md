# V2R cluster inventory

2026-09-26T15:19:27.222550+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318154629120 available bytes; 82.25% used; 112473927 free inodes.

server1 `/home`: 318154629120 available bytes; 82.25% used; 112473927 free inodes.

server1 `/tmp`: 318154629120 available bytes; 82.25% used; 112473927 free inodes.

server1 `/var/tmp`: 318154629120 available bytes; 82.25% used; 112473927 free inodes.

server1 `/mnt/raid5`: 654128816128 available bytes; 97.00% used; 337531542 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 10977439744 available bytes; 99.39% used; 110367433 free inodes.

server2 `/home`: 10977439744 available bytes; 99.39% used; 110367433 free inodes.

server2 `/tmp`: 10977439744 available bytes; 99.39% used; 110367433 free inodes.

server2 `/var/tmp`: 10977439744 available bytes; 99.39% used; 110367433 free inodes.

server2 `/mnt/raid5`: 609723449344 available bytes; 95.79% used; 444973328 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82442932224 available bytes; 95.40% used; 114101906 free inodes.

server3 `/home`: 82442932224 available bytes; 95.40% used; 114101906 free inodes.

server3 `/data`: 1347192877056 available bytes; 81.38% used; 225809977 free inodes.

server3 `/tmp`: 82442932224 available bytes; 95.40% used; 114101906 free inodes.

server3 `/var/tmp`: 82442932224 available bytes; 95.40% used; 114101906 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954942976 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105954942976 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410804490240 available bytes; 94.32% used; 224826047 free inodes.

server4 `/tmp`: 105954942976 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105954942976 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
