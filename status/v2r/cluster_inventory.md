# V2R cluster inventory

2026-09-24T18:27:45.498265+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324007260160 available bytes; 81.92% used; 112481436 free inodes.

server1 `/home`: 324007260160 available bytes; 81.92% used; 112481436 free inodes.

server1 `/tmp`: 324007260160 available bytes; 81.92% used; 112481436 free inodes.

server1 `/var/tmp`: 324007260160 available bytes; 81.92% used; 112481436 free inodes.

server1 `/mnt/raid5`: 416324014080 available bytes; 98.09% used; 337639656 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54491017216 available bytes; 96.96% used; 110411986 free inodes.

server2 `/home`: 54491017216 available bytes; 96.96% used; 110411986 free inodes.

server2 `/tmp`: 54491017216 available bytes; 96.96% used; 110411986 free inodes.

server2 `/var/tmp`: 54491017216 available bytes; 96.96% used; 110411986 free inodes.

server2 `/mnt/raid5`: 496809496576 available bytes; 96.57% used; 445160822 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84407603200 available bytes; 95.29% used; 114156134 free inodes.

server3 `/home`: 84407603200 available bytes; 95.29% used; 114156134 free inodes.

server3 `/data`: 152907145216 available bytes; 97.89% used; 225800579 free inodes.

server3 `/tmp`: 84407603200 available bytes; 95.29% used; 114156134 free inodes.

server3 `/var/tmp`: 84407603200 available bytes; 95.29% used; 114156134 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105662394368 available bytes; 94.10% used; 114348506 free inodes.

server4 `/home`: 105662394368 available bytes; 94.10% used; 114348506 free inodes.

server4 `/data`: 90053779456 available bytes; 98.76% used; 225267995 free inodes.

server4 `/tmp`: 105662394368 available bytes; 94.10% used; 114348506 free inodes.

server4 `/var/tmp`: 105662394368 available bytes; 94.10% used; 114348506 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
