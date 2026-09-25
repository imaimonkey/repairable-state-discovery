# V2R cluster inventory

2026-09-25T05:01:21.754457+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318905700352 available bytes; 82.21% used; 112480341 free inodes.

server1 `/home`: 318905700352 available bytes; 82.21% used; 112480341 free inodes.

server1 `/tmp`: 318905700352 available bytes; 82.21% used; 112480341 free inodes.

server1 `/var/tmp`: 318905700352 available bytes; 82.21% used; 112480341 free inodes.

server1 `/mnt/raid5`: 408629977088 available bytes; 98.13% used; 337571939 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938284032 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22938284032 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22938284032 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22938284032 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462075019264 available bytes; 96.81% used; 445109504 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340772864 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84340772864 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 142950166528 available bytes; 98.02% used; 225815533 free inodes.

server3 `/tmp`: 84340772864 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84340772864 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105659326464 available bytes; 94.10% used; 114350405 free inodes.

server4 `/home`: 105659326464 available bytes; 94.10% used; 114350405 free inodes.

server4 `/data`: 27938541568 available bytes; 99.61% used; 224961131 free inodes.

server4 `/tmp`: 105659326464 available bytes; 94.10% used; 114350405 free inodes.

server4 `/var/tmp`: 105659326464 available bytes; 94.10% used; 114350405 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
