# V2R cluster inventory

2026-09-26T19:01:41.965458+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315557203968 available bytes; 82.40% used; 112445738 free inodes.

server1 `/home`: 315557203968 available bytes; 82.40% used; 112445738 free inodes.

server1 `/tmp`: 315557203968 available bytes; 82.40% used; 112445738 free inodes.

server1 `/var/tmp`: 315557203968 available bytes; 82.40% used; 112445738 free inodes.

server1 `/mnt/raid5`: 645853990912 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18023374848 available bytes; 98.99% used; 110367602 free inodes.

server2 `/home`: 18023374848 available bytes; 98.99% used; 110367602 free inodes.

server2 `/tmp`: 18023374848 available bytes; 98.99% used; 110367602 free inodes.

server2 `/var/tmp`: 18023374848 available bytes; 98.99% used; 110367602 free inodes.

server2 `/mnt/raid5`: 603181424640 available bytes; 95.83% used; 444966963 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81274236928 available bytes; 95.46% used; 114065374 free inodes.

server3 `/home`: 81274236928 available bytes; 95.46% used; 114065374 free inodes.

server3 `/data`: 1349135167488 available bytes; 81.35% used; 225834288 free inodes.

server3 `/tmp`: 81274236928 available bytes; 95.46% used; 114065374 free inodes.

server3 `/var/tmp`: 81274236928 available bytes; 95.46% used; 114065374 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105929527296 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105929527296 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410328477696 available bytes; 94.33% used; 224824169 free inodes.

server4 `/tmp`: 105929527296 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105929527296 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
