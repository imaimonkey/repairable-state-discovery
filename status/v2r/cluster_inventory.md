# V2R cluster inventory

2026-09-26T17:16:51.818111+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315619631104 available bytes; 82.39% used; 112445845 free inodes.

server1 `/home`: 315619631104 available bytes; 82.39% used; 112445845 free inodes.

server1 `/tmp`: 315619631104 available bytes; 82.39% used; 112445845 free inodes.

server1 `/var/tmp`: 315619631104 available bytes; 82.39% used; 112445845 free inodes.

server1 `/mnt/raid5`: 645860548608 available bytes; 97.04% used; 337467958 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18024611840 available bytes; 98.99% used; 110367559 free inodes.

server2 `/home`: 18024611840 available bytes; 98.99% used; 110367559 free inodes.

server2 `/tmp`: 18024611840 available bytes; 98.99% used; 110367559 free inodes.

server2 `/var/tmp`: 18024611840 available bytes; 98.99% used; 110367559 free inodes.

server2 `/mnt/raid5`: 606444511232 available bytes; 95.81% used; 444969582 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81275240448 available bytes; 95.46% used; 114065340 free inodes.

server3 `/home`: 81275240448 available bytes; 95.46% used; 114065340 free inodes.

server3 `/data`: 1349226848256 available bytes; 81.35% used; 225836411 free inodes.

server3 `/tmp`: 81275240448 available bytes; 95.46% used; 114065340 free inodes.

server3 `/var/tmp`: 81275240448 available bytes; 95.46% used; 114065340 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952436224 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105952436224 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410518335488 available bytes; 94.33% used; 224824500 free inodes.

server4 `/tmp`: 105952436224 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105952436224 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
