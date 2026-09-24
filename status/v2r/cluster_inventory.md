# V2R cluster inventory

2026-09-24T14:28:41.855880+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324049780736 available bytes; 81.92% used; 112481459 free inodes.

server1 `/home`: 324049780736 available bytes; 81.92% used; 112481459 free inodes.

server1 `/tmp`: 324049780736 available bytes; 81.92% used; 112481459 free inodes.

server1 `/var/tmp`: 324049780736 available bytes; 81.92% used; 112481459 free inodes.

server1 `/mnt/raid5`: 416906448896 available bytes; 98.09% used; 337668373 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57463808000 available bytes; 96.79% used; 110428128 free inodes.

server2 `/home`: 57463808000 available bytes; 96.79% used; 110428128 free inodes.

server2 `/tmp`: 57463808000 available bytes; 96.79% used; 110428128 free inodes.

server2 `/var/tmp`: 57463808000 available bytes; 96.79% used; 110428128 free inodes.

server2 `/mnt/raid5`: 504526360576 available bytes; 96.51% used; 445167899 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84530556928 available bytes; 95.28% used; 114160736 free inodes.

server3 `/home`: 84530556928 available bytes; 95.28% used; 114160736 free inodes.

server3 `/data`: 160910974976 available bytes; 97.78% used; 225808523 free inodes.

server3 `/tmp`: 84530556928 available bytes; 95.28% used; 114160736 free inodes.

server3 `/var/tmp`: 84530556928 available bytes; 95.28% used; 114160736 free inodes.
| server4 | True | ['0', '4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759019008 available bytes; 94.10% used; 114348691 free inodes.

server4 `/home`: 105759019008 available bytes; 94.10% used; 114348691 free inodes.

server4 `/data`: 69353525248 available bytes; 99.04% used; 225257034 free inodes.

server4 `/tmp`: 105759019008 available bytes; 94.10% used; 114348691 free inodes.

server4 `/var/tmp`: 105759019008 available bytes; 94.10% used; 114348691 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
