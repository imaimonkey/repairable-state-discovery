# V2R cluster inventory

2026-09-23T23:41:26.278369+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325611597824 available bytes; 81.84% used; 112501196 free inodes.

server1 `/home`: 325611597824 available bytes; 81.84% used; 112501196 free inodes.

server1 `/tmp`: 325611597824 available bytes; 81.84% used; 112501196 free inodes.

server1 `/var/tmp`: 325611597824 available bytes; 81.84% used; 112501196 free inodes.

server1 `/mnt/raid5`: 1345782685696 available bytes; 93.83% used; 337735900 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41034326016 available bytes; 97.71% used; 110432528 free inodes.

server2 `/home`: 41034326016 available bytes; 97.71% used; 110432528 free inodes.

server2 `/tmp`: 41034326016 available bytes; 97.71% used; 110432528 free inodes.

server2 `/var/tmp`: 41034326016 available bytes; 97.71% used; 110432528 free inodes.

server2 `/mnt/raid5`: 534115917824 available bytes; 96.31% used; 445205211 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292337987584 available bytes; 83.69% used; 114185701 free inodes.

server3 `/home`: 292337987584 available bytes; 83.69% used; 114185701 free inodes.

server3 `/data`: 82296205312 available bytes; 98.86% used; 225845207 free inodes.

server3 `/tmp`: 292337987584 available bytes; 83.69% used; 114185701 free inodes.

server3 `/var/tmp`: 292337987584 available bytes; 83.69% used; 114185701 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106195193856 available bytes; 94.07% used; 114351951 free inodes.

server4 `/home`: 106195193856 available bytes; 94.07% used; 114351951 free inodes.

server4 `/data`: 292997718016 available bytes; 95.95% used; 225420593 free inodes.

server4 `/tmp`: 106195193856 available bytes; 94.07% used; 114351951 free inodes.

server4 `/var/tmp`: 106195193856 available bytes; 94.07% used; 114351951 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
