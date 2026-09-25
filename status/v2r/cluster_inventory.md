# V2R cluster inventory

2026-09-25T05:42:55.634739+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871490560 available bytes; 82.21% used; 112480333 free inodes.

server1 `/home`: 318871490560 available bytes; 82.21% used; 112480333 free inodes.

server1 `/tmp`: 318871490560 available bytes; 82.21% used; 112480333 free inodes.

server1 `/var/tmp`: 318871490560 available bytes; 82.21% used; 112480333 free inodes.

server1 `/mnt/raid5`: 408460218368 available bytes; 98.13% used; 337566737 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22914535424 available bytes; 98.72% used; 110410492 free inodes.

server2 `/home`: 22914535424 available bytes; 98.72% used; 110410492 free inodes.

server2 `/tmp`: 22914535424 available bytes; 98.72% used; 110410492 free inodes.

server2 `/var/tmp`: 22914535424 available bytes; 98.72% used; 110410492 free inodes.

server2 `/mnt/raid5`: 428287762432 available bytes; 97.04% used; 445102575 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84313243648 available bytes; 95.30% used; 114156039 free inodes.

server3 `/home`: 84313243648 available bytes; 95.30% used; 114156039 free inodes.

server3 `/data`: 142775656448 available bytes; 98.03% used; 225814614 free inodes.

server3 `/tmp`: 84313243648 available bytes; 95.30% used; 114156039 free inodes.

server3 `/var/tmp`: 84313243648 available bytes; 95.30% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649614848 available bytes; 94.10% used; 114350389 free inodes.

server4 `/home`: 105649614848 available bytes; 94.10% used; 114350389 free inodes.

server4 `/data`: 24762392576 available bytes; 99.66% used; 224966051 free inodes.

server4 `/tmp`: 105649614848 available bytes; 94.10% used; 114350389 free inodes.

server4 `/var/tmp`: 105649614848 available bytes; 94.10% used; 114350389 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
