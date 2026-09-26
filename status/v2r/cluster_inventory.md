# V2R cluster inventory

2026-09-26T03:58:06.165624+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318414508032 available bytes; 82.24% used; 112476261 free inodes.

server1 `/home`: 318414508032 available bytes; 82.24% used; 112476261 free inodes.

server1 `/tmp`: 318414508032 available bytes; 82.24% used; 112476261 free inodes.

server1 `/var/tmp`: 318414508032 available bytes; 82.24% used; 112476261 free inodes.

server1 `/mnt/raid5`: 330952900608 available bytes; 98.48% used; 337545658 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22931496960 available bytes; 98.72% used; 110406194 free inodes.

server2 `/home`: 22931496960 available bytes; 98.72% used; 110406194 free inodes.

server2 `/tmp`: 22931496960 available bytes; 98.72% used; 110406194 free inodes.

server2 `/var/tmp`: 22931496960 available bytes; 98.72% used; 110406194 free inodes.

server2 `/mnt/raid5`: 286437289984 available bytes; 98.02% used; 445051698 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84674318336 available bytes; 95.27% used; 114177998 free inodes.

server3 `/home`: 84674318336 available bytes; 95.27% used; 114177998 free inodes.

server3 `/data`: 124602695680 available bytes; 98.28% used; 225820456 free inodes.

server3 `/tmp`: 84674318336 available bytes; 95.27% used; 114177998 free inodes.

server3 `/var/tmp`: 84674318336 available bytes; 95.27% used; 114177998 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105851064320 available bytes; 94.09% used; 114347416 free inodes.

server4 `/home`: 105851064320 available bytes; 94.09% used; 114347416 free inodes.

server4 `/data`: 109775712256 available bytes; 98.48% used; 224929551 free inodes.

server4 `/tmp`: 105851064320 available bytes; 94.09% used; 114347416 free inodes.

server4 `/var/tmp`: 105851064320 available bytes; 94.09% used; 114347416 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
