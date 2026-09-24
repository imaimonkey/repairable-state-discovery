# V2R cluster inventory

2026-09-24T12:39:41.077942+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324044296192 available bytes; 81.92% used; 112481556 free inodes.

server1 `/home`: 324044296192 available bytes; 81.92% used; 112481556 free inodes.

server1 `/tmp`: 324044296192 available bytes; 81.92% used; 112481556 free inodes.

server1 `/var/tmp`: 324044296192 available bytes; 81.92% used; 112481556 free inodes.

server1 `/mnt/raid5`: 405150564352 available bytes; 98.14% used; 337681235 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57586307072 available bytes; 96.79% used; 110429304 free inodes.

server2 `/home`: 57586307072 available bytes; 96.79% used; 110429304 free inodes.

server2 `/tmp`: 57586307072 available bytes; 96.79% used; 110429304 free inodes.

server2 `/var/tmp`: 57586307072 available bytes; 96.79% used; 110429304 free inodes.

server2 `/mnt/raid5`: 508200132608 available bytes; 96.49% used; 445171467 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85697343488 available bytes; 95.22% used; 114196330 free inodes.

server3 `/home`: 85697343488 available bytes; 95.22% used; 114196330 free inodes.

server3 `/data`: 163239931904 available bytes; 97.74% used; 225814572 free inodes.

server3 `/tmp`: 85697343488 available bytes; 95.22% used; 114196330 free inodes.

server3 `/var/tmp`: 85697343488 available bytes; 95.22% used; 114196330 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780277248 available bytes; 94.10% used; 114348789 free inodes.

server4 `/home`: 105780277248 available bytes; 94.10% used; 114348789 free inodes.

server4 `/data`: 90054328320 available bytes; 98.76% used; 225257232 free inodes.

server4 `/tmp`: 105780277248 available bytes; 94.10% used; 114348789 free inodes.

server4 `/var/tmp`: 105780277248 available bytes; 94.10% used; 114348789 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
