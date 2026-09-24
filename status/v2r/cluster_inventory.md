# V2R cluster inventory

2026-09-24T11:51:09.422164+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324296581120 available bytes; 81.91% used; 112488514 free inodes.

server1 `/home`: 324296581120 available bytes; 81.91% used; 112488514 free inodes.

server1 `/tmp`: 324296581120 available bytes; 81.91% used; 112488514 free inodes.

server1 `/var/tmp`: 324296581120 available bytes; 81.91% used; 112488514 free inodes.

server1 `/mnt/raid5`: 419668332544 available bytes; 98.07% used; 337686780 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57638871040 available bytes; 96.78% used; 110429788 free inodes.

server2 `/home`: 57638871040 available bytes; 96.78% used; 110429788 free inodes.

server2 `/tmp`: 57638871040 available bytes; 96.78% used; 110429788 free inodes.

server2 `/var/tmp`: 57638871040 available bytes; 96.78% used; 110429788 free inodes.

server2 `/mnt/raid5`: 509987520512 available bytes; 96.48% used; 445172683 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85341302784 available bytes; 95.24% used; 114173325 free inodes.

server3 `/home`: 85341302784 available bytes; 95.24% used; 114173325 free inodes.

server3 `/data`: 163646988288 available bytes; 97.74% used; 225815854 free inodes.

server3 `/tmp`: 85341302784 available bytes; 95.24% used; 114173325 free inodes.

server3 `/var/tmp`: 85341302784 available bytes; 95.24% used; 114173325 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105727512576 available bytes; 94.10% used; 114348834 free inodes.

server4 `/home`: 105727512576 available bytes; 94.10% used; 114348834 free inodes.

server4 `/data`: 115387219968 available bytes; 98.41% used; 225257922 free inodes.

server4 `/tmp`: 105727512576 available bytes; 94.10% used; 114348834 free inodes.

server4 `/var/tmp`: 105727512576 available bytes; 94.10% used; 114348834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
