# V2R cluster inventory

2026-09-25T12:57:21.179424+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319110406144 available bytes; 82.20% used; 112477580 free inodes.

server1 `/home`: 319110406144 available bytes; 82.20% used; 112477580 free inodes.

server1 `/tmp`: 319110406144 available bytes; 82.20% used; 112477580 free inodes.

server1 `/var/tmp`: 319110406144 available bytes; 82.20% used; 112477580 free inodes.

server1 `/mnt/raid5`: 371226390528 available bytes; 98.30% used; 337548068 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 8305250304 available bytes; 99.54% used; 110408780 free inodes.

server2 `/home`: 8305250304 available bytes; 99.54% used; 110408780 free inodes.

server2 `/tmp`: 8305250304 available bytes; 99.54% used; 110408780 free inodes.

server2 `/var/tmp`: 8305250304 available bytes; 99.54% used; 110408780 free inodes.

server2 `/mnt/raid5`: 324420661248 available bytes; 97.76% used; 445078028 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84207706112 available bytes; 95.30% used; 114154974 free inodes.

server3 `/home`: 84207706112 available bytes; 95.30% used; 114154974 free inodes.

server3 `/data`: 142271725568 available bytes; 98.03% used; 225810754 free inodes.

server3 `/tmp`: 84207706112 available bytes; 95.30% used; 114154974 free inodes.

server3 `/var/tmp`: 84207706112 available bytes; 95.30% used; 114154974 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105665277952 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665277952 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 232003895296 available bytes; 96.79% used; 224960524 free inodes.

server4 `/tmp`: 105665277952 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665277952 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
