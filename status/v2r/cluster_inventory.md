# V2R cluster inventory

2026-09-26T00:25:41.717943+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318655062016 available bytes; 82.22% used; 112476280 free inodes.

server1 `/home`: 318655062016 available bytes; 82.22% used; 112476280 free inodes.

server1 `/tmp`: 318655062016 available bytes; 82.22% used; 112476280 free inodes.

server1 `/var/tmp`: 318655062016 available bytes; 82.22% used; 112476280 free inodes.

server1 `/mnt/raid5`: 359401816064 available bytes; 98.35% used; 337546908 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22947430400 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22947430400 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22947430400 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22947430400 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 295232745472 available bytes; 97.96% used; 445058029 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339273728 available bytes; 95.29% used; 114152441 free inodes.

server3 `/home`: 84339273728 available bytes; 95.29% used; 114152441 free inodes.

server3 `/data`: 124945674240 available bytes; 98.27% used; 225819133 free inodes.

server3 `/tmp`: 84339273728 available bytes; 95.29% used; 114152441 free inodes.

server3 `/var/tmp`: 84339273728 available bytes; 95.29% used; 114152441 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453309952 available bytes; 94.12% used; 114348372 free inodes.

server4 `/home`: 105453309952 available bytes; 94.12% used; 114348372 free inodes.

server4 `/data`: 177933967360 available bytes; 97.54% used; 224917524 free inodes.

server4 `/tmp`: 105453309952 available bytes; 94.12% used; 114348372 free inodes.

server4 `/var/tmp`: 105453309952 available bytes; 94.12% used; 114348372 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
