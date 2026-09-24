# V2R cluster inventory

2026-09-24T05:09:05.170957+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324596293632 available bytes; 81.89% used; 112492580 free inodes.

server1 `/home`: 324596293632 available bytes; 81.89% used; 112492580 free inodes.

server1 `/tmp`: 324596293632 available bytes; 81.89% used; 112492580 free inodes.

server1 `/var/tmp`: 324596293632 available bytes; 81.89% used; 112492580 free inodes.

server1 `/mnt/raid5`: 494059585536 available bytes; 97.73% used; 337724552 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40756396032 available bytes; 97.73% used; 110430374 free inodes.

server2 `/home`: 40756396032 available bytes; 97.73% used; 110430374 free inodes.

server2 `/tmp`: 40756396032 available bytes; 97.73% used; 110430374 free inodes.

server2 `/var/tmp`: 40756396032 available bytes; 97.73% used; 110430374 free inodes.

server2 `/mnt/raid5`: 523306897408 available bytes; 96.38% used; 445194670 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292396064768 available bytes; 83.68% used; 114200260 free inodes.

server3 `/home`: 292396064768 available bytes; 83.68% used; 114200260 free inodes.

server3 `/data`: 23289352192 available bytes; 99.68% used; 225840272 free inodes.

server3 `/tmp`: 292396064768 available bytes; 83.68% used; 114200260 free inodes.

server3 `/var/tmp`: 292396064768 available bytes; 83.68% used; 114200260 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105826545664 available bytes; 94.09% used; 114349379 free inodes.

server4 `/home`: 105826545664 available bytes; 94.09% used; 114349379 free inodes.

server4 `/data`: 252613095424 available bytes; 96.51% used; 225366768 free inodes.

server4 `/tmp`: 105826545664 available bytes; 94.09% used; 114349379 free inodes.

server4 `/var/tmp`: 105826545664 available bytes; 94.09% used; 114349379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
