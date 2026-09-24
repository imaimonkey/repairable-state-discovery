# V2R cluster inventory

2026-09-24T03:15:08.385127+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325364658176 available bytes; 81.85% used; 112498308 free inodes.

server1 `/home`: 325364658176 available bytes; 81.85% used; 112498308 free inodes.

server1 `/tmp`: 325364658176 available bytes; 81.85% used; 112498308 free inodes.

server1 `/var/tmp`: 325364658176 available bytes; 81.85% used; 112498308 free inodes.

server1 `/mnt/raid5`: 456998494208 available bytes; 97.90% used; 337732187 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40847495168 available bytes; 97.72% used; 110431209 free inodes.

server2 `/home`: 40847495168 available bytes; 97.72% used; 110431209 free inodes.

server2 `/tmp`: 40847495168 available bytes; 97.72% used; 110431209 free inodes.

server2 `/var/tmp`: 40847495168 available bytes; 97.72% used; 110431209 free inodes.

server2 `/mnt/raid5`: 527607017472 available bytes; 96.35% used; 445197989 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292293066752 available bytes; 83.69% used; 114187092 free inodes.

server3 `/home`: 292293066752 available bytes; 83.69% used; 114187092 free inodes.

server3 `/data`: 39677136896 available bytes; 99.45% used; 225844700 free inodes.

server3 `/tmp`: 292293066752 available bytes; 83.69% used; 114187092 free inodes.

server3 `/var/tmp`: 292293066752 available bytes; 83.69% used; 114187092 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105987735552 available bytes; 94.09% used; 114349617 free inodes.

server4 `/home`: 105987735552 available bytes; 94.09% used; 114349617 free inodes.

server4 `/data`: 289661714432 available bytes; 96.00% used; 225386644 free inodes.

server4 `/tmp`: 105987735552 available bytes; 94.09% used; 114349617 free inodes.

server4 `/var/tmp`: 105987735552 available bytes; 94.09% used; 114349617 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
