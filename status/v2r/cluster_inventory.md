# V2R cluster inventory

2026-09-24T12:31:50.988182+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324053880832 available bytes; 81.92% used; 112481555 free inodes.

server1 `/home`: 324053880832 available bytes; 81.92% used; 112481555 free inodes.

server1 `/tmp`: 324053880832 available bytes; 81.92% used; 112481555 free inodes.

server1 `/var/tmp`: 324053880832 available bytes; 81.92% used; 112481555 free inodes.

server1 `/mnt/raid5`: 405184741376 available bytes; 98.14% used; 337682180 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57594163200 available bytes; 96.79% used; 110429382 free inodes.

server2 `/home`: 57594163200 available bytes; 96.79% used; 110429382 free inodes.

server2 `/tmp`: 57594163200 available bytes; 96.79% used; 110429382 free inodes.

server2 `/var/tmp`: 57594163200 available bytes; 96.79% used; 110429382 free inodes.

server2 `/mnt/raid5`: 508446056448 available bytes; 96.49% used; 445171838 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85698727936 available bytes; 95.22% used; 114195297 free inodes.

server3 `/home`: 85698727936 available bytes; 95.22% used; 114195297 free inodes.

server3 `/data`: 163294109696 available bytes; 97.74% used; 225814719 free inodes.

server3 `/tmp`: 85698727936 available bytes; 95.22% used; 114195297 free inodes.

server3 `/var/tmp`: 85698727936 available bytes; 95.22% used; 114195297 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780551680 available bytes; 94.10% used; 114348793 free inodes.

server4 `/home`: 105780551680 available bytes; 94.10% used; 114348793 free inodes.

server4 `/data`: 90072207360 available bytes; 98.76% used; 225257241 free inodes.

server4 `/tmp`: 105780551680 available bytes; 94.10% used; 114348793 free inodes.

server4 `/var/tmp`: 105780551680 available bytes; 94.10% used; 114348793 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
