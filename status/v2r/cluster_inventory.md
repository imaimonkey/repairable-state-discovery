# V2R cluster inventory

2026-09-26T14:36:44.277926+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318129606656 available bytes; 82.25% used; 112474364 free inodes.

server1 `/home`: 318129606656 available bytes; 82.25% used; 112474364 free inodes.

server1 `/tmp`: 318129606656 available bytes; 82.25% used; 112474364 free inodes.

server1 `/var/tmp`: 318129606656 available bytes; 82.25% used; 112474364 free inodes.

server1 `/mnt/raid5`: 674018476032 available bytes; 96.91% used; 337531925 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 15070130176 available bytes; 99.16% used; 110378828 free inodes.

server2 `/home`: 15070130176 available bytes; 99.16% used; 110378828 free inodes.

server2 `/tmp`: 15070130176 available bytes; 99.16% used; 110378828 free inodes.

server2 `/var/tmp`: 15070130176 available bytes; 99.16% used; 110378828 free inodes.

server2 `/mnt/raid5`: 634732941312 available bytes; 95.61% used; 444974226 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82629271552 available bytes; 95.39% used; 114110776 free inodes.

server3 `/home`: 82629271552 available bytes; 95.39% used; 114110776 free inodes.

server3 `/data`: 1346877403136 available bytes; 81.39% used; 225805146 free inodes.

server3 `/tmp`: 82629271552 available bytes; 95.39% used; 114110776 free inodes.

server3 `/var/tmp`: 82629271552 available bytes; 95.39% used; 114110776 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886781440 available bytes; 94.09% used; 114347844 free inodes.

server4 `/home`: 105886781440 available bytes; 94.09% used; 114347844 free inodes.

server4 `/data`: 411002802176 available bytes; 94.32% used; 224826671 free inodes.

server4 `/tmp`: 105886781440 available bytes; 94.09% used; 114347844 free inodes.

server4 `/var/tmp`: 105886781440 available bytes; 94.09% used; 114347844 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
