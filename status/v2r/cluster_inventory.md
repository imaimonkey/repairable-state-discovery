# V2R cluster inventory

2026-09-24T01:53:54.133780+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325451264000 available bytes; 81.84% used; 112499405 free inodes.

server1 `/home`: 325451264000 available bytes; 81.84% used; 112499405 free inodes.

server1 `/tmp`: 325451264000 available bytes; 81.84% used; 112499405 free inodes.

server1 `/var/tmp`: 325451264000 available bytes; 81.84% used; 112499405 free inodes.

server1 `/mnt/raid5`: 798951215104 available bytes; 96.33% used; 337733661 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40922939392 available bytes; 97.72% used; 110431817 free inodes.

server2 `/home`: 40922939392 available bytes; 97.72% used; 110431817 free inodes.

server2 `/tmp`: 40922939392 available bytes; 97.72% used; 110431817 free inodes.

server2 `/var/tmp`: 40922939392 available bytes; 97.72% used; 110431817 free inodes.

server2 `/mnt/raid5`: 530140037120 available bytes; 96.34% used; 445200863 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292720013312 available bytes; 83.67% used; 114211042 free inodes.

server3 `/home`: 292720013312 available bytes; 83.67% used; 114211042 free inodes.

server3 `/data`: 60689682432 available bytes; 99.16% used; 225841812 free inodes.

server3 `/tmp`: 292720013312 available bytes; 83.67% used; 114211042 free inodes.

server3 `/var/tmp`: 292720013312 available bytes; 83.67% used; 114211042 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105947807744 available bytes; 94.09% used; 114348520 free inodes.

server4 `/home`: 105947807744 available bytes; 94.09% used; 114348520 free inodes.

server4 `/data`: 289771212800 available bytes; 96.00% used; 225388495 free inodes.

server4 `/tmp`: 105947807744 available bytes; 94.09% used; 114348520 free inodes.

server4 `/var/tmp`: 105947807744 available bytes; 94.09% used; 114348520 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
