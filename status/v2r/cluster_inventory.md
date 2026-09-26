# V2R cluster inventory

2026-09-26T19:12:45.046836+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315553099776 available bytes; 82.40% used; 112445259 free inodes.

server1 `/home`: 315553099776 available bytes; 82.40% used; 112445259 free inodes.

server1 `/tmp`: 315553099776 available bytes; 82.40% used; 112445259 free inodes.

server1 `/var/tmp`: 315553099776 available bytes; 82.40% used; 112445259 free inodes.

server1 `/mnt/raid5`: 645855715328 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18032664576 available bytes; 98.99% used; 110367606 free inodes.

server2 `/home`: 18032664576 available bytes; 98.99% used; 110367606 free inodes.

server2 `/tmp`: 18032664576 available bytes; 98.99% used; 110367606 free inodes.

server2 `/var/tmp`: 18032664576 available bytes; 98.99% used; 110367606 free inodes.

server2 `/mnt/raid5`: 602328973312 available bytes; 95.84% used; 444966433 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81272123392 available bytes; 95.46% used; 114065371 free inodes.

server3 `/home`: 81272123392 available bytes; 95.46% used; 114065371 free inodes.

server3 `/data`: 1349039611904 available bytes; 81.36% used; 225834077 free inodes.

server3 `/tmp`: 81272123392 available bytes; 95.46% used; 114065371 free inodes.

server3 `/var/tmp`: 81272123392 available bytes; 95.46% used; 114065371 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105920860160 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105920860160 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410319167488 available bytes; 94.33% used; 224824169 free inodes.

server4 `/tmp`: 105920860160 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105920860160 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
