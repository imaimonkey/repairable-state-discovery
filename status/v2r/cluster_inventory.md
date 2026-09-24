# V2R cluster inventory

2026-09-24T11:50:57.060710+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324296593408 available bytes; 81.91% used; 112488514 free inodes.

server1 `/home`: 324296593408 available bytes; 81.91% used; 112488514 free inodes.

server1 `/tmp`: 324296593408 available bytes; 81.91% used; 112488514 free inodes.

server1 `/var/tmp`: 324296593408 available bytes; 81.91% used; 112488514 free inodes.

server1 `/mnt/raid5`: 419914141696 available bytes; 98.07% used; 337686804 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57638948864 available bytes; 96.78% used; 110429788 free inodes.

server2 `/home`: 57638948864 available bytes; 96.78% used; 110429788 free inodes.

server2 `/tmp`: 57638948864 available bytes; 96.78% used; 110429788 free inodes.

server2 `/var/tmp`: 57638948864 available bytes; 96.78% used; 110429788 free inodes.

server2 `/mnt/raid5`: 509996670976 available bytes; 96.48% used; 445172710 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85341827072 available bytes; 95.24% used; 114173329 free inodes.

server3 `/home`: 85341827072 available bytes; 95.24% used; 114173329 free inodes.

server3 `/data`: 163647037440 available bytes; 97.74% used; 225815852 free inodes.

server3 `/tmp`: 85341827072 available bytes; 95.24% used; 114173329 free inodes.

server3 `/var/tmp`: 85341827072 available bytes; 95.24% used; 114173329 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105727520768 available bytes; 94.10% used; 114348834 free inodes.

server4 `/home`: 105727520768 available bytes; 94.10% used; 114348834 free inodes.

server4 `/data`: 115387301888 available bytes; 98.41% used; 225257922 free inodes.

server4 `/tmp`: 105727520768 available bytes; 94.10% used; 114348834 free inodes.

server4 `/var/tmp`: 105727520768 available bytes; 94.10% used; 114348834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
