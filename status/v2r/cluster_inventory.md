# V2R cluster inventory

2026-09-26T19:03:36.145488+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315556720640 available bytes; 82.40% used; 112445735 free inodes.

server1 `/home`: 315556720640 available bytes; 82.40% used; 112445735 free inodes.

server1 `/tmp`: 315556720640 available bytes; 82.40% used; 112445735 free inodes.

server1 `/var/tmp`: 315556720640 available bytes; 82.40% used; 112445735 free inodes.

server1 `/mnt/raid5`: 645856333824 available bytes; 97.04% used; 337467124 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18022969344 available bytes; 98.99% used; 110367602 free inodes.

server2 `/home`: 18022969344 available bytes; 98.99% used; 110367602 free inodes.

server2 `/tmp`: 18022969344 available bytes; 98.99% used; 110367602 free inodes.

server2 `/var/tmp`: 18022969344 available bytes; 98.99% used; 110367602 free inodes.

server2 `/mnt/raid5`: 603121971200 available bytes; 95.83% used; 444966782 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81159094272 available bytes; 95.47% used; 114065375 free inodes.

server3 `/home`: 81159094272 available bytes; 95.47% used; 114065375 free inodes.

server3 `/data`: 1349132210176 available bytes; 81.35% used; 225834262 free inodes.

server3 `/tmp`: 81159094272 available bytes; 95.47% used; 114065375 free inodes.

server3 `/var/tmp`: 81159094272 available bytes; 95.47% used; 114065375 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105929478144 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105929478144 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410325389312 available bytes; 94.33% used; 224824169 free inodes.

server4 `/tmp`: 105929478144 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105929478144 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
