# V2R cluster inventory

2026-09-25T02:03:49.469946+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319024119808 available bytes; 82.20% used; 112480576 free inodes.

server1 `/home`: 319024119808 available bytes; 82.20% used; 112480576 free inodes.

server1 `/tmp`: 319024119808 available bytes; 82.20% used; 112480576 free inodes.

server1 `/var/tmp`: 319024119808 available bytes; 82.20% used; 112480576 free inodes.

server1 `/mnt/raid5`: 416262713344 available bytes; 98.09% used; 337608997 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23025778688 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 23025778688 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 23025778688 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 23025778688 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 484218429440 available bytes; 96.65% used; 445114561 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84352430080 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84352430080 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 146039689216 available bytes; 97.98% used; 225811647 free inodes.

server3 `/tmp`: 84352430080 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84352430080 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105761038336 available bytes; 94.10% used; 114348250 free inodes.

server4 `/home`: 105761038336 available bytes; 94.10% used; 114348250 free inodes.

server4 `/data`: 48495579136 available bytes; 99.33% used; 225030318 free inodes.

server4 `/tmp`: 105761038336 available bytes; 94.10% used; 114348250 free inodes.

server4 `/var/tmp`: 105761038336 available bytes; 94.10% used; 114348250 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
