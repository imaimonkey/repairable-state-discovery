# V2R cluster inventory

2026-09-24T16:45:39.912906+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324025016320 available bytes; 81.92% used; 112481460 free inodes.

server1 `/home`: 324025016320 available bytes; 81.92% used; 112481460 free inodes.

server1 `/tmp`: 324025016320 available bytes; 81.92% used; 112481460 free inodes.

server1 `/var/tmp`: 324025016320 available bytes; 81.92% used; 112481460 free inodes.

server1 `/mnt/raid5`: 416539365376 available bytes; 98.09% used; 337651565 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57084801024 available bytes; 96.82% used; 110418180 free inodes.

server2 `/home`: 57084801024 available bytes; 96.82% used; 110418180 free inodes.

server2 `/tmp`: 57084801024 available bytes; 96.82% used; 110418180 free inodes.

server2 `/var/tmp`: 57084801024 available bytes; 96.82% used; 110418180 free inodes.

server2 `/mnt/raid5`: 500474736640 available bytes; 96.54% used; 445164209 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84263940096 available bytes; 95.30% used; 114151522 free inodes.

server3 `/home`: 84263940096 available bytes; 95.30% used; 114151522 free inodes.

server3 `/data`: 159251017728 available bytes; 97.80% used; 225787649 free inodes.

server3 `/tmp`: 84263940096 available bytes; 95.30% used; 114151522 free inodes.

server3 `/var/tmp`: 84263940096 available bytes; 95.30% used; 114151522 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682980864 available bytes; 94.10% used; 114348574 free inodes.

server4 `/home`: 105682980864 available bytes; 94.10% used; 114348574 free inodes.

server4 `/data`: 89239158784 available bytes; 98.77% used; 225255394 free inodes.

server4 `/tmp`: 105682980864 available bytes; 94.10% used; 114348574 free inodes.

server4 `/var/tmp`: 105682980864 available bytes; 94.10% used; 114348574 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
