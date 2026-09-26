# V2R cluster inventory

2026-09-26T14:09:16.945036+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318136758272 available bytes; 82.25% used; 112474386 free inodes.

server1 `/home`: 318136758272 available bytes; 82.25% used; 112474386 free inodes.

server1 `/tmp`: 318136758272 available bytes; 82.25% used; 112474386 free inodes.

server1 `/var/tmp`: 318136758272 available bytes; 82.25% used; 112474386 free inodes.

server1 `/mnt/raid5`: 674022252544 available bytes; 96.91% used; 337532117 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19071578112 available bytes; 98.94% used; 110378920 free inodes.

server2 `/home`: 19071578112 available bytes; 98.94% used; 110378920 free inodes.

server2 `/tmp`: 19071578112 available bytes; 98.94% used; 110378920 free inodes.

server2 `/var/tmp`: 19071578112 available bytes; 98.94% used; 110378920 free inodes.

server2 `/mnt/raid5`: 635453857792 available bytes; 95.61% used; 444975425 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82643353600 available bytes; 95.39% used; 114110796 free inodes.

server3 `/home`: 82643353600 available bytes; 95.39% used; 114110796 free inodes.

server3 `/data`: 1346992750592 available bytes; 81.38% used; 225808979 free inodes.

server3 `/tmp`: 82643353600 available bytes; 95.39% used; 114110796 free inodes.

server3 `/var/tmp`: 82643353600 available bytes; 95.39% used; 114110796 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105889370112 available bytes; 94.09% used; 114347928 free inodes.

server4 `/home`: 105889370112 available bytes; 94.09% used; 114347928 free inodes.

server4 `/data`: 411042418688 available bytes; 94.32% used; 224826933 free inodes.

server4 `/tmp`: 105889370112 available bytes; 94.09% used; 114347928 free inodes.

server4 `/var/tmp`: 105889370112 available bytes; 94.09% used; 114347928 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
