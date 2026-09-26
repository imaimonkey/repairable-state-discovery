# V2R cluster inventory

2026-09-26T17:09:14.451061+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315630800896 available bytes; 82.39% used; 112445890 free inodes.

server1 `/home`: 315630800896 available bytes; 82.39% used; 112445890 free inodes.

server1 `/tmp`: 315630800896 available bytes; 82.39% used; 112445890 free inodes.

server1 `/var/tmp`: 315630800896 available bytes; 82.39% used; 112445890 free inodes.

server1 `/mnt/raid5`: 645878112256 available bytes; 97.04% used; 337469092 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18030845952 available bytes; 98.99% used; 110367561 free inodes.

server2 `/home`: 18030845952 available bytes; 98.99% used; 110367561 free inodes.

server2 `/tmp`: 18030845952 available bytes; 98.99% used; 110367561 free inodes.

server2 `/var/tmp`: 18030845952 available bytes; 98.99% used; 110367561 free inodes.

server2 `/mnt/raid5`: 606666432512 available bytes; 95.81% used; 444970054 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81277030400 available bytes; 95.46% used; 114065342 free inodes.

server3 `/home`: 81277030400 available bytes; 95.46% used; 114065342 free inodes.

server3 `/data`: 1349318471680 available bytes; 81.35% used; 225836636 free inodes.

server3 `/tmp`: 81277030400 available bytes; 95.46% used; 114065342 free inodes.

server3 `/var/tmp`: 81277030400 available bytes; 95.46% used; 114065342 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952620544 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105952620544 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410524209152 available bytes; 94.33% used; 224824507 free inodes.

server4 `/tmp`: 105952620544 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105952620544 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
