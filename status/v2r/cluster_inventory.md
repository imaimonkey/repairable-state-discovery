# V2R cluster inventory

2026-09-25T04:02:45.994879+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318930841600 available bytes; 82.21% used; 112480371 free inodes.

server1 `/home`: 318930841600 available bytes; 82.21% used; 112480371 free inodes.

server1 `/tmp`: 318930841600 available bytes; 82.21% used; 112480371 free inodes.

server1 `/var/tmp`: 318930841600 available bytes; 82.21% used; 112480371 free inodes.

server1 `/mnt/raid5`: 395050737664 available bytes; 98.19% used; 337595008 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22964166656 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 22964166656 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 22964166656 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 22964166656 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 463877152768 available bytes; 96.79% used; 445110915 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342136832 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84342136832 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 144060649472 available bytes; 98.01% used; 225816700 free inodes.

server3 `/tmp`: 84342136832 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84342136832 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105682784256 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105682784256 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 36914372608 available bytes; 99.49% used; 224964382 free inodes.

server4 `/tmp`: 105682784256 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105682784256 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
