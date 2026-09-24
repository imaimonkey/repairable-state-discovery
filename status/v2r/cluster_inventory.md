# V2R cluster inventory

2026-09-24T12:44:26.030907+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324040339456 available bytes; 81.92% used; 112481553 free inodes.

server1 `/home`: 324040339456 available bytes; 81.92% used; 112481553 free inodes.

server1 `/tmp`: 324040339456 available bytes; 81.92% used; 112481553 free inodes.

server1 `/var/tmp`: 324040339456 available bytes; 81.92% used; 112481553 free inodes.

server1 `/mnt/raid5`: 403370954752 available bytes; 98.15% used; 337680614 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57580707840 available bytes; 96.79% used; 110429189 free inodes.

server2 `/home`: 57580707840 available bytes; 96.79% used; 110429189 free inodes.

server2 `/tmp`: 57580707840 available bytes; 96.79% used; 110429189 free inodes.

server2 `/var/tmp`: 57580707840 available bytes; 96.79% used; 110429189 free inodes.

server2 `/mnt/raid5`: 508048084992 available bytes; 96.49% used; 445171136 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 85325033472 available bytes; 95.24% used; 114179680 free inodes.

server3 `/home`: 85325033472 available bytes; 95.24% used; 114179680 free inodes.

server3 `/data`: 163151306752 available bytes; 97.75% used; 225814462 free inodes.

server3 `/tmp`: 85325033472 available bytes; 95.24% used; 114179680 free inodes.

server3 `/var/tmp`: 85325033472 available bytes; 95.24% used; 114179680 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780072448 available bytes; 94.10% used; 114348784 free inodes.

server4 `/home`: 105780072448 available bytes; 94.10% used; 114348784 free inodes.

server4 `/data`: 90049085440 available bytes; 98.76% used; 225257239 free inodes.

server4 `/tmp`: 105780072448 available bytes; 94.10% used; 114348784 free inodes.

server4 `/var/tmp`: 105780072448 available bytes; 94.10% used; 114348784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
