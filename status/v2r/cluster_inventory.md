# V2R cluster inventory

2026-09-24T11:19:45.466223+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324363223040 available bytes; 81.90% used; 112488916 free inodes.

server1 `/home`: 324363223040 available bytes; 81.90% used; 112488916 free inodes.

server1 `/tmp`: 324363223040 available bytes; 81.90% used; 112488916 free inodes.

server1 `/var/tmp`: 324363223040 available bytes; 81.90% used; 112488916 free inodes.

server1 `/mnt/raid5`: 459588263936 available bytes; 97.89% used; 337690521 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57675137024 available bytes; 96.78% used; 110430104 free inodes.

server2 `/home`: 57675137024 available bytes; 96.78% used; 110430104 free inodes.

server2 `/tmp`: 57675137024 available bytes; 96.78% used; 110430104 free inodes.

server2 `/var/tmp`: 57675137024 available bytes; 96.78% used; 110430104 free inodes.

server2 `/mnt/raid5`: 510952062976 available bytes; 96.47% used; 445173773 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85763043328 available bytes; 95.21% used; 114197404 free inodes.

server3 `/home`: 85763043328 available bytes; 95.21% used; 114197404 free inodes.

server3 `/data`: 163880284160 available bytes; 97.74% used; 225816854 free inodes.

server3 `/tmp`: 85763043328 available bytes; 95.21% used; 114197404 free inodes.

server3 `/var/tmp`: 85763043328 available bytes; 95.21% used; 114197404 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105731330048 available bytes; 94.10% used; 114348881 free inodes.

server4 `/home`: 105731330048 available bytes; 94.10% used; 114348881 free inodes.

server4 `/data`: 115648835584 available bytes; 98.40% used; 225258108 free inodes.

server4 `/tmp`: 105731330048 available bytes; 94.10% used; 114348881 free inodes.

server4 `/var/tmp`: 105731330048 available bytes; 94.10% used; 114348881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
