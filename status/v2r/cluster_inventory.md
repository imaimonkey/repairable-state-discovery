# V2R cluster inventory

2026-09-26T00:29:45.385829+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318653415424 available bytes; 82.22% used; 112476288 free inodes.

server1 `/home`: 318653415424 available bytes; 82.22% used; 112476288 free inodes.

server1 `/tmp`: 318653415424 available bytes; 82.22% used; 112476288 free inodes.

server1 `/var/tmp`: 318653415424 available bytes; 82.22% used; 112476288 free inodes.

server1 `/mnt/raid5`: 359395864576 available bytes; 98.35% used; 337546884 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22941687808 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22941687808 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22941687808 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22941687808 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 295124213760 available bytes; 97.96% used; 445058045 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84339392512 available bytes; 95.29% used; 114152443 free inodes.

server3 `/home`: 84339392512 available bytes; 95.29% used; 114152443 free inodes.

server3 `/data`: 124946468864 available bytes; 98.27% used; 225819064 free inodes.

server3 `/tmp`: 84339392512 available bytes; 95.29% used; 114152443 free inodes.

server3 `/var/tmp`: 84339392512 available bytes; 95.29% used; 114152443 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105453203456 available bytes; 94.12% used; 114348369 free inodes.

server4 `/home`: 105453203456 available bytes; 94.12% used; 114348369 free inodes.

server4 `/data`: 176289009664 available bytes; 97.56% used; 224917487 free inodes.

server4 `/tmp`: 105453203456 available bytes; 94.12% used; 114348369 free inodes.

server4 `/var/tmp`: 105453203456 available bytes; 94.12% used; 114348369 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
