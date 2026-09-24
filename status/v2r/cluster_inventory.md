# V2R cluster inventory

2026-09-24T05:27:56.656794+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324553043968 available bytes; 81.89% used; 112492389 free inodes.

server1 `/home`: 324553043968 available bytes; 81.89% used; 112492389 free inodes.

server1 `/tmp`: 324553043968 available bytes; 81.89% used; 112492389 free inodes.

server1 `/var/tmp`: 324553043968 available bytes; 81.89% used; 112492389 free inodes.

server1 `/mnt/raid5`: 514780516352 available bytes; 97.64% used; 337724268 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57168990208 available bytes; 96.81% used; 110431197 free inodes.

server2 `/home`: 57168990208 available bytes; 96.81% used; 110431197 free inodes.

server2 `/tmp`: 57168990208 available bytes; 96.81% used; 110431197 free inodes.

server2 `/var/tmp`: 57168990208 available bytes; 96.81% used; 110431197 free inodes.

server2 `/mnt/raid5`: 522448785408 available bytes; 96.39% used; 445193797 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 210388443136 available bytes; 88.26% used; 114200138 free inodes.

server3 `/home`: 210388426752 available bytes; 88.26% used; 114200138 free inodes.

server3 `/data`: 83085840384 available bytes; 98.85% used; 225839685 free inodes.

server3 `/tmp`: 210388410368 available bytes; 88.26% used; 114200138 free inodes.

server3 `/var/tmp`: 210388402176 available bytes; 88.26% used; 114200138 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105817124864 available bytes; 94.10% used; 114349363 free inodes.

server4 `/home`: 105817124864 available bytes; 94.10% used; 114349363 free inodes.

server4 `/data`: 252563730432 available bytes; 96.51% used; 225366489 free inodes.

server4 `/tmp`: 105817124864 available bytes; 94.10% used; 114349363 free inodes.

server4 `/var/tmp`: 105817124864 available bytes; 94.10% used; 114349363 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
