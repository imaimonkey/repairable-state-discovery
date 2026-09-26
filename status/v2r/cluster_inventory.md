# V2R cluster inventory

2026-09-26T22:53:48.317614+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315471781888 available bytes; 82.40% used; 112445701 free inodes.

server1 `/home`: 315471781888 available bytes; 82.40% used; 112445701 free inodes.

server1 `/tmp`: 315471781888 available bytes; 82.40% used; 112445701 free inodes.

server1 `/var/tmp`: 315471781888 available bytes; 82.40% used; 112445701 free inodes.

server1 `/mnt/raid5`: 645834260480 available bytes; 97.04% used; 337467224 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17946857472 available bytes; 99.00% used; 110367507 free inodes.

server2 `/home`: 17946857472 available bytes; 99.00% used; 110367507 free inodes.

server2 `/tmp`: 17946857472 available bytes; 99.00% used; 110367507 free inodes.

server2 `/var/tmp`: 17946857472 available bytes; 99.00% used; 110367507 free inodes.

server2 `/mnt/raid5`: 596406145024 available bytes; 95.88% used; 444960721 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 81084022784 available bytes; 95.48% used; 114069879 free inodes.

server3 `/home`: 81084022784 available bytes; 95.48% used; 114069879 free inodes.

server3 `/data`: 1349238804480 available bytes; 81.35% used; 225826786 free inodes.

server3 `/tmp`: 81084022784 available bytes; 95.48% used; 114069879 free inodes.

server3 `/var/tmp`: 81084022784 available bytes; 95.48% used; 114069879 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898598400 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105898598400 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409619820544 available bytes; 94.34% used; 224823835 free inodes.

server4 `/tmp`: 105898598400 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105898598400 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
