# V2R cluster inventory

2026-09-27T03:13:38.597471+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315086012416 available bytes; 82.42% used; 112443051 free inodes.

server1 `/home`: 315086012416 available bytes; 82.42% used; 112443051 free inodes.

server1 `/tmp`: 315086012416 available bytes; 82.42% used; 112443051 free inodes.

server1 `/var/tmp`: 315086012416 available bytes; 82.42% used; 112443051 free inodes.

server1 `/mnt/raid5`: 636791361536 available bytes; 97.08% used; 337401381 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17625624576 available bytes; 99.02% used; 110365007 free inodes.

server2 `/home`: 17625624576 available bytes; 99.02% used; 110365007 free inodes.

server2 `/tmp`: 17625624576 available bytes; 99.02% used; 110365007 free inodes.

server2 `/var/tmp`: 17625624576 available bytes; 99.02% used; 110365007 free inodes.

server2 `/mnt/raid5`: 579704336384 available bytes; 95.99% used; 444883373 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78706348032 available bytes; 95.61% used; 114062954 free inodes.

server3 `/home`: 78706348032 available bytes; 95.61% used; 114062954 free inodes.

server3 `/data`: 1336535801856 available bytes; 81.53% used; 225761694 free inodes.

server3 `/tmp`: 78706348032 available bytes; 95.61% used; 114062954 free inodes.

server3 `/var/tmp`: 78706348032 available bytes; 95.61% used; 114062954 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111028645888 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111028645888 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 393630019584 available bytes; 94.56% used; 224781004 free inodes.

server4 `/tmp`: 111028645888 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111028645888 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
