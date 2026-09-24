# V2R cluster inventory

2026-09-24T14:10:06.147141+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324058726400 available bytes; 81.92% used; 112481455 free inodes.

server1 `/home`: 324058726400 available bytes; 81.92% used; 112481455 free inodes.

server1 `/tmp`: 324058726400 available bytes; 81.92% used; 112481455 free inodes.

server1 `/var/tmp`: 324058726400 available bytes; 81.92% used; 112481455 free inodes.

server1 `/mnt/raid5`: 416942194688 available bytes; 98.09% used; 337670542 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57480163328 available bytes; 96.79% used; 110428313 free inodes.

server2 `/home`: 57480163328 available bytes; 96.79% used; 110428313 free inodes.

server2 `/tmp`: 57480163328 available bytes; 96.79% used; 110428313 free inodes.

server2 `/var/tmp`: 57480163328 available bytes; 96.79% used; 110428313 free inodes.

server2 `/mnt/raid5`: 504854962176 available bytes; 96.51% used; 445168701 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85082423296 available bytes; 95.25% used; 114190204 free inodes.

server3 `/home`: 85082423296 available bytes; 95.25% used; 114190204 free inodes.

server3 `/data`: 160970010624 available bytes; 97.78% used; 225802405 free inodes.

server3 `/tmp`: 85082423296 available bytes; 95.25% used; 114190204 free inodes.

server3 `/var/tmp`: 85082423296 available bytes; 95.25% used; 114190204 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759690752 available bytes; 94.10% used; 114348703 free inodes.

server4 `/home`: 105759690752 available bytes; 94.10% used; 114348703 free inodes.

server4 `/data`: 69381206016 available bytes; 99.04% used; 225257086 free inodes.

server4 `/tmp`: 105759690752 available bytes; 94.10% used; 114348703 free inodes.

server4 `/var/tmp`: 105759690752 available bytes; 94.10% used; 114348703 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
