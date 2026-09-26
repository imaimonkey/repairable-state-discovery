# V2R cluster inventory

2026-09-26T00:13:28.143236+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318669762560 available bytes; 82.22% used; 112476305 free inodes.

server1 `/home`: 318669762560 available bytes; 82.22% used; 112476305 free inodes.

server1 `/tmp`: 318669762560 available bytes; 82.22% used; 112476305 free inodes.

server1 `/var/tmp`: 318669762560 available bytes; 82.22% used; 112476305 free inodes.

server1 `/mnt/raid5`: 359568408576 available bytes; 98.35% used; 337547056 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22948720640 available bytes; 98.72% used; 110406222 free inodes.

server2 `/home`: 22948720640 available bytes; 98.72% used; 110406222 free inodes.

server2 `/tmp`: 22948720640 available bytes; 98.72% used; 110406222 free inodes.

server2 `/var/tmp`: 22948720640 available bytes; 98.72% used; 110406222 free inodes.

server2 `/mnt/raid5`: 285170159616 available bytes; 98.03% used; 445058667 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342071296 available bytes; 95.29% used; 114152433 free inodes.

server3 `/home`: 84342071296 available bytes; 95.29% used; 114152433 free inodes.

server3 `/data`: 124947697664 available bytes; 98.27% used; 225819327 free inodes.

server3 `/tmp`: 84342071296 available bytes; 95.29% used; 114152433 free inodes.

server3 `/var/tmp`: 84342071296 available bytes; 95.29% used; 114152433 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453760512 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105453760512 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178051219456 available bytes; 97.54% used; 224917560 free inodes.

server4 `/tmp`: 105453760512 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105453760512 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
