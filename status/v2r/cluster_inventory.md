# V2R cluster inventory

2026-09-26T02:34:02.297649+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318419402752 available bytes; 82.24% used; 112476274 free inodes.

server1 `/home`: 318419402752 available bytes; 82.24% used; 112476274 free inodes.

server1 `/tmp`: 318419402752 available bytes; 82.24% used; 112476274 free inodes.

server1 `/var/tmp`: 318419402752 available bytes; 82.24% used; 112476274 free inodes.

server1 `/mnt/raid5`: 339388481536 available bytes; 98.44% used; 337546126 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22943125504 available bytes; 98.72% used; 110406222 free inodes.

server2 `/home`: 22943125504 available bytes; 98.72% used; 110406222 free inodes.

server2 `/tmp`: 22943125504 available bytes; 98.72% used; 110406222 free inodes.

server2 `/var/tmp`: 22943125504 available bytes; 98.72% used; 110406222 free inodes.

server2 `/mnt/raid5`: 288323792896 available bytes; 98.01% used; 445054252 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84317093888 available bytes; 95.29% used; 114152372 free inodes.

server3 `/home`: 84317093888 available bytes; 95.29% used; 114152372 free inodes.

server3 `/data`: 124787314688 available bytes; 98.28% used; 225816912 free inodes.

server3 `/tmp`: 84317093888 available bytes; 95.29% used; 114152372 free inodes.

server3 `/var/tmp`: 84317093888 available bytes; 95.29% used; 114152372 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106126532608 available bytes; 94.08% used; 114349420 free inodes.

server4 `/home`: 106126532608 available bytes; 94.08% used; 114349420 free inodes.

server4 `/data`: 123759919104 available bytes; 98.29% used; 224915657 free inodes.

server4 `/tmp`: 106126532608 available bytes; 94.08% used; 114349420 free inodes.

server4 `/var/tmp`: 106126532608 available bytes; 94.08% used; 114349420 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
