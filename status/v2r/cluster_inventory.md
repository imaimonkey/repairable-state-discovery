# V2R cluster inventory

2026-09-25T07:21:27.626607+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871281664 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318871281664 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318871281664 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318871281664 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 385921085440 available bytes; 98.23% used; 337558491 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22866628608 available bytes; 98.72% used; 110410500 free inodes.

server2 `/home`: 22866628608 available bytes; 98.72% used; 110410500 free inodes.

server2 `/tmp`: 22866628608 available bytes; 98.72% used; 110410500 free inodes.

server2 `/var/tmp`: 22866628608 available bytes; 98.72% used; 110410500 free inodes.

server2 `/mnt/raid5`: 343435423744 available bytes; 97.63% used; 445097724 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84446781440 available bytes; 95.29% used; 114156017 free inodes.

server3 `/home`: 84446781440 available bytes; 95.29% used; 114156017 free inodes.

server3 `/data`: 142454452224 available bytes; 98.03% used; 225812868 free inodes.

server3 `/tmp`: 84446781440 available bytes; 95.29% used; 114156017 free inodes.

server3 `/var/tmp`: 84446781440 available bytes; 95.29% used; 114156017 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638146048 available bytes; 94.11% used; 114350361 free inodes.

server4 `/home`: 105638146048 available bytes; 94.11% used; 114350361 free inodes.

server4 `/data`: 249113935872 available bytes; 96.56% used; 225015343 free inodes.

server4 `/tmp`: 105638146048 available bytes; 94.11% used; 114350361 free inodes.

server4 `/var/tmp`: 105638146048 available bytes; 94.11% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
