# V2R cluster inventory

2026-09-24T11:11:53.337287+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324367409152 available bytes; 81.90% used; 112488968 free inodes.

server1 `/home`: 324367409152 available bytes; 81.90% used; 112488968 free inodes.

server1 `/tmp`: 324367409152 available bytes; 81.90% used; 112488968 free inodes.

server1 `/var/tmp`: 324367409152 available bytes; 81.90% used; 112488968 free inodes.

server1 `/mnt/raid5`: 471805300736 available bytes; 97.84% used; 337691925 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57682923520 available bytes; 96.78% used; 110430179 free inodes.

server2 `/home`: 57682923520 available bytes; 96.78% used; 110430179 free inodes.

server2 `/tmp`: 57682923520 available bytes; 96.78% used; 110430179 free inodes.

server2 `/var/tmp`: 57682923520 available bytes; 96.78% used; 110430179 free inodes.

server2 `/mnt/raid5`: 511208280064 available bytes; 96.47% used; 445174155 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85763977216 available bytes; 95.21% used; 114198711 free inodes.

server3 `/home`: 85763977216 available bytes; 95.21% used; 114198711 free inodes.

server3 `/data`: 163933921280 available bytes; 97.73% used; 225817004 free inodes.

server3 `/tmp`: 85763977216 available bytes; 95.21% used; 114198711 free inodes.

server3 `/var/tmp`: 85763977216 available bytes; 95.21% used; 114198711 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105732546560 available bytes; 94.10% used; 114348912 free inodes.

server4 `/home`: 105732546560 available bytes; 94.10% used; 114348912 free inodes.

server4 `/data`: 115726987264 available bytes; 98.40% used; 225258167 free inodes.

server4 `/tmp`: 105732546560 available bytes; 94.10% used; 114348912 free inodes.

server4 `/var/tmp`: 105732546560 available bytes; 94.10% used; 114348912 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
