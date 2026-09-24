# V2R cluster inventory

2026-09-24T07:38:52.823590+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324445761536 available bytes; 81.90% used; 112491059 free inodes.

server1 `/home`: 324445761536 available bytes; 81.90% used; 112491059 free inodes.

server1 `/tmp`: 324445761536 available bytes; 81.90% used; 112491059 free inodes.

server1 `/var/tmp`: 324445761536 available bytes; 81.90% used; 112491059 free inodes.

server1 `/mnt/raid5`: 517026058240 available bytes; 97.63% used; 337722776 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57840615424 available bytes; 96.77% used; 110431142 free inodes.

server2 `/home`: 57840615424 available bytes; 96.77% used; 110431142 free inodes.

server2 `/tmp`: 57840615424 available bytes; 96.77% used; 110431142 free inodes.

server2 `/var/tmp`: 57840615424 available bytes; 96.77% used; 110431142 free inodes.

server2 `/mnt/raid5`: 517997703168 available bytes; 96.42% used; 445180429 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126781177856 available bytes; 92.93% used; 114174978 free inodes.

server3 `/home`: 126781177856 available bytes; 92.93% used; 114174978 free inodes.

server3 `/data`: 138724278272 available bytes; 98.08% used; 225833548 free inodes.

server3 `/tmp`: 126781177856 available bytes; 92.93% used; 114174978 free inodes.

server3 `/var/tmp`: 126781177856 available bytes; 92.93% used; 114174978 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780416512 available bytes; 94.10% used; 114349185 free inodes.

server4 `/home`: 105780416512 available bytes; 94.10% used; 114349185 free inodes.

server4 `/data`: 285701193728 available bytes; 96.05% used; 225366805 free inodes.

server4 `/tmp`: 105780416512 available bytes; 94.10% used; 114349185 free inodes.

server4 `/var/tmp`: 105780416512 available bytes; 94.10% used; 114349185 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
