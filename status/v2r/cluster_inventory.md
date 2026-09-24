# V2R cluster inventory

2026-09-24T01:56:59.414394+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325448896512 available bytes; 81.84% used; 112499381 free inodes.

server1 `/home`: 325448896512 available bytes; 81.84% used; 112499381 free inodes.

server1 `/tmp`: 325448896512 available bytes; 81.84% used; 112499381 free inodes.

server1 `/var/tmp`: 325448896512 available bytes; 81.84% used; 112499381 free inodes.

server1 `/mnt/raid5`: 785891241984 available bytes; 96.39% used; 337733662 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40923082752 available bytes; 97.72% used; 110431795 free inodes.

server2 `/home`: 40923082752 available bytes; 97.72% used; 110431795 free inodes.

server2 `/tmp`: 40923082752 available bytes; 97.72% used; 110431795 free inodes.

server2 `/var/tmp`: 40923082752 available bytes; 97.72% used; 110431795 free inodes.

server2 `/mnt/raid5`: 530047819776 available bytes; 96.34% used; 445200574 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292720107520 available bytes; 83.67% used; 114211080 free inodes.

server3 `/home`: 292720107520 available bytes; 83.67% used; 114211080 free inodes.

server3 `/data`: 60367245312 available bytes; 99.17% used; 225841749 free inodes.

server3 `/tmp`: 292720107520 available bytes; 83.67% used; 114211080 free inodes.

server3 `/var/tmp`: 292720107520 available bytes; 83.67% used; 114211080 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105946132480 available bytes; 94.09% used; 114348489 free inodes.

server4 `/home`: 105946132480 available bytes; 94.09% used; 114348489 free inodes.

server4 `/data`: 289768812544 available bytes; 96.00% used; 225388486 free inodes.

server4 `/tmp`: 105946132480 available bytes; 94.09% used; 114348489 free inodes.

server4 `/var/tmp`: 105946132480 available bytes; 94.09% used; 114348489 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
