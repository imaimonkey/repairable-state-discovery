# V2R cluster inventory

2026-09-25T22:35:39.075096+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318693294080 available bytes; 82.22% used; 112476313 free inodes.

server1 `/home`: 318693294080 available bytes; 82.22% used; 112476313 free inodes.

server1 `/tmp`: 318693294080 available bytes; 82.22% used; 112476313 free inodes.

server1 `/var/tmp`: 318693294080 available bytes; 82.22% used; 112476313 free inodes.

server1 `/mnt/raid5`: 360238018560 available bytes; 98.35% used; 337538925 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22952914944 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22952914944 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22952914944 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22952914944 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 298792206336 available bytes; 97.94% used; 445052612 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84355518464 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84355518464 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124825632768 available bytes; 98.27% used; 225805840 free inodes.

server3 `/tmp`: 84355518464 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84355518464 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105235881984 available bytes; 94.13% used; 114346966 free inodes.

server4 `/home`: 105235881984 available bytes; 94.13% used; 114346966 free inodes.

server4 `/data`: 192244715520 available bytes; 97.34% used; 224917712 free inodes.

server4 `/tmp`: 105235881984 available bytes; 94.13% used; 114346966 free inodes.

server4 `/var/tmp`: 105235881984 available bytes; 94.13% used; 114346966 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
