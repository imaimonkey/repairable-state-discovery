# V2R cluster inventory

2026-09-24T01:51:27.030159+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325453225984 available bytes; 81.84% used; 112499425 free inodes.

server1 `/home`: 325453225984 available bytes; 81.84% used; 112499425 free inodes.

server1 `/tmp`: 325453225984 available bytes; 81.84% used; 112499425 free inodes.

server1 `/var/tmp`: 325453225984 available bytes; 81.84% used; 112499425 free inodes.

server1 `/mnt/raid5`: 808680296448 available bytes; 96.29% used; 337733757 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40923058176 available bytes; 97.72% used; 110431831 free inodes.

server2 `/home`: 40923058176 available bytes; 97.72% used; 110431831 free inodes.

server2 `/tmp`: 40923058176 available bytes; 97.72% used; 110431831 free inodes.

server2 `/var/tmp`: 40923058176 available bytes; 97.72% used; 110431831 free inodes.

server2 `/mnt/raid5`: 530217582592 available bytes; 96.34% used; 445200941 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292714905600 available bytes; 83.67% used; 114210701 free inodes.

server3 `/home`: 292714905600 available bytes; 83.67% used; 114210701 free inodes.

server3 `/data`: 60688166912 available bytes; 99.16% used; 225841852 free inodes.

server3 `/tmp`: 292714905600 available bytes; 83.67% used; 114210701 free inodes.

server3 `/var/tmp`: 292714905600 available bytes; 83.67% used; 114210701 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105949147136 available bytes; 94.09% used; 114348540 free inodes.

server4 `/home`: 105949147136 available bytes; 94.09% used; 114348540 free inodes.

server4 `/data`: 289770876928 available bytes; 96.00% used; 225388493 free inodes.

server4 `/tmp`: 105949147136 available bytes; 94.09% used; 114348540 free inodes.

server4 `/var/tmp`: 105949147136 available bytes; 94.09% used; 114348540 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
