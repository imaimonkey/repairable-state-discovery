# V2R cluster inventory

2026-09-26T14:03:10.775258+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318151155712 available bytes; 82.25% used; 112474403 free inodes.

server1 `/home`: 318151155712 available bytes; 82.25% used; 112474403 free inodes.

server1 `/tmp`: 318151155712 available bytes; 82.25% used; 112474403 free inodes.

server1 `/var/tmp`: 318151155712 available bytes; 82.25% used; 112474403 free inodes.

server1 `/mnt/raid5`: 674707460096 available bytes; 96.90% used; 337534728 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19080921088 available bytes; 98.94% used; 110378925 free inodes.

server2 `/home`: 19080921088 available bytes; 98.94% used; 110378925 free inodes.

server2 `/tmp`: 19080921088 available bytes; 98.94% used; 110378925 free inodes.

server2 `/var/tmp`: 19080921088 available bytes; 98.94% used; 110378925 free inodes.

server2 `/mnt/raid5`: 635611742208 available bytes; 95.61% used; 444975205 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82643812352 available bytes; 95.39% used; 114110791 free inodes.

server3 `/home`: 82643812352 available bytes; 95.39% used; 114110791 free inodes.

server3 `/data`: 1347105308672 available bytes; 81.38% used; 225816177 free inodes.

server3 `/tmp`: 82643812352 available bytes; 95.39% used; 114110791 free inodes.

server3 `/var/tmp`: 82643812352 available bytes; 95.39% used; 114110791 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105889406976 available bytes; 94.09% used; 114347937 free inodes.

server4 `/home`: 105889406976 available bytes; 94.09% used; 114347937 free inodes.

server4 `/data`: 411423240192 available bytes; 94.31% used; 224826994 free inodes.

server4 `/tmp`: 105889406976 available bytes; 94.09% used; 114347937 free inodes.

server4 `/var/tmp`: 105889406976 available bytes; 94.09% used; 114347937 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
