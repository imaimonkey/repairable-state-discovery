# V2R cluster inventory

2026-09-27T03:01:27.626233+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315086057472 available bytes; 82.42% used; 112443053 free inodes.

server1 `/home`: 315086057472 available bytes; 82.42% used; 112443053 free inodes.

server1 `/tmp`: 315086057472 available bytes; 82.42% used; 112443053 free inodes.

server1 `/var/tmp`: 315086057472 available bytes; 82.42% used; 112443053 free inodes.

server1 `/mnt/raid5`: 636811743232 available bytes; 97.08% used; 337401386 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17633300480 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17633300480 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17633300480 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17633300480 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 580064079872 available bytes; 95.99% used; 444883839 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78705430528 available bytes; 95.61% used; 114062940 free inodes.

server3 `/home`: 78705430528 available bytes; 95.61% used; 114062940 free inodes.

server3 `/data`: 1336574832640 available bytes; 81.53% used; 225761824 free inodes.

server3 `/tmp`: 78705430528 available bytes; 95.61% used; 114062940 free inodes.

server3 `/var/tmp`: 78705430528 available bytes; 95.61% used; 114062940 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111032643584 available bytes; 93.80% used; 114373131 free inodes.

server4 `/home`: 111032643584 available bytes; 93.80% used; 114373131 free inodes.

server4 `/data`: 396848312320 available bytes; 94.52% used; 224781092 free inodes.

server4 `/tmp`: 111032643584 available bytes; 93.80% used; 114373131 free inodes.

server4 `/var/tmp`: 111032643584 available bytes; 93.80% used; 114373131 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
