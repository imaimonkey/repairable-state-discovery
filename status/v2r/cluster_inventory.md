# V2R cluster inventory

2026-09-24T06:05:36.046261+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324527878144 available bytes; 81.90% used; 112491899 free inodes.

server1 `/home`: 324527878144 available bytes; 81.90% used; 112491899 free inodes.

server1 `/tmp`: 324527878144 available bytes; 81.90% used; 112491899 free inodes.

server1 `/var/tmp`: 324527878144 available bytes; 81.90% used; 112491899 free inodes.

server1 `/mnt/raid5`: 517609312256 available bytes; 97.63% used; 337723817 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57896656896 available bytes; 96.77% used; 110431282 free inodes.

server2 `/home`: 57896656896 available bytes; 96.77% used; 110431282 free inodes.

server2 `/tmp`: 57896656896 available bytes; 96.77% used; 110431282 free inodes.

server2 `/var/tmp`: 57896656896 available bytes; 96.77% used; 110431282 free inodes.

server2 `/mnt/raid5`: 521012453376 available bytes; 96.40% used; 445193047 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127164084224 available bytes; 92.90% used; 114196742 free inodes.

server3 `/home`: 127164084224 available bytes; 92.90% used; 114196742 free inodes.

server3 `/data`: 185834663936 available bytes; 97.43% used; 225838378 free inodes.

server3 `/tmp`: 127164084224 available bytes; 92.90% used; 114196742 free inodes.

server3 `/var/tmp`: 127164084224 available bytes; 92.90% used; 114196742 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105815212032 available bytes; 94.10% used; 114349323 free inodes.

server4 `/home`: 105815212032 available bytes; 94.10% used; 114349323 free inodes.

server4 `/data`: 339789631488 available bytes; 95.30% used; 225374292 free inodes.

server4 `/tmp`: 105815212032 available bytes; 94.10% used; 114349323 free inodes.

server4 `/var/tmp`: 105815212032 available bytes; 94.10% used; 114349323 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
