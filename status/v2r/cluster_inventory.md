# V2R cluster inventory

2026-09-24T01:52:21.907943+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325452640256 available bytes; 81.84% used; 112499421 free inodes.

server1 `/home`: 325452640256 available bytes; 81.84% used; 112499421 free inodes.

server1 `/tmp`: 325452640256 available bytes; 81.84% used; 112499421 free inodes.

server1 `/var/tmp`: 325452640256 available bytes; 81.84% used; 112499421 free inodes.

server1 `/mnt/raid5`: 805188284416 available bytes; 96.31% used; 337733714 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40923922432 available bytes; 97.72% used; 110431829 free inodes.

server2 `/home`: 40923922432 available bytes; 97.72% used; 110431829 free inodes.

server2 `/tmp`: 40923922432 available bytes; 97.72% used; 110431829 free inodes.

server2 `/var/tmp`: 40923922432 available bytes; 97.72% used; 110431829 free inodes.

server2 `/mnt/raid5`: 530176901120 available bytes; 96.34% used; 445200809 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292714721280 available bytes; 83.67% used; 114210699 free inodes.

server3 `/home`: 292714721280 available bytes; 83.67% used; 114210699 free inodes.

server3 `/data`: 60686753792 available bytes; 99.16% used; 225841830 free inodes.

server3 `/tmp`: 292714721280 available bytes; 83.67% used; 114210699 free inodes.

server3 `/var/tmp`: 292714721280 available bytes; 83.67% used; 114210699 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105948598272 available bytes; 94.09% used; 114348532 free inodes.

server4 `/home`: 105948598272 available bytes; 94.09% used; 114348532 free inodes.

server4 `/data`: 289771270144 available bytes; 96.00% used; 225388495 free inodes.

server4 `/tmp`: 105948598272 available bytes; 94.09% used; 114348532 free inodes.

server4 `/var/tmp`: 105948598272 available bytes; 94.09% used; 114348532 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
