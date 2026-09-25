# V2R cluster inventory

2026-09-25T07:30:38.947362+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318869385216 available bytes; 82.21% used; 112480370 free inodes.

server1 `/home`: 318869385216 available bytes; 82.21% used; 112480370 free inodes.

server1 `/tmp`: 318869385216 available bytes; 82.21% used; 112480370 free inodes.

server1 `/var/tmp`: 318869385216 available bytes; 82.21% used; 112480370 free inodes.

server1 `/mnt/raid5`: 385891127296 available bytes; 98.23% used; 337558422 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22860439552 available bytes; 98.72% used; 110410499 free inodes.

server2 `/home`: 22860439552 available bytes; 98.72% used; 110410499 free inodes.

server2 `/tmp`: 22860439552 available bytes; 98.72% used; 110410499 free inodes.

server2 `/var/tmp`: 22860439552 available bytes; 98.72% used; 110410499 free inodes.

server2 `/mnt/raid5`: 343202672640 available bytes; 97.63% used; 445097325 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84445425664 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84445425664 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142393491456 available bytes; 98.03% used; 225812701 free inodes.

server3 `/tmp`: 84445425664 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84445425664 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637826560 available bytes; 94.11% used; 114350354 free inodes.

server4 `/home`: 105637826560 available bytes; 94.11% used; 114350354 free inodes.

server4 `/data`: 249094909952 available bytes; 96.56% used; 225014318 free inodes.

server4 `/tmp`: 105637826560 available bytes; 94.11% used; 114350354 free inodes.

server4 `/var/tmp`: 105637826560 available bytes; 94.11% used; 114350354 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
