# V2R cluster inventory

2026-09-24T08:09:57.329180+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324408782848 available bytes; 81.90% used; 112490668 free inodes.

server1 `/home`: 324408782848 available bytes; 81.90% used; 112490668 free inodes.

server1 `/tmp`: 324408782848 available bytes; 81.90% used; 112490668 free inodes.

server1 `/var/tmp`: 324408782848 available bytes; 81.90% used; 112490668 free inodes.

server1 `/mnt/raid5`: 496661815296 available bytes; 97.72% used; 337721387 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57818038272 available bytes; 96.77% used; 110431046 free inodes.

server2 `/home`: 57818038272 available bytes; 96.77% used; 110431046 free inodes.

server2 `/tmp`: 57818038272 available bytes; 96.77% used; 110431046 free inodes.

server2 `/var/tmp`: 57818038272 available bytes; 96.77% used; 110431046 free inodes.

server2 `/mnt/raid5`: 516507693056 available bytes; 96.43% used; 445180228 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85483769856 available bytes; 95.23% used; 114175168 free inodes.

server3 `/home`: 85483769856 available bytes; 95.23% used; 114175168 free inodes.

server3 `/data`: 176651218944 available bytes; 97.56% used; 225838280 free inodes.

server3 `/tmp`: 85483769856 available bytes; 95.23% used; 114175168 free inodes.

server3 `/var/tmp`: 85483769856 available bytes; 95.23% used; 114175168 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778786304 available bytes; 94.10% used; 114349157 free inodes.

server4 `/home`: 105778786304 available bytes; 94.10% used; 114349157 free inodes.

server4 `/data`: 284223967232 available bytes; 96.07% used; 225365829 free inodes.

server4 `/tmp`: 105778786304 available bytes; 94.10% used; 114349157 free inodes.

server4 `/var/tmp`: 105778786304 available bytes; 94.10% used; 114349157 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
