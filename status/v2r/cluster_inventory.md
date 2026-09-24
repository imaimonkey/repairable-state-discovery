# V2R cluster inventory

2026-09-24T05:56:15.170482+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324533526528 available bytes; 81.90% used; 112491996 free inodes.

server1 `/home`: 324533526528 available bytes; 81.90% used; 112491996 free inodes.

server1 `/tmp`: 324533526528 available bytes; 81.90% used; 112491996 free inodes.

server1 `/var/tmp`: 324533526528 available bytes; 81.90% used; 112491996 free inodes.

server1 `/mnt/raid5`: 517605072896 available bytes; 97.63% used; 337723860 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57905033216 available bytes; 96.77% used; 110431304 free inodes.

server2 `/home`: 57905033216 available bytes; 96.77% used; 110431304 free inodes.

server2 `/tmp`: 57905033216 available bytes; 96.77% used; 110431304 free inodes.

server2 `/var/tmp`: 57905033216 available bytes; 96.77% used; 110431304 free inodes.

server2 `/mnt/raid5`: 521287278592 available bytes; 96.40% used; 445192984 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127195447296 available bytes; 92.90% used; 114198810 free inodes.

server3 `/home`: 127195447296 available bytes; 92.90% used; 114198810 free inodes.

server3 `/data`: 185864761344 available bytes; 97.43% used; 225838554 free inodes.

server3 `/tmp`: 127195447296 available bytes; 92.90% used; 114198810 free inodes.

server3 `/var/tmp`: 127195447296 available bytes; 92.90% used; 114198810 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105815764992 available bytes; 94.10% used; 114349341 free inodes.

server4 `/home`: 105815764992 available bytes; 94.10% used; 114349341 free inodes.

server4 `/data`: 339829641216 available bytes; 95.30% used; 225374797 free inodes.

server4 `/tmp`: 105815764992 available bytes; 94.10% used; 114349341 free inodes.

server4 `/var/tmp`: 105815764992 available bytes; 94.10% used; 114349341 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
