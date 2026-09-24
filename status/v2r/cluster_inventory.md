# V2R cluster inventory

2026-09-24T07:37:19.582641+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324447338496 available bytes; 81.90% used; 112491076 free inodes.

server1 `/home`: 324447338496 available bytes; 81.90% used; 112491076 free inodes.

server1 `/tmp`: 324447338496 available bytes; 81.90% used; 112491076 free inodes.

server1 `/var/tmp`: 324447338496 available bytes; 81.90% used; 112491076 free inodes.

server1 `/mnt/raid5`: 517190610944 available bytes; 97.63% used; 337722778 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57841184768 available bytes; 96.77% used; 110431146 free inodes.

server2 `/home`: 57841184768 available bytes; 96.77% used; 110431146 free inodes.

server2 `/tmp`: 57841184768 available bytes; 96.77% used; 110431146 free inodes.

server2 `/var/tmp`: 57841184768 available bytes; 96.77% used; 110431146 free inodes.

server2 `/mnt/raid5`: 518038470656 available bytes; 96.42% used; 445180579 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126781427712 available bytes; 92.93% used; 114174978 free inodes.

server3 `/home`: 126781427712 available bytes; 92.93% used; 114174978 free inodes.

server3 `/data`: 138735136768 available bytes; 98.08% used; 225833595 free inodes.

server3 `/tmp`: 126781427712 available bytes; 92.93% used; 114174978 free inodes.

server3 `/var/tmp`: 126781427712 available bytes; 92.93% used; 114174978 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780457472 available bytes; 94.10% used; 114349185 free inodes.

server4 `/home`: 105780457472 available bytes; 94.10% used; 114349185 free inodes.

server4 `/data`: 285751992320 available bytes; 96.05% used; 225366820 free inodes.

server4 `/tmp`: 105780457472 available bytes; 94.10% used; 114349185 free inodes.

server4 `/var/tmp`: 105780457472 available bytes; 94.10% used; 114349185 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
