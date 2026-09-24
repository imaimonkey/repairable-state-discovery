# V2R cluster inventory

2026-09-24T12:56:51.812086+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324041162752 available bytes; 81.92% used; 112481551 free inodes.

server1 `/home`: 324041162752 available bytes; 81.92% used; 112481551 free inodes.

server1 `/tmp`: 324041162752 available bytes; 81.92% used; 112481551 free inodes.

server1 `/var/tmp`: 324041162752 available bytes; 81.92% used; 112481551 free inodes.

server1 `/mnt/raid5`: 417095720960 available bytes; 98.09% used; 337679102 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57562832896 available bytes; 96.79% used; 110429065 free inodes.

server2 `/home`: 57562832896 available bytes; 96.79% used; 110429065 free inodes.

server2 `/tmp`: 57562832896 available bytes; 96.79% used; 110429065 free inodes.

server2 `/var/tmp`: 57562832896 available bytes; 96.79% used; 110429065 free inodes.

server2 `/mnt/raid5`: 507667255296 available bytes; 96.49% used; 445170723 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85244252160 available bytes; 95.24% used; 114169188 free inodes.

server3 `/home`: 85244252160 available bytes; 95.24% used; 114169188 free inodes.

server3 `/data`: 163047825408 available bytes; 97.75% used; 225813806 free inodes.

server3 `/tmp`: 85244252160 available bytes; 95.24% used; 114169188 free inodes.

server3 `/var/tmp`: 85244252160 available bytes; 95.24% used; 114169188 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779572736 available bytes; 94.10% used; 114348776 free inodes.

server4 `/home`: 105779572736 available bytes; 94.10% used; 114348776 free inodes.

server4 `/data`: 90037977088 available bytes; 98.76% used; 225257186 free inodes.

server4 `/tmp`: 105779572736 available bytes; 94.10% used; 114348776 free inodes.

server4 `/var/tmp`: 105779572736 available bytes; 94.10% used; 114348776 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
