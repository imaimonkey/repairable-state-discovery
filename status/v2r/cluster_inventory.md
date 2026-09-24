# V2R cluster inventory

2026-09-24T00:57:13.602269+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325527748608 available bytes; 81.84% used; 112500305 free inodes.

server1 `/home`: 325527748608 available bytes; 81.84% used; 112500305 free inodes.

server1 `/tmp`: 325527748608 available bytes; 81.84% used; 112500305 free inodes.

server1 `/var/tmp`: 325527748608 available bytes; 81.84% used; 112500305 free inodes.

server1 `/mnt/raid5`: 1029047103488 available bytes; 95.28% used; 337734749 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40973365248 available bytes; 97.71% used; 110432226 free inodes.

server2 `/home`: 40973365248 available bytes; 97.71% used; 110432226 free inodes.

server2 `/tmp`: 40973365248 available bytes; 97.71% used; 110432226 free inodes.

server2 `/var/tmp`: 40973365248 available bytes; 97.71% used; 110432226 free inodes.

server2 `/mnt/raid5`: 531953561600 available bytes; 96.32% used; 445202481 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292746375168 available bytes; 83.66% used; 114211807 free inodes.

server3 `/home`: 292746375168 available bytes; 83.66% used; 114211807 free inodes.

server3 `/data`: 82156638208 available bytes; 98.86% used; 225843324 free inodes.

server3 `/tmp`: 292746375168 available bytes; 83.66% used; 114211807 free inodes.

server3 `/var/tmp`: 292746375168 available bytes; 83.66% used; 114211807 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106025635840 available bytes; 94.08% used; 114349625 free inodes.

server4 `/home`: 106025635840 available bytes; 94.08% used; 114349625 free inodes.

server4 `/data`: 292875563008 available bytes; 95.95% used; 225414551 free inodes.

server4 `/tmp`: 106025635840 available bytes; 94.08% used; 114349625 free inodes.

server4 `/var/tmp`: 106025635840 available bytes; 94.08% used; 114349625 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
