# V2R cluster inventory

2026-09-23T23:10:37.873346+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325672411136 available bytes; 81.83% used; 112501640 free inodes.

server1 `/home`: 325672411136 available bytes; 81.83% used; 112501640 free inodes.

server1 `/tmp`: 325672411136 available bytes; 81.83% used; 112501640 free inodes.

server1 `/var/tmp`: 325672411136 available bytes; 81.83% used; 112501640 free inodes.

server1 `/mnt/raid5`: 1387994406912 available bytes; 93.63% used; 337739778 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41059512320 available bytes; 97.71% used; 110432610 free inodes.

server2 `/home`: 41059512320 available bytes; 97.71% used; 110432610 free inodes.

server2 `/tmp`: 41059512320 available bytes; 97.71% used; 110432610 free inodes.

server2 `/var/tmp`: 41059512320 available bytes; 97.71% used; 110432610 free inodes.

server2 `/mnt/raid5`: 535093760000 available bytes; 96.30% used; 445206339 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292257341440 available bytes; 83.69% used; 114170902 free inodes.

server3 `/home`: 292257341440 available bytes; 83.69% used; 114170902 free inodes.

server3 `/data`: 82340491264 available bytes; 98.86% used; 225846469 free inodes.

server3 `/tmp`: 292257341440 available bytes; 83.69% used; 114170902 free inodes.

server3 `/var/tmp`: 292257341440 available bytes; 83.69% used; 114170902 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106273038336 available bytes; 94.07% used; 114353067 free inodes.

server4 `/home`: 106273038336 available bytes; 94.07% used; 114353067 free inodes.

server4 `/data`: 300043329536 available bytes; 95.85% used; 225430135 free inodes.

server4 `/tmp`: 106273038336 available bytes; 94.07% used; 114353067 free inodes.

server4 `/var/tmp`: 106273038336 available bytes; 94.07% used; 114353067 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
