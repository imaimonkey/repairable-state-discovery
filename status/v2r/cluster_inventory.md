# V2R cluster inventory

2026-09-24T06:00:56.538054+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324531331072 available bytes; 81.90% used; 112491948 free inodes.

server1 `/home`: 324531331072 available bytes; 81.90% used; 112491948 free inodes.

server1 `/tmp`: 324531331072 available bytes; 81.90% used; 112491948 free inodes.

server1 `/var/tmp`: 324531331072 available bytes; 81.90% used; 112491948 free inodes.

server1 `/mnt/raid5`: 517600980992 available bytes; 97.63% used; 337723838 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57903984640 available bytes; 96.77% used; 110431294 free inodes.

server2 `/home`: 57903984640 available bytes; 96.77% used; 110431294 free inodes.

server2 `/tmp`: 57903984640 available bytes; 96.77% used; 110431294 free inodes.

server2 `/var/tmp`: 57903984640 available bytes; 96.77% used; 110431294 free inodes.

server2 `/mnt/raid5`: 521141489664 available bytes; 96.40% used; 445192826 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127217999872 available bytes; 92.90% used; 114200478 free inodes.

server3 `/home`: 127217999872 available bytes; 92.90% used; 114200478 free inodes.

server3 `/data`: 185849593856 available bytes; 97.43% used; 225838470 free inodes.

server3 `/tmp`: 127217999872 available bytes; 92.90% used; 114200478 free inodes.

server3 `/var/tmp`: 127217999872 available bytes; 92.90% used; 114200478 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105815351296 available bytes; 94.10% used; 114349323 free inodes.

server4 `/home`: 105815351296 available bytes; 94.10% used; 114349323 free inodes.

server4 `/data`: 339824209920 available bytes; 95.30% used; 225374709 free inodes.

server4 `/tmp`: 105815351296 available bytes; 94.10% used; 114349323 free inodes.

server4 `/var/tmp`: 105815351296 available bytes; 94.10% used; 114349323 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
