# V2R cluster inventory

2026-09-24T23:36:17.818756+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319011729408 available bytes; 82.20% used; 112480788 free inodes.

server1 `/home`: 319011729408 available bytes; 82.20% used; 112480788 free inodes.

server1 `/tmp`: 319011729408 available bytes; 82.20% used; 112480788 free inodes.

server1 `/var/tmp`: 319011729408 available bytes; 82.20% used; 112480788 free inodes.

server1 `/mnt/raid5`: 415221202944 available bytes; 98.10% used; 337612500 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23113236480 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23113236480 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23113236480 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23113236480 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 486198370304 available bytes; 96.64% used; 445150890 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84359987200 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84359987200 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 148109197312 available bytes; 97.95% used; 225800801 free inodes.

server3 `/tmp`: 84359987200 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84359987200 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799397376 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799397376 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 61154500608 available bytes; 99.15% used; 225138371 free inodes.

server4 `/tmp`: 105799397376 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799397376 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
