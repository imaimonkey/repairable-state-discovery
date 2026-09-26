# V2R cluster inventory

2026-09-26T20:07:38.226780+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315538894848 available bytes; 82.40% used; 112445142 free inodes.

server1 `/home`: 315538894848 available bytes; 82.40% used; 112445142 free inodes.

server1 `/tmp`: 315538894848 available bytes; 82.40% used; 112445142 free inodes.

server1 `/var/tmp`: 315538894848 available bytes; 82.40% used; 112445142 free inodes.

server1 `/mnt/raid5`: 645855412224 available bytes; 97.04% used; 337467122 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18022313984 available bytes; 98.99% used; 110367553 free inodes.

server2 `/home`: 18022313984 available bytes; 98.99% used; 110367553 free inodes.

server2 `/tmp`: 18022313984 available bytes; 98.99% used; 110367553 free inodes.

server2 `/var/tmp`: 18022313984 available bytes; 98.99% used; 110367553 free inodes.

server2 `/mnt/raid5`: 601320620032 available bytes; 95.85% used; 444965284 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81264168960 available bytes; 95.47% used; 114065295 free inodes.

server3 `/home`: 81264168960 available bytes; 95.47% used; 114065295 free inodes.

server3 `/data`: 1348726874112 available bytes; 81.36% used; 225832954 free inodes.

server3 `/tmp`: 81264168960 available bytes; 95.47% used; 114065295 free inodes.

server3 `/var/tmp`: 81264168960 available bytes; 95.47% used; 114065295 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105919610880 available bytes; 94.09% used; 114347833 free inodes.

server4 `/home`: 105919610880 available bytes; 94.09% used; 114347833 free inodes.

server4 `/data`: 410268295168 available bytes; 94.33% used; 224824169 free inodes.

server4 `/tmp`: 105919610880 available bytes; 94.09% used; 114347833 free inodes.

server4 `/var/tmp`: 105919610880 available bytes; 94.09% used; 114347833 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
