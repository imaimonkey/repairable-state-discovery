# V2R cluster inventory

2026-09-24T08:22:23.151873+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324402700288 available bytes; 81.90% used; 112490525 free inodes.

server1 `/home`: 324402700288 available bytes; 81.90% used; 112490525 free inodes.

server1 `/tmp`: 324402700288 available bytes; 81.90% used; 112490525 free inodes.

server1 `/var/tmp`: 324402700288 available bytes; 81.90% used; 112490525 free inodes.

server1 `/mnt/raid5`: 510244409344 available bytes; 97.66% used; 337721278 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57809768448 available bytes; 96.77% used; 110431018 free inodes.

server2 `/home`: 57809768448 available bytes; 96.77% used; 110431018 free inodes.

server2 `/tmp`: 57809768448 available bytes; 96.77% used; 110431018 free inodes.

server2 `/var/tmp`: 57809768448 available bytes; 96.77% used; 110431018 free inodes.

server2 `/mnt/raid5`: 516386660352 available bytes; 96.43% used; 445179867 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85512699904 available bytes; 95.23% used; 114179425 free inodes.

server3 `/home`: 85512699904 available bytes; 95.23% used; 114179425 free inodes.

server3 `/data`: 175129776128 available bytes; 97.58% used; 225823130 free inodes.

server3 `/tmp`: 85512699904 available bytes; 95.23% used; 114179425 free inodes.

server3 `/var/tmp`: 85512699904 available bytes; 95.23% used; 114179425 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769656320 available bytes; 94.10% used; 114349133 free inodes.

server4 `/home`: 105769656320 available bytes; 94.10% used; 114349133 free inodes.

server4 `/data`: 280473268224 available bytes; 96.12% used; 225350814 free inodes.

server4 `/tmp`: 105769656320 available bytes; 94.10% used; 114349133 free inodes.

server4 `/var/tmp`: 105769656320 available bytes; 94.10% used; 114349133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
