# V2R cluster inventory

2026-09-26T18:13:16.851329+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315566268416 available bytes; 82.40% used; 112445741 free inodes.

server1 `/home`: 315566268416 available bytes; 82.40% used; 112445741 free inodes.

server1 `/tmp`: 315566268416 available bytes; 82.40% used; 112445741 free inodes.

server1 `/var/tmp`: 315566268416 available bytes; 82.40% used; 112445741 free inodes.

server1 `/mnt/raid5`: 645855244288 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18030866432 available bytes; 98.99% used; 110367618 free inodes.

server2 `/home`: 18030866432 available bytes; 98.99% used; 110367618 free inodes.

server2 `/tmp`: 18030866432 available bytes; 98.99% used; 110367618 free inodes.

server2 `/var/tmp`: 18030866432 available bytes; 98.99% used; 110367618 free inodes.

server2 `/mnt/raid5`: 604571525120 available bytes; 95.82% used; 444968297 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81272446976 available bytes; 95.46% used; 114065371 free inodes.

server3 `/home`: 81272446976 available bytes; 95.46% used; 114065371 free inodes.

server3 `/data`: 1349357608960 available bytes; 81.35% used; 225835144 free inodes.

server3 `/tmp`: 81272446976 available bytes; 95.46% used; 114065371 free inodes.

server3 `/var/tmp`: 81272446976 available bytes; 95.46% used; 114065371 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105939050496 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105939050496 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410368851968 available bytes; 94.33% used; 224824201 free inodes.

server4 `/tmp`: 105939050496 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105939050496 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
