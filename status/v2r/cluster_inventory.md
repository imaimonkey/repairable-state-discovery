# V2R cluster inventory

2026-09-25T10:57:51.330703+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319064190976 available bytes; 82.20% used; 112478862 free inodes.

server1 `/home`: 319064190976 available bytes; 82.20% used; 112478862 free inodes.

server1 `/tmp`: 319064190976 available bytes; 82.20% used; 112478862 free inodes.

server1 `/var/tmp`: 319064190976 available bytes; 82.20% used; 112478862 free inodes.

server1 `/mnt/raid5`: 364863811584 available bytes; 98.33% used; 337555191 free inodes.
| server2 | True | ['1', '2', '3', '5', '6'] | [] |

server2 `/`: 22912679936 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22912679936 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22912679936 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22912679936 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 329178406912 available bytes; 97.73% used; 445089237 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84505829376 available bytes; 95.28% used; 114155533 free inodes.

server3 `/home`: 84505829376 available bytes; 95.28% used; 114155533 free inodes.

server3 `/data`: 142005063680 available bytes; 98.04% used; 225815240 free inodes.

server3 `/tmp`: 84505829376 available bytes; 95.28% used; 114155533 free inodes.

server3 `/var/tmp`: 84505829376 available bytes; 95.28% used; 114155533 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105612541952 available bytes; 94.11% used; 114350252 free inodes.

server4 `/home`: 105612541952 available bytes; 94.11% used; 114350252 free inodes.

server4 `/data`: 238574653440 available bytes; 96.70% used; 224984251 free inodes.

server4 `/tmp`: 105612541952 available bytes; 94.11% used; 114350252 free inodes.

server4 `/var/tmp`: 105612541952 available bytes; 94.11% used; 114350252 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
