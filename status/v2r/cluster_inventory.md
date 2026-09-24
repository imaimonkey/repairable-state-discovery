# V2R cluster inventory

2026-09-24T01:17:22.261626+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325474873344 available bytes; 81.84% used; 112499853 free inodes.

server1 `/home`: 325474873344 available bytes; 81.84% used; 112499853 free inodes.

server1 `/tmp`: 325474873344 available bytes; 81.84% used; 112499853 free inodes.

server1 `/var/tmp`: 325474873344 available bytes; 81.84% used; 112499853 free inodes.

server1 `/mnt/raid5`: 927984783360 available bytes; 95.74% used; 337734115 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40954056704 available bytes; 97.72% used; 110432091 free inodes.

server2 `/home`: 40954056704 available bytes; 97.72% used; 110432091 free inodes.

server2 `/tmp`: 40954056704 available bytes; 97.72% used; 110432091 free inodes.

server2 `/var/tmp`: 40954056704 available bytes; 97.72% used; 110432091 free inodes.

server2 `/mnt/raid5`: 531352133632 available bytes; 96.33% used; 445202246 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292210679808 available bytes; 83.69% used; 114183508 free inodes.

server3 `/home`: 292210679808 available bytes; 83.69% used; 114183508 free inodes.

server3 `/data`: 82065842176 available bytes; 98.87% used; 225842579 free inodes.

server3 `/tmp`: 292210679808 available bytes; 83.69% used; 114183508 free inodes.

server3 `/var/tmp`: 292210679808 available bytes; 83.69% used; 114183508 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105991393280 available bytes; 94.09% used; 114349079 free inodes.

server4 `/home`: 105991393280 available bytes; 94.09% used; 114349079 free inodes.

server4 `/data`: 290836631552 available bytes; 95.98% used; 225397018 free inodes.

server4 `/tmp`: 105991393280 available bytes; 94.09% used; 114349079 free inodes.

server4 `/var/tmp`: 105991393280 available bytes; 94.09% used; 114349079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
