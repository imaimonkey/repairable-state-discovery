# V2R cluster inventory

2026-09-26T14:10:48.442113+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318134423552 available bytes; 82.25% used; 112474395 free inodes.

server1 `/home`: 318134423552 available bytes; 82.25% used; 112474395 free inodes.

server1 `/tmp`: 318134423552 available bytes; 82.25% used; 112474395 free inodes.

server1 `/var/tmp`: 318134423552 available bytes; 82.25% used; 112474395 free inodes.

server1 `/mnt/raid5`: 674019667968 available bytes; 96.91% used; 337532046 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19071119360 available bytes; 98.94% used; 110378919 free inodes.

server2 `/home`: 19071119360 available bytes; 98.94% used; 110378919 free inodes.

server2 `/tmp`: 19071119360 available bytes; 98.94% used; 110378919 free inodes.

server2 `/var/tmp`: 19071119360 available bytes; 98.94% used; 110378919 free inodes.

server2 `/mnt/raid5`: 635483090944 available bytes; 95.61% used; 444975281 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82642657280 available bytes; 95.39% used; 114110796 free inodes.

server3 `/home`: 82642657280 available bytes; 95.39% used; 114110796 free inodes.

server3 `/data`: 1346980085760 available bytes; 81.38% used; 225808939 free inodes.

server3 `/tmp`: 82642657280 available bytes; 95.39% used; 114110796 free inodes.

server3 `/var/tmp`: 82642657280 available bytes; 95.39% used; 114110796 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105889325056 available bytes; 94.09% used; 114347928 free inodes.

server4 `/home`: 105889325056 available bytes; 94.09% used; 114347928 free inodes.

server4 `/data`: 411035996160 available bytes; 94.32% used; 224826933 free inodes.

server4 `/tmp`: 105889325056 available bytes; 94.09% used; 114347928 free inodes.

server4 `/var/tmp`: 105889325056 available bytes; 94.09% used; 114347928 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
