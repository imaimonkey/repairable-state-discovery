# V2R cluster inventory

2026-09-25T01:54:58.361929+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319024902144 available bytes; 82.20% used; 112480595 free inodes.

server1 `/home`: 319024902144 available bytes; 82.20% used; 112480595 free inodes.

server1 `/tmp`: 319024902144 available bytes; 82.20% used; 112480595 free inodes.

server1 `/var/tmp`: 319024902144 available bytes; 82.20% used; 112480595 free inodes.

server1 `/mnt/raid5`: 416435843072 available bytes; 98.09% used; 337610051 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23040757760 available bytes; 98.71% used; 110410744 free inodes.

server2 `/home`: 23040757760 available bytes; 98.71% used; 110410744 free inodes.

server2 `/tmp`: 23040757760 available bytes; 98.71% used; 110410744 free inodes.

server2 `/var/tmp`: 23040757760 available bytes; 98.71% used; 110410744 free inodes.

server2 `/mnt/raid5`: 493826875392 available bytes; 96.59% used; 445160775 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84356759552 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84356759552 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 146260529152 available bytes; 97.98% used; 225811821 free inodes.

server3 `/tmp`: 84356759552 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84356759552 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761345536 available bytes; 94.10% used; 114348267 free inodes.

server4 `/home`: 105761345536 available bytes; 94.10% used; 114348267 free inodes.

server4 `/data`: 51707232256 available bytes; 99.29% used; 225030467 free inodes.

server4 `/tmp`: 105761345536 available bytes; 94.10% used; 114348267 free inodes.

server4 `/var/tmp`: 105761345536 available bytes; 94.10% used; 114348267 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
