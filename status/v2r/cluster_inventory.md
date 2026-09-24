# V2R cluster inventory

2026-09-24T14:20:57.333001+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324056481792 available bytes; 81.92% used; 112481459 free inodes.

server1 `/home`: 324056481792 available bytes; 81.92% used; 112481459 free inodes.

server1 `/tmp`: 324056481792 available bytes; 81.92% used; 112481459 free inodes.

server1 `/var/tmp`: 324056481792 available bytes; 81.92% used; 112481459 free inodes.

server1 `/mnt/raid5`: 416918007808 available bytes; 98.09% used; 337669278 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57468309504 available bytes; 96.79% used; 110428215 free inodes.

server2 `/home`: 57468309504 available bytes; 96.79% used; 110428215 free inodes.

server2 `/tmp`: 57468309504 available bytes; 96.79% used; 110428215 free inodes.

server2 `/var/tmp`: 57468309504 available bytes; 96.79% used; 110428215 free inodes.

server2 `/mnt/raid5`: 504775929856 available bytes; 96.51% used; 445168174 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85045497856 available bytes; 95.25% used; 114188740 free inodes.

server3 `/home`: 85045497856 available bytes; 95.25% used; 114188740 free inodes.

server3 `/data`: 160973172736 available bytes; 97.78% used; 225808804 free inodes.

server3 `/tmp`: 85045497856 available bytes; 95.25% used; 114188740 free inodes.

server3 `/var/tmp`: 85045497856 available bytes; 95.25% used; 114188740 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759318016 available bytes; 94.10% used; 114348699 free inodes.

server4 `/home`: 105759318016 available bytes; 94.10% used; 114348699 free inodes.

server4 `/data`: 69362442240 available bytes; 99.04% used; 225257063 free inodes.

server4 `/tmp`: 105759318016 available bytes; 94.10% used; 114348699 free inodes.

server4 `/var/tmp`: 105759318016 available bytes; 94.10% used; 114348699 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
