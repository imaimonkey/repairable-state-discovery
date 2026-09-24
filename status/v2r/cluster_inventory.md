# V2R cluster inventory

2026-09-24T14:08:32.841057+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324061097984 available bytes; 81.92% used; 112481654 free inodes.

server1 `/home`: 324061097984 available bytes; 81.92% used; 112481654 free inodes.

server1 `/tmp`: 324061097984 available bytes; 81.92% used; 112481654 free inodes.

server1 `/var/tmp`: 324061097984 available bytes; 81.92% used; 112481654 free inodes.

server1 `/mnt/raid5`: 416947236864 available bytes; 98.09% used; 337670729 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57481633792 available bytes; 96.79% used; 110428327 free inodes.

server2 `/home`: 57481633792 available bytes; 96.79% used; 110428327 free inodes.

server2 `/tmp`: 57481633792 available bytes; 96.79% used; 110428327 free inodes.

server2 `/var/tmp`: 57481633792 available bytes; 96.79% used; 110428327 free inodes.

server2 `/mnt/raid5`: 505441181696 available bytes; 96.51% used; 445168775 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85083283456 available bytes; 95.25% used; 114190238 free inodes.

server3 `/home`: 85083283456 available bytes; 95.25% used; 114190238 free inodes.

server3 `/data`: 160981504000 available bytes; 97.78% used; 225802439 free inodes.

server3 `/tmp`: 85083283456 available bytes; 95.25% used; 114190238 free inodes.

server3 `/var/tmp`: 85083283456 available bytes; 95.25% used; 114190238 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759834112 available bytes; 94.10% used; 114348708 free inodes.

server4 `/home`: 105759834112 available bytes; 94.10% used; 114348708 free inodes.

server4 `/data`: 69382139904 available bytes; 99.04% used; 225257115 free inodes.

server4 `/tmp`: 105759834112 available bytes; 94.10% used; 114348708 free inodes.

server4 `/var/tmp`: 105759834112 available bytes; 94.10% used; 114348708 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
