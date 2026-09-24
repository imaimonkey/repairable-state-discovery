# V2R cluster inventory

2026-09-24T01:55:26.901394+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325450330112 available bytes; 81.84% used; 112499399 free inodes.

server1 `/home`: 325450330112 available bytes; 81.84% used; 112499399 free inodes.

server1 `/tmp`: 325450330112 available bytes; 81.84% used; 112499399 free inodes.

server1 `/var/tmp`: 325450330112 available bytes; 81.84% used; 112499399 free inodes.

server1 `/mnt/raid5`: 792741777408 available bytes; 96.36% used; 337733688 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40922959872 available bytes; 97.72% used; 110431805 free inodes.

server2 `/home`: 40922959872 available bytes; 97.72% used; 110431805 free inodes.

server2 `/tmp`: 40922959872 available bytes; 97.72% used; 110431805 free inodes.

server2 `/var/tmp`: 40922959872 available bytes; 97.72% used; 110431805 free inodes.

server2 `/mnt/raid5`: 530091974656 available bytes; 96.34% used; 445200691 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292720861184 available bytes; 83.67% used; 114211090 free inodes.

server3 `/home`: 292720861184 available bytes; 83.67% used; 114211090 free inodes.

server3 `/data`: 60368281600 available bytes; 99.17% used; 225841773 free inodes.

server3 `/tmp`: 292720861184 available bytes; 83.67% used; 114211090 free inodes.

server3 `/var/tmp`: 292720861184 available bytes; 83.67% used; 114211090 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105946767360 available bytes; 94.09% used; 114348504 free inodes.

server4 `/home`: 105946767360 available bytes; 94.09% used; 114348504 free inodes.

server4 `/data`: 289770479616 available bytes; 96.00% used; 225388495 free inodes.

server4 `/tmp`: 105946767360 available bytes; 94.09% used; 114348504 free inodes.

server4 `/var/tmp`: 105946767360 available bytes; 94.09% used; 114348504 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
