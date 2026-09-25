# V2R cluster inventory

2026-09-25T12:43:33.505515+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319128510464 available bytes; 82.20% used; 112477610 free inodes.

server1 `/home`: 319128510464 available bytes; 82.20% used; 112477610 free inodes.

server1 `/tmp`: 319128510464 available bytes; 82.20% used; 112477610 free inodes.

server1 `/var/tmp`: 319128510464 available bytes; 82.20% used; 112477610 free inodes.

server1 `/mnt/raid5`: 364253057024 available bytes; 98.33% used; 337548053 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 20257386496 available bytes; 98.87% used; 110409426 free inodes.

server2 `/home`: 20257386496 available bytes; 98.87% used; 110409426 free inodes.

server2 `/tmp`: 20257386496 available bytes; 98.87% used; 110409426 free inodes.

server2 `/var/tmp`: 20257386496 available bytes; 98.87% used; 110409426 free inodes.

server2 `/mnt/raid5`: 324727664640 available bytes; 97.76% used; 445078938 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84208906240 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84208906240 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142277304320 available bytes; 98.03% used; 225810998 free inodes.

server3 `/tmp`: 84208906240 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84208906240 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105665671168 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665671168 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231945773056 available bytes; 96.79% used; 224962799 free inodes.

server4 `/tmp`: 105665671168 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665671168 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
