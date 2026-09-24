# V2R cluster inventory

2026-09-24T14:11:38.979011+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324058558464 available bytes; 81.92% used; 112481454 free inodes.

server1 `/home`: 324058558464 available bytes; 81.92% used; 112481454 free inodes.

server1 `/tmp`: 324058558464 available bytes; 81.92% used; 112481454 free inodes.

server1 `/var/tmp`: 324058558464 available bytes; 81.92% used; 112481454 free inodes.

server1 `/mnt/raid5`: 416939732992 available bytes; 98.09% used; 337670369 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57478692864 available bytes; 96.79% used; 110428301 free inodes.

server2 `/home`: 57478692864 available bytes; 96.79% used; 110428301 free inodes.

server2 `/tmp`: 57478692864 available bytes; 96.79% used; 110428301 free inodes.

server2 `/var/tmp`: 57478692864 available bytes; 96.79% used; 110428301 free inodes.

server2 `/mnt/raid5`: 505338679296 available bytes; 96.51% used; 445168637 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85080707072 available bytes; 95.25% used; 114190189 free inodes.

server3 `/home`: 85080707072 available bytes; 95.25% used; 114190189 free inodes.

server3 `/data`: 160966127616 available bytes; 97.78% used; 225802384 free inodes.

server3 `/tmp`: 85080707072 available bytes; 95.25% used; 114190189 free inodes.

server3 `/var/tmp`: 85080707072 available bytes; 95.25% used; 114190189 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759645696 available bytes; 94.10% used; 114348703 free inodes.

server4 `/home`: 105759645696 available bytes; 94.10% used; 114348703 free inodes.

server4 `/data`: 69375709184 available bytes; 99.04% used; 225257082 free inodes.

server4 `/tmp`: 105759645696 available bytes; 94.10% used; 114348703 free inodes.

server4 `/var/tmp`: 105759645696 available bytes; 94.10% used; 114348703 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
