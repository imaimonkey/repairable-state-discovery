# V2R cluster inventory

2026-09-24T03:08:11.410238+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325369335808 available bytes; 81.85% used; 112498452 free inodes.

server1 `/home`: 325369335808 available bytes; 81.85% used; 112498452 free inodes.

server1 `/tmp`: 325369335808 available bytes; 81.85% used; 112498452 free inodes.

server1 `/var/tmp`: 325369335808 available bytes; 81.85% used; 112498452 free inodes.

server1 `/mnt/raid5`: 484981153792 available bytes; 97.78% used; 337732366 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40859385856 available bytes; 97.72% used; 110431270 free inodes.

server2 `/home`: 40859385856 available bytes; 97.72% used; 110431270 free inodes.

server2 `/tmp`: 40859385856 available bytes; 97.72% used; 110431270 free inodes.

server2 `/var/tmp`: 40859385856 available bytes; 97.72% used; 110431270 free inodes.

server2 `/mnt/raid5`: 507177472000 available bytes; 96.50% used; 445198145 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292289859584 available bytes; 83.69% used; 114187179 free inodes.

server3 `/home`: 292289859584 available bytes; 83.69% used; 114187179 free inodes.

server3 `/data`: 39687163904 available bytes; 99.45% used; 225844832 free inodes.

server3 `/tmp`: 292289859584 available bytes; 83.69% used; 114187179 free inodes.

server3 `/var/tmp`: 292289859584 available bytes; 83.69% used; 114187179 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105988096000 available bytes; 94.09% used; 114349625 free inodes.

server4 `/home`: 105988096000 available bytes; 94.09% used; 114349625 free inodes.

server4 `/data`: 289708683264 available bytes; 96.00% used; 225386852 free inodes.

server4 `/tmp`: 105988096000 available bytes; 94.09% used; 114349625 free inodes.

server4 `/var/tmp`: 105988096000 available bytes; 94.09% used; 114349625 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
