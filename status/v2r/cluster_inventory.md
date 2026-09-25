# V2R cluster inventory

2026-09-25T10:54:45.813843+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319063126016 available bytes; 82.20% used; 112478880 free inodes.

server1 `/home`: 319063126016 available bytes; 82.20% used; 112478880 free inodes.

server1 `/tmp`: 319063126016 available bytes; 82.20% used; 112478880 free inodes.

server1 `/var/tmp`: 319063126016 available bytes; 82.20% used; 112478880 free inodes.

server1 `/mnt/raid5`: 367917453312 available bytes; 98.31% used; 337555261 free inodes.
| server2 | True | ['1', '2', '3', '5', '6'] | [] |

server2 `/`: 22912503808 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22912503808 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22912503808 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22912503808 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 328733741056 available bytes; 97.73% used; 445089352 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84420050944 available bytes; 95.29% used; 114156045 free inodes.

server3 `/home`: 84420050944 available bytes; 95.29% used; 114156045 free inodes.

server3 `/data`: 142006284288 available bytes; 98.04% used; 225815293 free inodes.

server3 `/tmp`: 84420050944 available bytes; 95.29% used; 114156045 free inodes.

server3 `/var/tmp`: 84420050944 available bytes; 95.29% used; 114156045 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105612636160 available bytes; 94.11% used; 114350252 free inodes.

server4 `/home`: 105612636160 available bytes; 94.11% used; 114350252 free inodes.

server4 `/data`: 238576115712 available bytes; 96.70% used; 224984462 free inodes.

server4 `/tmp`: 105612636160 available bytes; 94.11% used; 114350252 free inodes.

server4 `/var/tmp`: 105612636160 available bytes; 94.11% used; 114350252 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
