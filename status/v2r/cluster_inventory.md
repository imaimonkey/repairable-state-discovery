# V2R cluster inventory

2026-09-26T17:51:37.693966+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315584917504 available bytes; 82.39% used; 112445768 free inodes.

server1 `/home`: 315584917504 available bytes; 82.39% used; 112445768 free inodes.

server1 `/tmp`: 315584917504 available bytes; 82.39% used; 112445768 free inodes.

server1 `/var/tmp`: 315584917504 available bytes; 82.39% used; 112445768 free inodes.

server1 `/mnt/raid5`: 645853409280 available bytes; 97.04% used; 337467122 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18024087552 available bytes; 98.99% used; 110367620 free inodes.

server2 `/home`: 18024087552 available bytes; 98.99% used; 110367620 free inodes.

server2 `/tmp`: 18024087552 available bytes; 98.99% used; 110367620 free inodes.

server2 `/var/tmp`: 18024087552 available bytes; 98.99% used; 110367620 free inodes.

server2 `/mnt/raid5`: 605199040512 available bytes; 95.82% used; 444969024 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81273458688 available bytes; 95.46% used; 114065377 free inodes.

server3 `/home`: 81273458688 available bytes; 95.46% used; 114065377 free inodes.

server3 `/data`: 1349369098240 available bytes; 81.35% used; 225835489 free inodes.

server3 `/tmp`: 81273458688 available bytes; 95.46% used; 114065377 free inodes.

server3 `/var/tmp`: 81273458688 available bytes; 95.46% used; 114065377 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105939574784 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105939574784 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410385895424 available bytes; 94.33% used; 224824203 free inodes.

server4 `/tmp`: 105939574784 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105939574784 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
