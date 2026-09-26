# V2R cluster inventory

2026-09-26T18:03:48.809834+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315568173056 available bytes; 82.40% used; 112445754 free inodes.

server1 `/home`: 315568173056 available bytes; 82.40% used; 112445754 free inodes.

server1 `/tmp`: 315568173056 available bytes; 82.40% used; 112445754 free inodes.

server1 `/var/tmp`: 315568173056 available bytes; 82.40% used; 112445754 free inodes.

server1 `/mnt/raid5`: 645854908416 available bytes; 97.04% used; 337467118 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18022789120 available bytes; 98.99% used; 110367620 free inodes.

server2 `/home`: 18022789120 available bytes; 98.99% used; 110367620 free inodes.

server2 `/tmp`: 18022789120 available bytes; 98.99% used; 110367620 free inodes.

server2 `/var/tmp`: 18022789120 available bytes; 98.99% used; 110367620 free inodes.

server2 `/mnt/raid5`: 604824522752 available bytes; 95.82% used; 444968422 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81273036800 available bytes; 95.46% used; 114065369 free inodes.

server3 `/home`: 81273036800 available bytes; 95.46% used; 114065369 free inodes.

server3 `/data`: 1349368483840 available bytes; 81.35% used; 225835333 free inodes.

server3 `/tmp`: 81273036800 available bytes; 95.46% used; 114065369 free inodes.

server3 `/var/tmp`: 81273036800 available bytes; 95.46% used; 114065369 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105939308544 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105939308544 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410377117696 available bytes; 94.33% used; 224824199 free inodes.

server4 `/tmp`: 105939308544 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105939308544 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
