# V2R cluster inventory

2026-09-26T17:59:33.374102+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315583709184 available bytes; 82.39% used; 112445753 free inodes.

server1 `/home`: 315583709184 available bytes; 82.39% used; 112445753 free inodes.

server1 `/tmp`: 315583709184 available bytes; 82.39% used; 112445753 free inodes.

server1 `/var/tmp`: 315583709184 available bytes; 82.39% used; 112445753 free inodes.

server1 `/mnt/raid5`: 645856321536 available bytes; 97.04% used; 337467124 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18024067072 available bytes; 98.99% used; 110367620 free inodes.

server2 `/home`: 18024067072 available bytes; 98.99% used; 110367620 free inodes.

server2 `/tmp`: 18024067072 available bytes; 98.99% used; 110367620 free inodes.

server2 `/var/tmp`: 18024067072 available bytes; 98.99% used; 110367620 free inodes.

server2 `/mnt/raid5`: 604976644096 available bytes; 95.82% used; 444968671 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81277558784 available bytes; 95.46% used; 114065375 free inodes.

server3 `/home`: 81277558784 available bytes; 95.46% used; 114065375 free inodes.

server3 `/data`: 1349373702144 available bytes; 81.35% used; 225835375 free inodes.

server3 `/tmp`: 81277558784 available bytes; 95.46% used; 114065375 free inodes.

server3 `/var/tmp`: 81277558784 available bytes; 95.46% used; 114065375 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105939398656 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105939398656 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410383638528 available bytes; 94.33% used; 224824193 free inodes.

server4 `/tmp`: 105939398656 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105939398656 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
