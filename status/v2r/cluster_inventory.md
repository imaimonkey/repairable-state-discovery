# V2R cluster inventory

2026-09-26T03:13:47.901790+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318417981440 available bytes; 82.24% used; 112476252 free inodes.

server1 `/home`: 318417981440 available bytes; 82.24% used; 112476252 free inodes.

server1 `/tmp`: 318417981440 available bytes; 82.24% used; 112476252 free inodes.

server1 `/var/tmp`: 318417981440 available bytes; 82.24% used; 112476252 free inodes.

server1 `/mnt/raid5`: 331051360256 available bytes; 98.48% used; 337545888 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22940766208 available bytes; 98.72% used; 110406212 free inodes.

server2 `/home`: 22940766208 available bytes; 98.72% used; 110406212 free inodes.

server2 `/tmp`: 22940766208 available bytes; 98.72% used; 110406212 free inodes.

server2 `/var/tmp`: 22940766208 available bytes; 98.72% used; 110406212 free inodes.

server2 `/mnt/raid5`: 287173713920 available bytes; 98.02% used; 445053019 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84311773184 available bytes; 95.30% used; 114152350 free inodes.

server3 `/home`: 84311773184 available bytes; 95.30% used; 114152350 free inodes.

server3 `/data`: 125436575744 available bytes; 98.27% used; 225830882 free inodes.

server3 `/tmp`: 84311773184 available bytes; 95.30% used; 114152350 free inodes.

server3 `/var/tmp`: 84311773184 available bytes; 95.30% used; 114152350 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918345216 available bytes; 94.09% used; 114347136 free inodes.

server4 `/home`: 105918345216 available bytes; 94.09% used; 114347136 free inodes.

server4 `/data`: 109003792384 available bytes; 98.49% used; 224914850 free inodes.

server4 `/tmp`: 105918345216 available bytes; 94.09% used; 114347136 free inodes.

server4 `/var/tmp`: 105918345216 available bytes; 94.09% used; 114347136 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
