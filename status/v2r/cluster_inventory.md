# V2R cluster inventory

2026-09-26T13:00:37.205810+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318153764864 available bytes; 82.25% used; 112474490 free inodes.

server1 `/home`: 318153764864 available bytes; 82.25% used; 112474490 free inodes.

server1 `/tmp`: 318153764864 available bytes; 82.25% used; 112474490 free inodes.

server1 `/var/tmp`: 318153764864 available bytes; 82.25% used; 112474490 free inodes.

server1 `/mnt/raid5`: 675391950848 available bytes; 96.90% used; 337537606 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19159584768 available bytes; 98.93% used; 110381030 free inodes.

server2 `/home`: 19159584768 available bytes; 98.93% used; 110381030 free inodes.

server2 `/tmp`: 19159584768 available bytes; 98.93% used; 110381030 free inodes.

server2 `/var/tmp`: 19159584768 available bytes; 98.93% used; 110381030 free inodes.

server2 `/mnt/raid5`: 637615656960 available bytes; 95.59% used; 444976975 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82651029504 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82651029504 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 1347687284736 available bytes; 81.37% used; 225823334 free inodes.

server3 `/tmp`: 82651029504 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82651029504 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105899073536 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105899073536 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 413510713344 available bytes; 94.29% used; 224846990 free inodes.

server4 `/tmp`: 105899073536 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105899073536 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
