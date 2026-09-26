# V2R cluster inventory

2026-09-26T16:57:02.654410+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315638652928 available bytes; 82.39% used; 112446008 free inodes.

server1 `/home`: 315638652928 available bytes; 82.39% used; 112446008 free inodes.

server1 `/tmp`: 315638652928 available bytes; 82.39% used; 112446008 free inodes.

server1 `/var/tmp`: 315638652928 available bytes; 82.39% used; 112446008 free inodes.

server1 `/mnt/raid5`: 645892325376 available bytes; 97.04% used; 337469596 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18031857664 available bytes; 98.99% used; 110367561 free inodes.

server2 `/home`: 18031857664 available bytes; 98.99% used; 110367561 free inodes.

server2 `/tmp`: 18031857664 available bytes; 98.99% used; 110367561 free inodes.

server2 `/var/tmp`: 18031857664 available bytes; 98.99% used; 110367561 free inodes.

server2 `/mnt/raid5`: 606965297152 available bytes; 95.81% used; 444970407 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81276428288 available bytes; 95.46% used; 114065340 free inodes.

server3 `/home`: 81276428288 available bytes; 95.46% used; 114065340 free inodes.

server3 `/data`: 1349297491968 available bytes; 81.35% used; 225829312 free inodes.

server3 `/tmp`: 81276428288 available bytes; 95.46% used; 114065340 free inodes.

server3 `/var/tmp`: 81276428288 available bytes; 95.46% used; 114065340 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952956416 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105952956416 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410530299904 available bytes; 94.33% used; 224824521 free inodes.

server4 `/tmp`: 105952956416 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105952956416 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
