# V2R cluster inventory

2026-09-26T19:47:49.093836+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315541209088 available bytes; 82.40% used; 112445148 free inodes.

server1 `/home`: 315541209088 available bytes; 82.40% used; 112445148 free inodes.

server1 `/tmp`: 315541209088 available bytes; 82.40% used; 112445148 free inodes.

server1 `/var/tmp`: 315541209088 available bytes; 82.40% used; 112445148 free inodes.

server1 `/mnt/raid5`: 645854822400 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18031177728 available bytes; 98.99% used; 110367537 free inodes.

server2 `/home`: 18031177728 available bytes; 98.99% used; 110367537 free inodes.

server2 `/tmp`: 18031177728 available bytes; 98.99% used; 110367537 free inodes.

server2 `/var/tmp`: 18031177728 available bytes; 98.99% used; 110367537 free inodes.

server2 `/mnt/raid5`: 601879302144 available bytes; 95.84% used; 444965818 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81264881664 available bytes; 95.47% used; 114065303 free inodes.

server3 `/home`: 81264881664 available bytes; 95.47% used; 114065303 free inodes.

server3 `/data`: 1348740009984 available bytes; 81.36% used; 225833368 free inodes.

server3 `/tmp`: 81264881664 available bytes; 95.47% used; 114065303 free inodes.

server3 `/var/tmp`: 81264881664 available bytes; 95.47% used; 114065303 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105920073728 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105920073728 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410287869952 available bytes; 94.33% used; 224824171 free inodes.

server4 `/tmp`: 105920073728 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105920073728 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
