# V2R cluster inventory

2026-09-23T23:32:11.430130+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325655101440 available bytes; 81.83% used; 112501473 free inodes.

server1 `/home`: 325655101440 available bytes; 81.83% used; 112501473 free inodes.

server1 `/tmp`: 325655101440 available bytes; 81.83% used; 112501473 free inodes.

server1 `/var/tmp`: 325655101440 available bytes; 81.83% used; 112501473 free inodes.

server1 `/mnt/raid5`: 1367425589248 available bytes; 93.73% used; 337736490 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41036730368 available bytes; 97.71% used; 110432564 free inodes.

server2 `/home`: 41036730368 available bytes; 97.71% used; 110432564 free inodes.

server2 `/tmp`: 41036730368 available bytes; 97.71% used; 110432564 free inodes.

server2 `/var/tmp`: 41036730368 available bytes; 97.71% used; 110432564 free inodes.

server2 `/mnt/raid5`: 534419197952 available bytes; 96.31% used; 445205340 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292866244608 available bytes; 83.66% used; 114214364 free inodes.

server3 `/home`: 292866244608 available bytes; 83.66% used; 114214364 free inodes.

server3 `/data`: 82307952640 available bytes; 98.86% used; 225845743 free inodes.

server3 `/tmp`: 292866244608 available bytes; 83.66% used; 114214364 free inodes.

server3 `/var/tmp`: 292866244608 available bytes; 83.66% used; 114214364 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106216251392 available bytes; 94.07% used; 114352283 free inodes.

server4 `/home`: 106216251392 available bytes; 94.07% used; 114352283 free inodes.

server4 `/data`: 293066514432 available bytes; 95.95% used; 225423333 free inodes.

server4 `/tmp`: 106216251392 available bytes; 94.07% used; 114352283 free inodes.

server4 `/var/tmp`: 106216251392 available bytes; 94.07% used; 114352283 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
