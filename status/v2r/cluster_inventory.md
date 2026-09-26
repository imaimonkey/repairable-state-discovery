# V2R cluster inventory

2026-09-26T18:08:42.391693+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315566153728 available bytes; 82.40% used; 112445741 free inodes.

server1 `/home`: 315566153728 available bytes; 82.40% used; 112445741 free inodes.

server1 `/tmp`: 315566153728 available bytes; 82.40% used; 112445741 free inodes.

server1 `/var/tmp`: 315566153728 available bytes; 82.40% used; 112445741 free inodes.

server1 `/mnt/raid5`: 645855477760 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18028994560 available bytes; 98.99% used; 110367616 free inodes.

server2 `/home`: 18028994560 available bytes; 98.99% used; 110367616 free inodes.

server2 `/tmp`: 18028994560 available bytes; 98.99% used; 110367616 free inodes.

server2 `/var/tmp`: 18028994560 available bytes; 98.99% used; 110367616 free inodes.

server2 `/mnt/raid5`: 604687478784 available bytes; 95.82% used; 444968326 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81272233984 available bytes; 95.46% used; 114065369 free inodes.

server3 `/home`: 81272233984 available bytes; 95.46% used; 114065369 free inodes.

server3 `/data`: 1349366423552 available bytes; 81.35% used; 225835272 free inodes.

server3 `/tmp`: 81272233984 available bytes; 95.46% used; 114065369 free inodes.

server3 `/var/tmp`: 81272233984 available bytes; 95.46% used; 114065369 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105939181568 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105939181568 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410372419584 available bytes; 94.33% used; 224824199 free inodes.

server4 `/tmp`: 105939181568 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105939181568 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
