# V2R cluster inventory

2026-09-24T14:14:44.657790+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324057968640 available bytes; 81.92% used; 112481453 free inodes.

server1 `/home`: 324057968640 available bytes; 81.92% used; 112481453 free inodes.

server1 `/tmp`: 324057968640 available bytes; 81.92% used; 112481453 free inodes.

server1 `/var/tmp`: 324057968640 available bytes; 81.92% used; 112481453 free inodes.

server1 `/mnt/raid5`: 416932241408 available bytes; 98.09% used; 337670002 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57475678208 available bytes; 96.79% used; 110428273 free inodes.

server2 `/home`: 57475678208 available bytes; 96.79% used; 110428273 free inodes.

server2 `/tmp`: 57475678208 available bytes; 96.79% used; 110428273 free inodes.

server2 `/var/tmp`: 57475678208 available bytes; 96.79% used; 110428273 free inodes.

server2 `/mnt/raid5`: 504974360576 available bytes; 96.51% used; 445168568 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85059866624 available bytes; 95.25% used; 114189113 free inodes.

server3 `/home`: 85059866624 available bytes; 95.25% used; 114189113 free inodes.

server3 `/data`: 161023119360 available bytes; 97.77% used; 225808983 free inodes.

server3 `/tmp`: 85059866624 available bytes; 95.25% used; 114189113 free inodes.

server3 `/var/tmp`: 85059866624 available bytes; 95.25% used; 114189113 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759547392 available bytes; 94.10% used; 114348703 free inodes.

server4 `/home`: 105759547392 available bytes; 94.10% used; 114348703 free inodes.

server4 `/data`: 69366849536 available bytes; 99.04% used; 225257076 free inodes.

server4 `/tmp`: 105759547392 available bytes; 94.10% used; 114348703 free inodes.

server4 `/var/tmp`: 105759547392 available bytes; 94.10% used; 114348703 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
