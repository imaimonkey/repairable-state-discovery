# V2R cluster inventory

2026-09-26T13:31:08.655354+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318155472896 available bytes; 82.25% used; 112474430 free inodes.

server1 `/home`: 318155472896 available bytes; 82.25% used; 112474430 free inodes.

server1 `/tmp`: 318155472896 available bytes; 82.25% used; 112474430 free inodes.

server1 `/var/tmp`: 318155472896 available bytes; 82.25% used; 112474430 free inodes.

server1 `/mnt/raid5`: 674743382016 available bytes; 96.90% used; 337535766 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19075182592 available bytes; 98.94% used; 110378934 free inodes.

server2 `/home`: 19075182592 available bytes; 98.94% used; 110378934 free inodes.

server2 `/tmp`: 19075182592 available bytes; 98.94% used; 110378934 free inodes.

server2 `/var/tmp`: 19075182592 available bytes; 98.94% used; 110378934 free inodes.

server2 `/mnt/raid5`: 636510564352 available bytes; 95.60% used; 444976210 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82645147648 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82645147648 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 1347500773376 available bytes; 81.38% used; 225822991 free inodes.

server3 `/tmp`: 82645147648 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82645147648 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898491904 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105898491904 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 411555762176 available bytes; 94.31% used; 224827610 free inodes.

server4 `/tmp`: 105898491904 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105898491904 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
