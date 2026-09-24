# V2R cluster inventory

2026-09-24T14:19:24.257371+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324056600576 available bytes; 81.92% used; 112481459 free inodes.

server1 `/home`: 324056600576 available bytes; 81.92% used; 112481459 free inodes.

server1 `/tmp`: 324056600576 available bytes; 81.92% used; 112481459 free inodes.

server1 `/var/tmp`: 324056600576 available bytes; 81.92% used; 112481459 free inodes.

server1 `/mnt/raid5`: 416920506368 available bytes; 98.09% used; 337669455 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57467641856 available bytes; 96.79% used; 110428225 free inodes.

server2 `/home`: 57467641856 available bytes; 96.79% used; 110428225 free inodes.

server2 `/tmp`: 57467641856 available bytes; 96.79% used; 110428225 free inodes.

server2 `/var/tmp`: 57467641856 available bytes; 96.79% used; 110428225 free inodes.

server2 `/mnt/raid5`: 504279982080 available bytes; 96.52% used; 445168261 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85047644160 available bytes; 95.25% used; 114188748 free inodes.

server3 `/home`: 85047644160 available bytes; 95.25% used; 114188748 free inodes.

server3 `/data`: 160983605248 available bytes; 97.78% used; 225808852 free inodes.

server3 `/tmp`: 85047644160 available bytes; 95.25% used; 114188748 free inodes.

server3 `/var/tmp`: 85047644160 available bytes; 95.25% used; 114188748 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759444992 available bytes; 94.10% used; 114348703 free inodes.

server4 `/home`: 105759444992 available bytes; 94.10% used; 114348703 free inodes.

server4 `/data`: 69363392512 available bytes; 99.04% used; 225257071 free inodes.

server4 `/tmp`: 105759444992 available bytes; 94.10% used; 114348703 free inodes.

server4 `/var/tmp`: 105759444992 available bytes; 94.10% used; 114348703 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
