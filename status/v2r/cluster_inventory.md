# V2R cluster inventory

2026-09-26T18:39:12.330620+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315567190016 available bytes; 82.40% used; 112445745 free inodes.

server1 `/home`: 315567190016 available bytes; 82.40% used; 112445745 free inodes.

server1 `/tmp`: 315567190016 available bytes; 82.40% used; 112445745 free inodes.

server1 `/var/tmp`: 315567190016 available bytes; 82.40% used; 112445745 free inodes.

server1 `/mnt/raid5`: 645854740480 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18031288320 available bytes; 98.99% used; 110367618 free inodes.

server2 `/home`: 18031288320 available bytes; 98.99% used; 110367618 free inodes.

server2 `/tmp`: 18031288320 available bytes; 98.99% used; 110367618 free inodes.

server2 `/var/tmp`: 18031288320 available bytes; 98.99% used; 110367618 free inodes.

server2 `/mnt/raid5`: 603277041664 available bytes; 95.83% used; 444967574 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81275777024 available bytes; 95.46% used; 114065373 free inodes.

server3 `/home`: 81275777024 available bytes; 95.46% used; 114065373 free inodes.

server3 `/data`: 1349259976704 available bytes; 81.35% used; 225834695 free inodes.

server3 `/tmp`: 81275777024 available bytes; 95.46% used; 114065373 free inodes.

server3 `/var/tmp`: 81275777024 available bytes; 95.46% used; 114065373 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105938456576 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105938456576 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410353577984 available bytes; 94.33% used; 224824177 free inodes.

server4 `/tmp`: 105938456576 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105938456576 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
