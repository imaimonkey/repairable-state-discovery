# V2R cluster inventory

2026-09-25T05:50:36.554037+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318870224896 available bytes; 82.21% used; 112480334 free inodes.

server1 `/home`: 318870224896 available bytes; 82.21% used; 112480334 free inodes.

server1 `/tmp`: 318870224896 available bytes; 82.21% used; 112480334 free inodes.

server1 `/var/tmp`: 318870224896 available bytes; 82.21% used; 112480334 free inodes.

server1 `/mnt/raid5`: 408441171968 available bytes; 98.13% used; 337565835 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22912208896 available bytes; 98.72% used; 110410373 free inodes.

server2 `/home`: 22912208896 available bytes; 98.72% used; 110410373 free inodes.

server2 `/tmp`: 22912208896 available bytes; 98.72% used; 110410373 free inodes.

server2 `/var/tmp`: 22912208896 available bytes; 98.72% used; 110410373 free inodes.

server2 `/mnt/raid5`: 411610550272 available bytes; 97.16% used; 445101874 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84312887296 available bytes; 95.30% used; 114156043 free inodes.

server3 `/home`: 84312887296 available bytes; 95.30% used; 114156043 free inodes.

server3 `/data`: 142775107584 available bytes; 98.03% used; 225814486 free inodes.

server3 `/tmp`: 84312887296 available bytes; 95.30% used; 114156043 free inodes.

server3 `/var/tmp`: 84312887296 available bytes; 95.30% used; 114156043 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649397760 available bytes; 94.10% used; 114350388 free inodes.

server4 `/home`: 105649397760 available bytes; 94.10% used; 114350388 free inodes.

server4 `/data`: 256308752384 available bytes; 96.46% used; 225027321 free inodes.

server4 `/tmp`: 105649397760 available bytes; 94.10% used; 114350388 free inodes.

server4 `/var/tmp`: 105649397760 available bytes; 94.10% used; 114350388 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
