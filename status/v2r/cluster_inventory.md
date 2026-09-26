# V2R cluster inventory

2026-09-26T18:52:55.730339+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315556859904 available bytes; 82.40% used; 112445746 free inodes.

server1 `/home`: 315556859904 available bytes; 82.40% used; 112445746 free inodes.

server1 `/tmp`: 315556859904 available bytes; 82.40% used; 112445746 free inodes.

server1 `/var/tmp`: 315556859904 available bytes; 82.40% used; 112445746 free inodes.

server1 `/mnt/raid5`: 645854990336 available bytes; 97.04% used; 337467122 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18032177152 available bytes; 98.99% used; 110367622 free inodes.

server2 `/home`: 18032177152 available bytes; 98.99% used; 110367622 free inodes.

server2 `/tmp`: 18032177152 available bytes; 98.99% used; 110367622 free inodes.

server2 `/var/tmp`: 18032177152 available bytes; 98.99% used; 110367622 free inodes.

server2 `/mnt/raid5`: 603428442112 available bytes; 95.83% used; 444966906 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81275723776 available bytes; 95.46% used; 114065393 free inodes.

server3 `/home`: 81275723776 available bytes; 95.46% used; 114065393 free inodes.

server3 `/data`: 1349145788416 available bytes; 81.35% used; 225834433 free inodes.

server3 `/tmp`: 81275723776 available bytes; 95.46% used; 114065393 free inodes.

server3 `/var/tmp`: 81275723776 available bytes; 95.46% used; 114065393 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105938124800 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105938124800 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410336047104 available bytes; 94.33% used; 224824177 free inodes.

server4 `/tmp`: 105938124800 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105938124800 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
