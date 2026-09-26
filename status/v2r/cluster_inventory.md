# V2R cluster inventory

2026-09-26T16:43:19.434359+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318127779840 available bytes; 82.25% used; 112473835 free inodes.

server1 `/home`: 318127779840 available bytes; 82.25% used; 112473835 free inodes.

server1 `/tmp`: 318127779840 available bytes; 82.25% used; 112473835 free inodes.

server1 `/var/tmp`: 318127779840 available bytes; 82.25% used; 112473835 free inodes.

server1 `/mnt/raid5`: 654102265856 available bytes; 97.00% used; 337531408 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18024886272 available bytes; 98.99% used; 110367553 free inodes.

server2 `/home`: 18024886272 available bytes; 98.99% used; 110367553 free inodes.

server2 `/tmp`: 18024886272 available bytes; 98.99% used; 110367553 free inodes.

server2 `/var/tmp`: 18024886272 available bytes; 98.99% used; 110367553 free inodes.

server2 `/mnt/raid5`: 606797582336 available bytes; 95.81% used; 444970617 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81276125184 available bytes; 95.46% used; 114065345 free inodes.

server3 `/home`: 81276125184 available bytes; 95.46% used; 114065345 free inodes.

server3 `/data`: 1349251235840 available bytes; 81.35% used; 225830054 free inodes.

server3 `/tmp`: 81276125184 available bytes; 95.46% used; 114065345 free inodes.

server3 `/var/tmp`: 81276125184 available bytes; 95.46% used; 114065345 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953247232 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105953247232 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410534137856 available bytes; 94.33% used; 224824589 free inodes.

server4 `/tmp`: 105953247232 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105953247232 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
