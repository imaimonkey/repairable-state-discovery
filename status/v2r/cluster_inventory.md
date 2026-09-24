# V2R cluster inventory

2026-09-24T12:20:44.507744+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324058578944 available bytes; 81.92% used; 112481576 free inodes.

server1 `/home`: 324058578944 available bytes; 81.92% used; 112481576 free inodes.

server1 `/tmp`: 324058578944 available bytes; 81.92% used; 112481576 free inodes.

server1 `/var/tmp`: 324058578944 available bytes; 81.92% used; 112481576 free inodes.

server1 `/mnt/raid5`: 405207109632 available bytes; 98.14% used; 337683466 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57605586944 available bytes; 96.79% used; 110429500 free inodes.

server2 `/home`: 57605586944 available bytes; 96.79% used; 110429500 free inodes.

server2 `/tmp`: 57605586944 available bytes; 96.79% used; 110429500 free inodes.

server2 `/var/tmp`: 57605586944 available bytes; 96.79% used; 110429500 free inodes.

server2 `/mnt/raid5`: 508787474432 available bytes; 96.48% used; 445171967 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85319667712 available bytes; 95.24% used; 114172749 free inodes.

server3 `/home`: 85319667712 available bytes; 95.24% used; 114172749 free inodes.

server3 `/data`: 163431682048 available bytes; 97.74% used; 225814928 free inodes.

server3 `/tmp`: 85319667712 available bytes; 95.24% used; 114172749 free inodes.

server3 `/var/tmp`: 85319667712 available bytes; 95.24% used; 114172749 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105781002240 available bytes; 94.10% used; 114348801 free inodes.

server4 `/home`: 105781002240 available bytes; 94.10% used; 114348801 free inodes.

server4 `/data`: 90077147136 available bytes; 98.76% used; 225257307 free inodes.

server4 `/tmp`: 105781002240 available bytes; 94.10% used; 114348801 free inodes.

server4 `/var/tmp`: 105781002240 available bytes; 94.10% used; 114348801 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
