# V2R cluster inventory

2026-09-24T02:58:47.147422+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325376188416 available bytes; 81.85% used; 112498543 free inodes.

server1 `/home`: 325376188416 available bytes; 81.85% used; 112498543 free inodes.

server1 `/tmp`: 325376188416 available bytes; 81.85% used; 112498543 free inodes.

server1 `/var/tmp`: 325376188416 available bytes; 81.85% used; 112498543 free inodes.

server1 `/mnt/raid5`: 521146839040 available bytes; 97.61% used; 337732250 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40863940608 available bytes; 97.72% used; 110431338 free inodes.

server2 `/home`: 40863940608 available bytes; 97.72% used; 110431338 free inodes.

server2 `/tmp`: 40863940608 available bytes; 97.72% used; 110431338 free inodes.

server2 `/var/tmp`: 40863940608 available bytes; 97.72% used; 110431338 free inodes.

server2 `/mnt/raid5`: 528130670592 available bytes; 96.35% used; 445198640 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292287094784 available bytes; 83.69% used; 114186960 free inodes.

server3 `/home`: 292287094784 available bytes; 83.69% used; 114186960 free inodes.

server3 `/data`: 39707033600 available bytes; 99.45% used; 225845378 free inodes.

server3 `/tmp`: 292287094784 available bytes; 83.69% used; 114186960 free inodes.

server3 `/var/tmp`: 292287094784 available bytes; 83.69% used; 114186960 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105996857344 available bytes; 94.08% used; 114349629 free inodes.

server4 `/home`: 105996857344 available bytes; 94.08% used; 114349629 free inodes.

server4 `/data`: 289713225728 available bytes; 96.00% used; 225386863 free inodes.

server4 `/tmp`: 105996857344 available bytes; 94.08% used; 114349629 free inodes.

server4 `/var/tmp`: 105996857344 available bytes; 94.08% used; 114349629 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
