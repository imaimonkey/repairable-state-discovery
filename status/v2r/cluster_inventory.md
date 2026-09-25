# V2R cluster inventory

2026-09-25T04:01:13.739417+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318930358272 available bytes; 82.21% used; 112480366 free inodes.

server1 `/home`: 318930358272 available bytes; 82.21% used; 112480366 free inodes.

server1 `/tmp`: 318930358272 available bytes; 82.21% used; 112480366 free inodes.

server1 `/var/tmp`: 318930358272 available bytes; 82.21% used; 112480366 free inodes.

server1 `/mnt/raid5`: 395050459136 available bytes; 98.19% used; 337595183 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22963191808 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22963191808 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22963191808 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22963191808 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 463920869376 available bytes; 96.79% used; 445111064 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341514240 available bytes; 95.29% used; 114156070 free inodes.

server3 `/home`: 84341514240 available bytes; 95.29% used; 114156070 free inodes.

server3 `/data`: 144086188032 available bytes; 98.01% used; 225816753 free inodes.

server3 `/tmp`: 84341514240 available bytes; 95.29% used; 114156070 free inodes.

server3 `/var/tmp`: 84341514240 available bytes; 95.29% used; 114156070 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105682833408 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105682833408 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 36918583296 available bytes; 99.49% used; 224964442 free inodes.

server4 `/tmp`: 105682833408 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105682833408 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
