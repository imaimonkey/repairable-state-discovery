# V2R cluster inventory

2026-09-24T18:30:50.341344+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324006359040 available bytes; 81.92% used; 112481442 free inodes.

server1 `/home`: 324006359040 available bytes; 81.92% used; 112481442 free inodes.

server1 `/tmp`: 324006359040 available bytes; 81.92% used; 112481442 free inodes.

server1 `/var/tmp`: 324006359040 available bytes; 81.92% used; 112481442 free inodes.

server1 `/mnt/raid5`: 416319229952 available bytes; 98.09% used; 337639311 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54490386432 available bytes; 96.96% used; 110411980 free inodes.

server2 `/home`: 54490386432 available bytes; 96.96% used; 110411980 free inodes.

server2 `/tmp`: 54490386432 available bytes; 96.96% used; 110411980 free inodes.

server2 `/var/tmp`: 54490386432 available bytes; 96.96% used; 110411980 free inodes.

server2 `/mnt/raid5`: 496702046208 available bytes; 96.57% used; 445160755 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84409257984 available bytes; 95.29% used; 114156134 free inodes.

server3 `/home`: 84409257984 available bytes; 95.29% used; 114156134 free inodes.

server3 `/data`: 152876937216 available bytes; 97.89% used; 225800530 free inodes.

server3 `/tmp`: 84409257984 available bytes; 95.29% used; 114156134 free inodes.

server3 `/var/tmp`: 84409257984 available bytes; 95.29% used; 114156134 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105662279680 available bytes; 94.10% used; 114348506 free inodes.

server4 `/home`: 105662279680 available bytes; 94.10% used; 114348506 free inodes.

server4 `/data`: 90048122880 available bytes; 98.76% used; 225267991 free inodes.

server4 `/tmp`: 105662279680 available bytes; 94.10% used; 114348506 free inodes.

server4 `/var/tmp`: 105662279680 available bytes; 94.10% used; 114348506 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
