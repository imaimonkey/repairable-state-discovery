# V2R cluster inventory

2026-09-26T20:01:32.338760+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315539783680 available bytes; 82.40% used; 112445152 free inodes.

server1 `/home`: 315539783680 available bytes; 82.40% used; 112445152 free inodes.

server1 `/tmp`: 315539783680 available bytes; 82.40% used; 112445152 free inodes.

server1 `/var/tmp`: 315539783680 available bytes; 82.40% used; 112445152 free inodes.

server1 `/mnt/raid5`: 645853405184 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18030710784 available bytes; 98.99% used; 110367559 free inodes.

server2 `/home`: 18030710784 available bytes; 98.99% used; 110367559 free inodes.

server2 `/tmp`: 18030710784 available bytes; 98.99% used; 110367559 free inodes.

server2 `/var/tmp`: 18030710784 available bytes; 98.99% used; 110367559 free inodes.

server2 `/mnt/raid5`: 601497477120 available bytes; 95.84% used; 444965583 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81265774592 available bytes; 95.47% used; 114065304 free inodes.

server3 `/home`: 81265774592 available bytes; 95.47% used; 114065304 free inodes.

server3 `/data`: 1348730810368 available bytes; 81.36% used; 225833079 free inodes.

server3 `/tmp`: 81265774592 available bytes; 95.47% used; 114065304 free inodes.

server3 `/var/tmp`: 81265774592 available bytes; 95.47% used; 114065304 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105919741952 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105919741952 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410274775040 available bytes; 94.33% used; 224824175 free inodes.

server4 `/tmp`: 105919741952 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105919741952 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
