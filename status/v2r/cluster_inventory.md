# V2R cluster inventory

2026-09-24T14:00:45.546147+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324067397632 available bytes; 81.92% used; 112481656 free inodes.

server1 `/home`: 324067397632 available bytes; 81.92% used; 112481656 free inodes.

server1 `/tmp`: 324067397632 available bytes; 81.92% used; 112481656 free inodes.

server1 `/var/tmp`: 324067397632 available bytes; 81.92% used; 112481656 free inodes.

server1 `/mnt/raid5`: 416964685824 available bytes; 98.09% used; 337671632 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57490092032 available bytes; 96.79% used; 110428403 free inodes.

server2 `/home`: 57490092032 available bytes; 96.79% used; 110428403 free inodes.

server2 `/tmp`: 57490092032 available bytes; 96.79% used; 110428403 free inodes.

server2 `/var/tmp`: 57490092032 available bytes; 96.79% used; 110428403 free inodes.

server2 `/mnt/raid5`: 505670184960 available bytes; 96.51% used; 445168633 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85091102720 available bytes; 95.25% used; 114190419 free inodes.

server3 `/home`: 85091102720 available bytes; 95.25% used; 114190419 free inodes.

server3 `/data`: 161028628480 available bytes; 97.77% used; 225802581 free inodes.

server3 `/tmp`: 85091102720 available bytes; 95.25% used; 114190419 free inodes.

server3 `/var/tmp`: 85091102720 available bytes; 95.25% used; 114190419 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105760088064 available bytes; 94.10% used; 114348712 free inodes.

server4 `/home`: 105760088064 available bytes; 94.10% used; 114348712 free inodes.

server4 `/data`: 69382643712 available bytes; 99.04% used; 225257148 free inodes.

server4 `/tmp`: 105760088064 available bytes; 94.10% used; 114348712 free inodes.

server4 `/var/tmp`: 105760088064 available bytes; 94.10% used; 114348712 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
