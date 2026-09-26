# V2R cluster inventory

2026-09-26T17:57:43.266733+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315584339968 available bytes; 82.39% used; 112445754 free inodes.

server1 `/home`: 315584339968 available bytes; 82.39% used; 112445754 free inodes.

server1 `/tmp`: 315584339968 available bytes; 82.39% used; 112445754 free inodes.

server1 `/var/tmp`: 315584339968 available bytes; 82.39% used; 112445754 free inodes.

server1 `/mnt/raid5`: 645856739328 available bytes; 97.04% used; 337467124 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18024206336 available bytes; 98.99% used; 110367620 free inodes.

server2 `/home`: 18024206336 available bytes; 98.99% used; 110367620 free inodes.

server2 `/tmp`: 18024206336 available bytes; 98.99% used; 110367620 free inodes.

server2 `/var/tmp`: 18024206336 available bytes; 98.99% used; 110367620 free inodes.

server2 `/mnt/raid5`: 605032910848 available bytes; 95.82% used; 444968856 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81273487360 available bytes; 95.46% used; 114065375 free inodes.

server3 `/home`: 81273487360 available bytes; 95.46% used; 114065375 free inodes.

server3 `/data`: 1349367603200 available bytes; 81.35% used; 225835400 free inodes.

server3 `/tmp`: 81273487360 available bytes; 95.46% used; 114065375 free inodes.

server3 `/var/tmp`: 81273487360 available bytes; 95.46% used; 114065375 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105939456000 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105939456000 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410382397440 available bytes; 94.33% used; 224824191 free inodes.

server4 `/tmp`: 105939456000 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105939456000 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
