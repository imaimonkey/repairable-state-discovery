# V2R cluster inventory

2026-09-25T03:59:40.669666+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318930554880 available bytes; 82.21% used; 112480368 free inodes.

server1 `/home`: 318930554880 available bytes; 82.21% used; 112480368 free inodes.

server1 `/tmp`: 318930554880 available bytes; 82.21% used; 112480368 free inodes.

server1 `/var/tmp`: 318930554880 available bytes; 82.21% used; 112480368 free inodes.

server1 `/mnt/raid5`: 395057385472 available bytes; 98.19% used; 337595372 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22963716096 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22963716096 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22963716096 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22963716096 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 463999631360 available bytes; 96.79% used; 445111121 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341673984 available bytes; 95.29% used; 114156070 free inodes.

server3 `/home`: 84341673984 available bytes; 95.29% used; 114156070 free inodes.

server3 `/data`: 144113524736 available bytes; 98.01% used; 225816779 free inodes.

server3 `/tmp`: 84341673984 available bytes; 95.29% used; 114156070 free inodes.

server3 `/var/tmp`: 84341673984 available bytes; 95.29% used; 114156070 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105682878464 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105682878464 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 36946841600 available bytes; 99.49% used; 224964697 free inodes.

server4 `/tmp`: 105682878464 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105682878464 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
