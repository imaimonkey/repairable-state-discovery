# V2R cluster inventory

2026-09-26T19:05:07.585935+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315556155392 available bytes; 82.40% used; 112445735 free inodes.

server1 `/home`: 315556155392 available bytes; 82.40% used; 112445735 free inodes.

server1 `/tmp`: 315556155392 available bytes; 82.40% used; 112445735 free inodes.

server1 `/var/tmp`: 315556155392 available bytes; 82.40% used; 112445735 free inodes.

server1 `/mnt/raid5`: 645855969280 available bytes; 97.04% used; 337467124 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18023796736 available bytes; 98.99% used; 110367604 free inodes.

server2 `/home`: 18023796736 available bytes; 98.99% used; 110367604 free inodes.

server2 `/tmp`: 18023796736 available bytes; 98.99% used; 110367604 free inodes.

server2 `/var/tmp`: 18023796736 available bytes; 98.99% used; 110367604 free inodes.

server2 `/mnt/raid5`: 603078832128 available bytes; 95.83% used; 444966740 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81273786368 available bytes; 95.46% used; 114065376 free inodes.

server3 `/home`: 81273786368 available bytes; 95.46% used; 114065376 free inodes.

server3 `/data`: 1349050613760 available bytes; 81.36% used; 225834200 free inodes.

server3 `/tmp`: 81273786368 available bytes; 95.46% used; 114065376 free inodes.

server3 `/var/tmp`: 81273786368 available bytes; 95.46% used; 114065376 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105921060864 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105921060864 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410323726336 available bytes; 94.33% used; 224824169 free inodes.

server4 `/tmp`: 105921060864 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105921060864 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
