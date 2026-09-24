# V2R cluster inventory

2026-09-24T23:37:37.103381+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319011786752 available bytes; 82.20% used; 112480780 free inodes.

server1 `/home`: 319011786752 available bytes; 82.20% used; 112480780 free inodes.

server1 `/tmp`: 319011786752 available bytes; 82.20% used; 112480780 free inodes.

server1 `/var/tmp`: 319011786752 available bytes; 82.20% used; 112480780 free inodes.

server1 `/mnt/raid5`: 405246447616 available bytes; 98.14% used; 337612343 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23112855552 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23112855552 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23112855552 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23112855552 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 486164516864 available bytes; 96.64% used; 445150943 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84361609216 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84361609216 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148083310592 available bytes; 97.95% used; 225800779 free inodes.

server3 `/tmp`: 84361609216 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84361609216 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105799372800 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799372800 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 61131436032 available bytes; 99.16% used; 225136379 free inodes.

server4 `/tmp`: 105799372800 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799372800 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
