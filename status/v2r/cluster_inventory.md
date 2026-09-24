# V2R cluster inventory

2026-09-24T06:21:07.889898+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324512186368 available bytes; 81.90% used; 112491736 free inodes.

server1 `/home`: 324512186368 available bytes; 81.90% used; 112491736 free inodes.

server1 `/tmp`: 324512186368 available bytes; 81.90% used; 112491736 free inodes.

server1 `/var/tmp`: 324512186368 available bytes; 81.90% used; 112491736 free inodes.

server1 `/mnt/raid5`: 517575086080 available bytes; 97.63% used; 337723764 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57885716480 available bytes; 96.77% used; 110431229 free inodes.

server2 `/home`: 57885716480 available bytes; 96.77% used; 110431229 free inodes.

server2 `/tmp`: 57885716480 available bytes; 96.77% used; 110431229 free inodes.

server2 `/var/tmp`: 57885716480 available bytes; 96.77% used; 110431229 free inodes.

server2 `/mnt/raid5`: 520532008960 available bytes; 96.40% used; 445192438 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127167242240 available bytes; 92.90% used; 114196692 free inodes.

server3 `/home`: 127167242240 available bytes; 92.90% used; 114196692 free inodes.

server3 `/data`: 140581462016 available bytes; 98.06% used; 225835929 free inodes.

server3 `/tmp`: 127167242240 available bytes; 92.90% used; 114196692 free inodes.

server3 `/var/tmp`: 127167242240 available bytes; 92.90% used; 114196692 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105805905920 available bytes; 94.10% used; 114349291 free inodes.

server4 `/home`: 105805905920 available bytes; 94.10% used; 114349291 free inodes.

server4 `/data`: 334779330560 available bytes; 95.37% used; 225373538 free inodes.

server4 `/tmp`: 105805905920 available bytes; 94.10% used; 114349291 free inodes.

server4 `/var/tmp`: 105805905920 available bytes; 94.10% used; 114349291 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
