# V2R cluster inventory

2026-09-26T14:07:45.444272+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318149193728 available bytes; 82.25% used; 112474390 free inodes.

server1 `/home`: 318149193728 available bytes; 82.25% used; 112474390 free inodes.

server1 `/tmp`: 318149193728 available bytes; 82.25% used; 112474390 free inodes.

server1 `/var/tmp`: 318149193728 available bytes; 82.25% used; 112474390 free inodes.

server1 `/mnt/raid5`: 674063564800 available bytes; 96.91% used; 337532754 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19072000000 available bytes; 98.94% used; 110378926 free inodes.

server2 `/home`: 19072000000 available bytes; 98.94% used; 110378926 free inodes.

server2 `/tmp`: 19072000000 available bytes; 98.94% used; 110378926 free inodes.

server2 `/var/tmp`: 19072000000 available bytes; 98.94% used; 110378926 free inodes.

server2 `/mnt/raid5`: 635504054272 available bytes; 95.61% used; 444975478 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82643660800 available bytes; 95.39% used; 114110790 free inodes.

server3 `/home`: 82643660800 available bytes; 95.39% used; 114110790 free inodes.

server3 `/data`: 1346988396544 available bytes; 81.38% used; 225808830 free inodes.

server3 `/tmp`: 82643660800 available bytes; 95.39% used; 114110790 free inodes.

server3 `/var/tmp`: 82643660800 available bytes; 95.39% used; 114110790 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105889394688 available bytes; 94.09% used; 114347928 free inodes.

server4 `/home`: 105889394688 available bytes; 94.09% used; 114347928 free inodes.

server4 `/data`: 411042381824 available bytes; 94.32% used; 224826945 free inodes.

server4 `/tmp`: 105889394688 available bytes; 94.09% used; 114347928 free inodes.

server4 `/var/tmp`: 105889394688 available bytes; 94.09% used; 114347928 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
