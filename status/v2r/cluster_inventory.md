# V2R cluster inventory

2026-09-24T04:18:23.080126+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324708884480 available bytes; 81.89% used; 112493349 free inodes.

server1 `/home`: 324708884480 available bytes; 81.89% used; 112493349 free inodes.

server1 `/tmp`: 324708884480 available bytes; 81.89% used; 112493349 free inodes.

server1 `/var/tmp`: 324708884480 available bytes; 81.89% used; 112493349 free inodes.

server1 `/mnt/raid5`: 431140028416 available bytes; 98.02% used; 337724730 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40795598848 available bytes; 97.72% used; 110430736 free inodes.

server2 `/home`: 40795598848 available bytes; 97.72% used; 110430736 free inodes.

server2 `/tmp`: 40795598848 available bytes; 97.72% used; 110430736 free inodes.

server2 `/var/tmp`: 40795598848 available bytes; 97.72% used; 110430736 free inodes.

server2 `/mnt/raid5`: 525734748160 available bytes; 96.37% used; 445196203 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292202438656 available bytes; 83.69% used; 114194238 free inodes.

server3 `/home`: 292202438656 available bytes; 83.69% used; 114194238 free inodes.

server3 `/data`: 31709614080 available bytes; 99.56% used; 225841713 free inodes.

server3 `/tmp`: 292202438656 available bytes; 83.69% used; 114194238 free inodes.

server3 `/var/tmp`: 292202438656 available bytes; 83.69% used; 114194238 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105851994112 available bytes; 94.09% used; 114349453 free inodes.

server4 `/home`: 105851994112 available bytes; 94.09% used; 114349453 free inodes.

server4 `/data`: 256706334720 available bytes; 96.45% used; 225381788 free inodes.

server4 `/tmp`: 105851994112 available bytes; 94.09% used; 114349453 free inodes.

server4 `/var/tmp`: 105851994112 available bytes; 94.09% used; 114349453 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
