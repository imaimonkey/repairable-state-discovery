# V2R cluster inventory

2026-09-26T14:24:32.387935+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318129410048 available bytes; 82.25% used; 112474362 free inodes.

server1 `/home`: 318129410048 available bytes; 82.25% used; 112474362 free inodes.

server1 `/tmp`: 318129410048 available bytes; 82.25% used; 112474362 free inodes.

server1 `/var/tmp`: 318129410048 available bytes; 82.25% used; 112474362 free inodes.

server1 `/mnt/raid5`: 674013888512 available bytes; 96.91% used; 337531924 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 16086097920 available bytes; 99.10% used; 110378827 free inodes.

server2 `/home`: 16086097920 available bytes; 99.10% used; 110378827 free inodes.

server2 `/tmp`: 16086097920 available bytes; 99.10% used; 110378827 free inodes.

server2 `/var/tmp`: 16086097920 available bytes; 99.10% used; 110378827 free inodes.

server2 `/mnt/raid5`: 634557853696 available bytes; 95.62% used; 444974781 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82631761920 available bytes; 95.39% used; 114110778 free inodes.

server3 `/home`: 82631761920 available bytes; 95.39% used; 114110778 free inodes.

server3 `/data`: 1346884444160 available bytes; 81.39% used; 225805275 free inodes.

server3 `/tmp`: 82631761920 available bytes; 95.39% used; 114110778 free inodes.

server3 `/var/tmp`: 82631761920 available bytes; 95.39% used; 114110778 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105887019008 available bytes; 94.09% used; 114347844 free inodes.

server4 `/home`: 105887019008 available bytes; 94.09% used; 114347844 free inodes.

server4 `/data`: 411017854976 available bytes; 94.32% used; 224826774 free inodes.

server4 `/tmp`: 105887019008 available bytes; 94.09% used; 114347844 free inodes.

server4 `/var/tmp`: 105887019008 available bytes; 94.09% used; 114347844 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
