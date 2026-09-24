# V2R cluster inventory

2026-09-24T01:12:14.004048+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325478768640 available bytes; 81.84% used; 112499921 free inodes.

server1 `/home`: 325478768640 available bytes; 81.84% used; 112499921 free inodes.

server1 `/tmp`: 325478768640 available bytes; 81.84% used; 112499921 free inodes.

server1 `/var/tmp`: 325478768640 available bytes; 81.84% used; 112499921 free inodes.

server1 `/mnt/raid5`: 969613275136 available bytes; 95.55% used; 337734141 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40964255744 available bytes; 97.71% used; 110432127 free inodes.

server2 `/home`: 40964255744 available bytes; 97.71% used; 110432127 free inodes.

server2 `/tmp`: 40964255744 available bytes; 97.71% used; 110432127 free inodes.

server2 `/var/tmp`: 40964255744 available bytes; 97.71% used; 110432127 free inodes.

server2 `/mnt/raid5`: 531469754368 available bytes; 96.33% used; 445201792 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292450689024 available bytes; 83.68% used; 114198524 free inodes.

server3 `/home`: 292450689024 available bytes; 83.68% used; 114198524 free inodes.

server3 `/data`: 82079952896 available bytes; 98.87% used; 225843036 free inodes.

server3 `/tmp`: 292450689024 available bytes; 83.68% used; 114198524 free inodes.

server3 `/var/tmp`: 292450689024 available bytes; 83.68% used; 114198524 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105999933440 available bytes; 94.08% used; 114349211 free inodes.

server4 `/home`: 105999933440 available bytes; 94.08% used; 114349211 free inodes.

server4 `/data`: 291865014272 available bytes; 95.97% used; 225405350 free inodes.

server4 `/tmp`: 105999933440 available bytes; 94.08% used; 114349211 free inodes.

server4 `/var/tmp`: 105999933440 available bytes; 94.08% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
