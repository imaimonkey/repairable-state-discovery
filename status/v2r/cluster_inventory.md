# V2R cluster inventory

2026-09-24T01:58:31.808476+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325447270400 available bytes; 81.84% used; 112499316 free inodes.

server1 `/home`: 325447270400 available bytes; 81.84% used; 112499316 free inodes.

server1 `/tmp`: 325447270400 available bytes; 81.84% used; 112499316 free inodes.

server1 `/var/tmp`: 325447270400 available bytes; 81.84% used; 112499316 free inodes.

server1 `/mnt/raid5`: 780336447488 available bytes; 96.42% used; 337733642 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40921485312 available bytes; 97.72% used; 110431781 free inodes.

server2 `/home`: 40921485312 available bytes; 97.72% used; 110431781 free inodes.

server2 `/tmp`: 40921485312 available bytes; 97.72% used; 110431781 free inodes.

server2 `/var/tmp`: 40921485312 available bytes; 97.72% used; 110431781 free inodes.

server2 `/mnt/raid5`: 529997012992 available bytes; 96.34% used; 445200610 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292720381952 available bytes; 83.67% used; 114211082 free inodes.

server3 `/home`: 292720381952 available bytes; 83.67% used; 114211082 free inodes.

server3 `/data`: 60365168640 available bytes; 99.17% used; 225841711 free inodes.

server3 `/tmp`: 292720381952 available bytes; 83.67% used; 114211082 free inodes.

server3 `/var/tmp`: 292720381952 available bytes; 83.67% used; 114211082 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105938505728 available bytes; 94.09% used; 114348472 free inodes.

server4 `/home`: 105938505728 available bytes; 94.09% used; 114348472 free inodes.

server4 `/data`: 289777975296 available bytes; 96.00% used; 225388494 free inodes.

server4 `/tmp`: 105938505728 available bytes; 94.09% used; 114348472 free inodes.

server4 `/var/tmp`: 105938505728 available bytes; 94.09% used; 114348472 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
