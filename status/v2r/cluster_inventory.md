# V2R cluster inventory

2026-09-26T03:56:34.489955+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318414733312 available bytes; 82.24% used; 112476261 free inodes.

server1 `/home`: 318414733312 available bytes; 82.24% used; 112476261 free inodes.

server1 `/tmp`: 318414733312 available bytes; 82.24% used; 112476261 free inodes.

server1 `/var/tmp`: 318414733312 available bytes; 82.24% used; 112476261 free inodes.

server1 `/mnt/raid5`: 330966106112 available bytes; 98.48% used; 337545689 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22931730432 available bytes; 98.72% used; 110406194 free inodes.

server2 `/home`: 22931730432 available bytes; 98.72% used; 110406194 free inodes.

server2 `/tmp`: 22931730432 available bytes; 98.72% used; 110406194 free inodes.

server2 `/var/tmp`: 22931730432 available bytes; 98.72% used; 110406194 free inodes.

server2 `/mnt/raid5`: 286465662976 available bytes; 98.02% used; 445051412 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84674256896 available bytes; 95.27% used; 114177991 free inodes.

server3 `/home`: 84674256896 available bytes; 95.27% used; 114177991 free inodes.

server3 `/data`: 124605407232 available bytes; 98.28% used; 225820470 free inodes.

server3 `/tmp`: 84674256896 available bytes; 95.27% used; 114177991 free inodes.

server3 `/var/tmp`: 84674256896 available bytes; 95.27% used; 114177991 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105851117568 available bytes; 94.09% used; 114347416 free inodes.

server4 `/home`: 105851117568 available bytes; 94.09% used; 114347416 free inodes.

server4 `/data`: 109778333696 available bytes; 98.48% used; 224929551 free inodes.

server4 `/tmp`: 105851117568 available bytes; 94.09% used; 114347416 free inodes.

server4 `/var/tmp`: 105851117568 available bytes; 94.09% used; 114347416 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
