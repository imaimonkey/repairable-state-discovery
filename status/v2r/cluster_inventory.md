# V2R cluster inventory

2026-09-24T14:03:53.100264+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324062683136 available bytes; 81.92% used; 112481661 free inodes.

server1 `/home`: 324062683136 available bytes; 81.92% used; 112481661 free inodes.

server1 `/tmp`: 324062683136 available bytes; 81.92% used; 112481661 free inodes.

server1 `/var/tmp`: 324062683136 available bytes; 81.92% used; 112481661 free inodes.

server1 `/mnt/raid5`: 416957640704 available bytes; 98.09% used; 337671275 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57486143488 available bytes; 96.79% used; 110428375 free inodes.

server2 `/home`: 57486143488 available bytes; 96.79% used; 110428375 free inodes.

server2 `/tmp`: 57486143488 available bytes; 96.79% used; 110428375 free inodes.

server2 `/var/tmp`: 57486143488 available bytes; 96.79% used; 110428375 free inodes.

server2 `/mnt/raid5`: 505573548032 available bytes; 96.51% used; 445168489 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85087928320 available bytes; 95.25% used; 114190411 free inodes.

server3 `/home`: 85087928320 available bytes; 95.25% used; 114190411 free inodes.

server3 `/data`: 161012158464 available bytes; 97.77% used; 225802523 free inodes.

server3 `/tmp`: 85087928320 available bytes; 95.25% used; 114190411 free inodes.

server3 `/var/tmp`: 85087928320 available bytes; 95.25% used; 114190411 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759997952 available bytes; 94.10% used; 114348712 free inodes.

server4 `/home`: 105759997952 available bytes; 94.10% used; 114348712 free inodes.

server4 `/data`: 69387976704 available bytes; 99.04% used; 225257141 free inodes.

server4 `/tmp`: 105759997952 available bytes; 94.10% used; 114348712 free inodes.

server4 `/var/tmp`: 105759997952 available bytes; 94.10% used; 114348712 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
