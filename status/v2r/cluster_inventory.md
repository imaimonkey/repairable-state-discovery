# V2R cluster inventory

2026-09-26T17:07:42.978115+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315633266688 available bytes; 82.39% used; 112445898 free inodes.

server1 `/home`: 315633266688 available bytes; 82.39% used; 112445898 free inodes.

server1 `/tmp`: 315633266688 available bytes; 82.39% used; 112445898 free inodes.

server1 `/var/tmp`: 315633266688 available bytes; 82.39% used; 112445898 free inodes.

server1 `/mnt/raid5`: 645878902784 available bytes; 97.04% used; 337469104 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18030534656 available bytes; 98.99% used; 110367560 free inodes.

server2 `/home`: 18030534656 available bytes; 98.99% used; 110367560 free inodes.

server2 `/tmp`: 18030534656 available bytes; 98.99% used; 110367560 free inodes.

server2 `/var/tmp`: 18030534656 available bytes; 98.99% used; 110367560 free inodes.

server2 `/mnt/raid5`: 606169440256 available bytes; 95.81% used; 444969961 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81275781120 available bytes; 95.46% used; 114065341 free inodes.

server3 `/home`: 81275781120 available bytes; 95.46% used; 114065341 free inodes.

server3 `/data`: 1349320200192 available bytes; 81.35% used; 225836682 free inodes.

server3 `/tmp`: 81275781120 available bytes; 95.46% used; 114065341 free inodes.

server3 `/var/tmp`: 81275781120 available bytes; 95.46% used; 114065341 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952657408 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105952657408 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410522017792 available bytes; 94.33% used; 224824507 free inodes.

server4 `/tmp`: 105952657408 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105952657408 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
