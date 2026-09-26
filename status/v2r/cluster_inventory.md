# V2R cluster inventory

2026-09-26T17:29:03.733544+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315597516800 available bytes; 82.39% used; 112445886 free inodes.

server1 `/home`: 315597516800 available bytes; 82.39% used; 112445886 free inodes.

server1 `/tmp`: 315597516800 available bytes; 82.39% used; 112445886 free inodes.

server1 `/var/tmp`: 315597516800 available bytes; 82.39% used; 112445886 free inodes.

server1 `/mnt/raid5`: 645852405760 available bytes; 97.04% used; 337467116 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18022690816 available bytes; 98.99% used; 110367626 free inodes.

server2 `/home`: 18022690816 available bytes; 98.99% used; 110367626 free inodes.

server2 `/tmp`: 18022690816 available bytes; 98.99% used; 110367626 free inodes.

server2 `/var/tmp`: 18022690816 available bytes; 98.99% used; 110367626 free inodes.

server2 `/mnt/raid5`: 605587611648 available bytes; 95.82% used; 444969639 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81275981824 available bytes; 95.46% used; 114065401 free inodes.

server3 `/home`: 81275981824 available bytes; 95.46% used; 114065401 free inodes.

server3 `/data`: 1349215424512 available bytes; 81.35% used; 225836171 free inodes.

server3 `/tmp`: 81275981824 available bytes; 95.46% used; 114065401 free inodes.

server3 `/var/tmp`: 81275981824 available bytes; 95.46% used; 114065401 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952137216 available bytes; 94.09% used; 114347874 free inodes.

server4 `/home`: 105952137216 available bytes; 94.09% used; 114347874 free inodes.

server4 `/data`: 410446782464 available bytes; 94.33% used; 224824480 free inodes.

server4 `/tmp`: 105952137216 available bytes; 94.09% used; 114347874 free inodes.

server4 `/var/tmp`: 105952137216 available bytes; 94.09% used; 114347874 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
