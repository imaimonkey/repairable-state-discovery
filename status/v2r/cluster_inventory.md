# V2R cluster inventory

2026-09-25T07:06:08.441842+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318873030656 available bytes; 82.21% used; 112480379 free inodes.

server1 `/home`: 318873030656 available bytes; 82.21% used; 112480379 free inodes.

server1 `/tmp`: 318873030656 available bytes; 82.21% used; 112480379 free inodes.

server1 `/var/tmp`: 318873030656 available bytes; 82.21% used; 112480379 free inodes.

server1 `/mnt/raid5`: 399691534336 available bytes; 98.17% used; 337560433 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22872305664 available bytes; 98.72% used; 110410523 free inodes.

server2 `/home`: 22872305664 available bytes; 98.72% used; 110410523 free inodes.

server2 `/tmp`: 22872305664 available bytes; 98.72% used; 110410523 free inodes.

server2 `/var/tmp`: 22872305664 available bytes; 98.72% used; 110410523 free inodes.

server2 `/mnt/raid5`: 330390904832 available bytes; 97.72% used; 445097860 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84446720000 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84446720000 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142454714368 available bytes; 98.03% used; 225813111 free inodes.

server3 `/tmp`: 84446720000 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84446720000 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638608896 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638608896 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249492606976 available bytes; 96.55% used; 225016833 free inodes.

server4 `/tmp`: 105638608896 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638608896 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
