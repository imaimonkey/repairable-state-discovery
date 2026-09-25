# V2R cluster inventory

2026-09-25T10:44:02.247185+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318989922304 available bytes; 82.20% used; 112479395 free inodes.

server1 `/home`: 318989922304 available bytes; 82.20% used; 112479395 free inodes.

server1 `/tmp`: 318989922304 available bytes; 82.20% used; 112479395 free inodes.

server1 `/var/tmp`: 318989922304 available bytes; 82.20% used; 112479395 free inodes.

server1 `/mnt/raid5`: 364830257152 available bytes; 98.33% used; 337555265 free inodes.
| server2 | True | ['0', '2', '3', '5', '6'] | [] |

server2 `/`: 22907727872 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22907727872 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22907727872 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22907727872 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 308926849024 available bytes; 97.87% used; 445089477 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84421783552 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84421783552 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142004764672 available bytes; 98.04% used; 225815496 free inodes.

server3 `/tmp`: 84421783552 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84421783552 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105612955648 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612955648 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238510727168 available bytes; 96.70% used; 224985796 free inodes.

server4 `/tmp`: 105612955648 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612955648 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
