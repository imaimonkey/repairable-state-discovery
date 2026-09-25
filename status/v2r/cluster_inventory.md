# V2R cluster inventory

2026-09-25T22:15:47.730557+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318692126720 available bytes; 82.22% used; 112476302 free inodes.

server1 `/home`: 318692126720 available bytes; 82.22% used; 112476302 free inodes.

server1 `/tmp`: 318692126720 available bytes; 82.22% used; 112476302 free inodes.

server1 `/var/tmp`: 318692126720 available bytes; 82.22% used; 112476302 free inodes.

server1 `/mnt/raid5`: 360273100800 available bytes; 98.35% used; 337539015 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22947233792 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22947233792 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22947233792 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22947233792 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 299395465216 available bytes; 97.93% used; 445053486 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84357357568 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84357357568 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 125873541120 available bytes; 98.26% used; 225806226 free inodes.

server3 `/tmp`: 84357357568 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84357357568 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105312083968 available bytes; 94.12% used; 114347145 free inodes.

server4 `/home`: 105312083968 available bytes; 94.12% used; 114347145 free inodes.

server4 `/data`: 207985459200 available bytes; 97.13% used; 224917956 free inodes.

server4 `/tmp`: 105312083968 available bytes; 94.12% used; 114347145 free inodes.

server4 `/var/tmp`: 105312083968 available bytes; 94.12% used; 114347145 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
