# V2R cluster inventory

2026-09-23T22:29:02.541792+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325704335360 available bytes; 81.83% used; 112501389 free inodes.

server1 `/home`: 325704335360 available bytes; 81.83% used; 112501389 free inodes.

server1 `/tmp`: 325704335360 available bytes; 81.83% used; 112501389 free inodes.

server1 `/var/tmp`: 325704335360 available bytes; 81.83% used; 112501389 free inodes.

server1 `/mnt/raid5`: 1388096417792 available bytes; 93.63% used; 337739842 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41082179584 available bytes; 97.71% used; 110432627 free inodes.

server2 `/home`: 41082179584 available bytes; 97.71% used; 110432627 free inodes.

server2 `/tmp`: 41082179584 available bytes; 97.71% used; 110432627 free inodes.

server2 `/var/tmp`: 41082179584 available bytes; 97.71% used; 110432627 free inodes.

server2 `/mnt/raid5`: 536727724032 available bytes; 96.29% used; 445206918 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293021523968 available bytes; 83.65% used; 114223226 free inodes.

server3 `/home`: 293021523968 available bytes; 83.65% used; 114223226 free inodes.

server3 `/data`: 82435133440 available bytes; 98.86% used; 225847389 free inodes.

server3 `/tmp`: 293021523968 available bytes; 83.65% used; 114223226 free inodes.

server3 `/var/tmp`: 293021523968 available bytes; 83.65% used; 114223226 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106384289792 available bytes; 94.06% used; 114354575 free inodes.

server4 `/home`: 106384289792 available bytes; 94.06% used; 114354575 free inodes.

server4 `/data`: 300077740032 available bytes; 95.85% used; 225437374 free inodes.

server4 `/tmp`: 106384289792 available bytes; 94.06% used; 114354575 free inodes.

server4 `/var/tmp`: 106384289792 available bytes; 94.06% used; 114354575 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
