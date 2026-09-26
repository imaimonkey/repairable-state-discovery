# V2R cluster inventory

2026-09-26T19:15:48.017967+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315552522240 available bytes; 82.40% used; 112445192 free inodes.

server1 `/home`: 315552522240 available bytes; 82.40% used; 112445192 free inodes.

server1 `/tmp`: 315552522240 available bytes; 82.40% used; 112445192 free inodes.

server1 `/var/tmp`: 315552522240 available bytes; 82.40% used; 112445192 free inodes.

server1 `/mnt/raid5`: 645855039488 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18029772800 available bytes; 98.99% used; 110367535 free inodes.

server2 `/home`: 18029772800 available bytes; 98.99% used; 110367535 free inodes.

server2 `/tmp`: 18029772800 available bytes; 98.99% used; 110367535 free inodes.

server2 `/var/tmp`: 18029772800 available bytes; 98.99% used; 110367535 free inodes.

server2 `/mnt/raid5`: 602780581888 available bytes; 95.83% used; 444966317 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81270939648 available bytes; 95.46% used; 114065303 free inodes.

server3 `/home`: 81270939648 available bytes; 95.46% used; 114065303 free inodes.

server3 `/data`: 1349036482560 available bytes; 81.36% used; 225834054 free inodes.

server3 `/tmp`: 81270939648 available bytes; 95.46% used; 114065303 free inodes.

server3 `/var/tmp`: 81270939648 available bytes; 95.46% used; 114065303 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105920778240 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105920778240 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410314981376 available bytes; 94.33% used; 224824167 free inodes.

server4 `/tmp`: 105920778240 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105920778240 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
