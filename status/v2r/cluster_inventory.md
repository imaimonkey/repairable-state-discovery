# V2R cluster inventory

2026-09-26T01:19:09.038939+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318648553472 available bytes; 82.22% used; 112476296 free inodes.

server1 `/home`: 318648553472 available bytes; 82.22% used; 112476296 free inodes.

server1 `/tmp`: 318648553472 available bytes; 82.22% used; 112476296 free inodes.

server1 `/var/tmp`: 318648553472 available bytes; 82.22% used; 112476296 free inodes.

server1 `/mnt/raid5`: 345524305920 available bytes; 98.41% used; 337546607 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22931824640 available bytes; 98.72% used; 110406204 free inodes.

server2 `/home`: 22931824640 available bytes; 98.72% used; 110406204 free inodes.

server2 `/tmp`: 22931824640 available bytes; 98.72% used; 110406204 free inodes.

server2 `/var/tmp`: 22931824640 available bytes; 98.72% used; 110406204 free inodes.

server2 `/mnt/raid5`: 291048280064 available bytes; 97.99% used; 445056446 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 84340523008 available bytes; 95.29% used; 114152442 free inodes.

server3 `/home`: 84340523008 available bytes; 95.29% used; 114152442 free inodes.

server3 `/data`: 124869103616 available bytes; 98.27% used; 225818212 free inodes.

server3 `/tmp`: 84340523008 available bytes; 95.29% used; 114152442 free inodes.

server3 `/var/tmp`: 84340523008 available bytes; 95.29% used; 114152442 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105264435200 available bytes; 94.13% used; 114347079 free inodes.

server4 `/home`: 105264435200 available bytes; 94.13% used; 114347079 free inodes.

server4 `/data`: 141690507264 available bytes; 98.04% used; 224917311 free inodes.

server4 `/tmp`: 105264435200 available bytes; 94.13% used; 114347079 free inodes.

server4 `/var/tmp`: 105264435200 available bytes; 94.13% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
