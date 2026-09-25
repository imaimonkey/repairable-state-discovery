# V2R cluster inventory

2026-09-25T08:16:45.903012+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318837317632 available bytes; 82.21% used; 112480355 free inodes.

server1 `/home`: 318837317632 available bytes; 82.21% used; 112480355 free inodes.

server1 `/tmp`: 318837317632 available bytes; 82.21% used; 112480355 free inodes.

server1 `/var/tmp`: 318837317632 available bytes; 82.21% used; 112480355 free inodes.

server1 `/mnt/raid5`: 379085824000 available bytes; 98.26% used; 337557515 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22834962432 available bytes; 98.73% used; 110410482 free inodes.

server2 `/home`: 22834962432 available bytes; 98.73% used; 110410482 free inodes.

server2 `/tmp`: 22834962432 available bytes; 98.73% used; 110410482 free inodes.

server2 `/var/tmp`: 22834962432 available bytes; 98.73% used; 110410482 free inodes.

server2 `/mnt/raid5`: 333697908736 available bytes; 97.69% used; 445094916 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84439506944 available bytes; 95.29% used; 114156055 free inodes.

server3 `/home`: 84439506944 available bytes; 95.29% used; 114156055 free inodes.

server3 `/data`: 142387961856 available bytes; 98.03% used; 225811912 free inodes.

server3 `/tmp`: 84439506944 available bytes; 95.29% used; 114156055 free inodes.

server3 `/var/tmp`: 84439506944 available bytes; 95.29% used; 114156055 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105625026560 available bytes; 94.11% used; 114350334 free inodes.

server4 `/home`: 105625026560 available bytes; 94.11% used; 114350334 free inodes.

server4 `/data`: 248742674432 available bytes; 96.56% used; 225007108 free inodes.

server4 `/tmp`: 105625026560 available bytes; 94.11% used; 114350334 free inodes.

server4 `/var/tmp`: 105625026560 available bytes; 94.11% used; 114350334 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
