# V2R cluster inventory

2026-09-25T02:10:23.746095+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318969659392 available bytes; 82.21% used; 112480529 free inodes.

server1 `/home`: 318969659392 available bytes; 82.21% used; 112480529 free inodes.

server1 `/tmp`: 318969659392 available bytes; 82.21% used; 112480529 free inodes.

server1 `/var/tmp`: 318969659392 available bytes; 82.21% used; 112480529 free inodes.

server1 `/mnt/raid5`: 416252903424 available bytes; 98.09% used; 337608239 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23023902720 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 23023902720 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 23023902720 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 23023902720 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 483473625088 available bytes; 96.66% used; 445114352 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351352832 available bytes; 95.29% used; 114156074 free inodes.

server3 `/home`: 84351352832 available bytes; 95.29% used; 114156074 free inodes.

server3 `/data`: 145937604608 available bytes; 97.98% used; 225811537 free inodes.

server3 `/tmp`: 84351352832 available bytes; 95.29% used; 114156074 free inodes.

server3 `/var/tmp`: 84351352832 available bytes; 95.29% used; 114156074 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105752424448 available bytes; 94.10% used; 114348242 free inodes.

server4 `/home`: 105752424448 available bytes; 94.10% used; 114348242 free inodes.

server4 `/data`: 42569940992 available bytes; 99.41% used; 225013617 free inodes.

server4 `/tmp`: 105752424448 available bytes; 94.10% used; 114348242 free inodes.

server4 `/var/tmp`: 105752424448 available bytes; 94.10% used; 114348242 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
