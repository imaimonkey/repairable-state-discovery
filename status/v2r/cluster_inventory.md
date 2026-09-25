# V2R cluster inventory

2026-09-25T13:26:28.059744+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319106822144 available bytes; 82.20% used; 112477573 free inodes.

server1 `/home`: 319106822144 available bytes; 82.20% used; 112477573 free inodes.

server1 `/tmp`: 319106822144 available bytes; 82.20% used; 112477573 free inodes.

server1 `/var/tmp`: 319106822144 available bytes; 82.20% used; 112477573 free inodes.

server1 `/mnt/raid5`: 364239601664 available bytes; 98.33% used; 337547786 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 15494963200 available bytes; 99.14% used; 110408610 free inodes.

server2 `/home`: 15494963200 available bytes; 99.14% used; 110408610 free inodes.

server2 `/tmp`: 15494963200 available bytes; 99.14% used; 110408610 free inodes.

server2 `/var/tmp`: 15494963200 available bytes; 99.14% used; 110408610 free inodes.

server2 `/mnt/raid5`: 323553611776 available bytes; 97.76% used; 445077042 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84199821312 available bytes; 95.30% used; 114154966 free inodes.

server3 `/home`: 84199821312 available bytes; 95.30% used; 114154966 free inodes.

server3 `/data`: 142347382784 available bytes; 98.03% used; 225809755 free inodes.

server3 `/tmp`: 84199821312 available bytes; 95.30% used; 114154966 free inodes.

server3 `/var/tmp`: 84199821312 available bytes; 95.30% used; 114154966 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105656053760 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656053760 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231401730048 available bytes; 96.80% used; 224952255 free inodes.

server4 `/tmp`: 105656053760 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656053760 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
