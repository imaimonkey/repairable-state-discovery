# V2R cluster inventory

2026-09-23T21:33:35.594276+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325717430272 available bytes; 81.83% used; 112501426 free inodes.

server1 `/home`: 325717430272 available bytes; 81.83% used; 112501426 free inodes.

server1 `/tmp`: 325717430272 available bytes; 81.83% used; 112501426 free inodes.

server1 `/var/tmp`: 325717430272 available bytes; 81.83% used; 112501426 free inodes.

server1 `/mnt/raid5`: 1385837359104 available bytes; 93.64% used; 337739941 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41120751616 available bytes; 97.71% used; 110432687 free inodes.

server2 `/home`: 41120751616 available bytes; 97.71% used; 110432687 free inodes.

server2 `/tmp`: 41120751616 available bytes; 97.71% used; 110432687 free inodes.

server2 `/var/tmp`: 41120751616 available bytes; 97.71% used; 110432687 free inodes.

server2 `/mnt/raid5`: 538419908608 available bytes; 96.28% used; 445208875 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293245722624 available bytes; 83.64% used; 114229089 free inodes.

server3 `/home`: 293245722624 available bytes; 83.64% used; 114229089 free inodes.

server3 `/data`: 52272619520 available bytes; 99.28% used; 225848699 free inodes.

server3 `/tmp`: 293245722624 available bytes; 83.64% used; 114229089 free inodes.

server3 `/var/tmp`: 293245722624 available bytes; 83.64% used; 114229089 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106478563328 available bytes; 94.06% used; 114355994 free inodes.

server4 `/home`: 106478563328 available bytes; 94.06% used; 114355994 free inodes.

server4 `/data`: 300293636096 available bytes; 95.85% used; 225450206 free inodes.

server4 `/tmp`: 106478563328 available bytes; 94.06% used; 114355994 free inodes.

server4 `/var/tmp`: 106478563328 available bytes; 94.06% used; 114355994 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
