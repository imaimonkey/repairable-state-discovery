# V2R cluster inventory

2026-09-26T14:04:42.358942+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318150115328 available bytes; 82.25% used; 112474401 free inodes.

server1 `/home`: 318150115328 available bytes; 82.25% used; 112474401 free inodes.

server1 `/tmp`: 318150115328 available bytes; 82.25% used; 112474401 free inodes.

server1 `/var/tmp`: 318150115328 available bytes; 82.25% used; 112474401 free inodes.

server1 `/mnt/raid5`: 674709741568 available bytes; 96.90% used; 337534714 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19080732672 available bytes; 98.94% used; 110378925 free inodes.

server2 `/home`: 19080732672 available bytes; 98.94% used; 110378925 free inodes.

server2 `/tmp`: 19080732672 available bytes; 98.94% used; 110378925 free inodes.

server2 `/var/tmp`: 19080732672 available bytes; 98.94% used; 110378925 free inodes.

server2 `/mnt/raid5`: 635571011584 available bytes; 95.61% used; 444975138 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82644258816 available bytes; 95.39% used; 114110790 free inodes.

server3 `/home`: 82644258816 available bytes; 95.39% used; 114110790 free inodes.

server3 `/data`: 1347030163456 available bytes; 81.38% used; 225812978 free inodes.

server3 `/tmp`: 82644258816 available bytes; 95.39% used; 114110790 free inodes.

server3 `/var/tmp`: 82644258816 available bytes; 95.39% used; 114110790 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105889456128 available bytes; 94.09% used; 114347933 free inodes.

server4 `/home`: 105889456128 available bytes; 94.09% used; 114347933 free inodes.

server4 `/data`: 411455614976 available bytes; 94.31% used; 224827197 free inodes.

server4 `/tmp`: 105889456128 available bytes; 94.09% used; 114347933 free inodes.

server4 `/var/tmp`: 105889456128 available bytes; 94.09% used; 114347933 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
