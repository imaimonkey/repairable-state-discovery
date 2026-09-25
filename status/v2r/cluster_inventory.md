# V2R cluster inventory

2026-09-25T04:05:49.869824+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318930444288 available bytes; 82.21% used; 112480380 free inodes.

server1 `/home`: 318930444288 available bytes; 82.21% used; 112480380 free inodes.

server1 `/tmp`: 318930444288 available bytes; 82.21% used; 112480380 free inodes.

server1 `/var/tmp`: 318930444288 available bytes; 82.21% used; 112480380 free inodes.

server1 `/mnt/raid5`: 395036700672 available bytes; 98.19% used; 337594625 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22963384320 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 22963384320 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 22963384320 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 22963384320 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 463798067200 available bytes; 96.80% used; 445110943 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341940224 available bytes; 95.29% used; 114156074 free inodes.

server3 `/home`: 84341940224 available bytes; 95.29% used; 114156074 free inodes.

server3 `/data`: 144008179712 available bytes; 98.01% used; 225816631 free inodes.

server3 `/tmp`: 84341940224 available bytes; 95.29% used; 114156074 free inodes.

server3 `/var/tmp`: 84341940224 available bytes; 95.29% used; 114156074 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105682706432 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105682706432 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 35307528192 available bytes; 99.51% used; 224964217 free inodes.

server4 `/tmp`: 105682706432 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105682706432 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
