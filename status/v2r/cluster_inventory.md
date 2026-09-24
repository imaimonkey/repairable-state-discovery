# V2R cluster inventory

2026-09-24T05:26:20.936410+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324555218944 available bytes; 81.89% used; 112492408 free inodes.

server1 `/home`: 324555218944 available bytes; 81.89% used; 112492408 free inodes.

server1 `/tmp`: 324555218944 available bytes; 81.89% used; 112492408 free inodes.

server1 `/var/tmp`: 324555218944 available bytes; 81.89% used; 112492408 free inodes.

server1 `/mnt/raid5`: 513336500224 available bytes; 97.65% used; 337724317 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57169543168 available bytes; 96.81% used; 110431201 free inodes.

server2 `/home`: 57169543168 available bytes; 96.81% used; 110431201 free inodes.

server2 `/tmp`: 57169543168 available bytes; 96.81% used; 110431201 free inodes.

server2 `/var/tmp`: 57169543168 available bytes; 96.81% used; 110431201 free inodes.

server2 `/mnt/raid5`: 521963094016 available bytes; 96.39% used; 445193859 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 260703055872 available bytes; 85.45% used; 114199646 free inodes.

server3 `/home`: 260702990336 available bytes; 85.45% used; 114199646 free inodes.

server3 `/data`: 41792929792 available bytes; 99.42% used; 225839704 free inodes.

server3 `/tmp`: 260702928896 available bytes; 85.45% used; 114199646 free inodes.

server3 `/var/tmp`: 260702900224 available bytes; 85.45% used; 114199646 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105817255936 available bytes; 94.10% used; 114349367 free inodes.

server4 `/home`: 105817255936 available bytes; 94.10% used; 114349367 free inodes.

server4 `/data`: 252566167552 available bytes; 96.51% used; 225366530 free inodes.

server4 `/tmp`: 105817255936 available bytes; 94.10% used; 114349367 free inodes.

server4 `/var/tmp`: 105817255936 available bytes; 94.10% used; 114349367 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
