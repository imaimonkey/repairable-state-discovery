# V2R cluster inventory

2026-09-23T22:25:57.729653+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325705986048 available bytes; 81.83% used; 112501400 free inodes.

server1 `/home`: 325705986048 available bytes; 81.83% used; 112501400 free inodes.

server1 `/tmp`: 325705986048 available bytes; 81.83% used; 112501400 free inodes.

server1 `/var/tmp`: 325705986048 available bytes; 81.83% used; 112501400 free inodes.

server1 `/mnt/raid5`: 1388098785280 available bytes; 93.63% used; 337739839 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41082920960 available bytes; 97.71% used; 110432643 free inodes.

server2 `/home`: 41082920960 available bytes; 97.71% used; 110432643 free inodes.

server2 `/tmp`: 41082920960 available bytes; 97.71% used; 110432643 free inodes.

server2 `/var/tmp`: 41082920960 available bytes; 97.71% used; 110432643 free inodes.

server2 `/mnt/raid5`: 536282406912 available bytes; 96.29% used; 445206994 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292731633664 available bytes; 83.66% used; 114201996 free inodes.

server3 `/home`: 292731633664 available bytes; 83.66% used; 114201996 free inodes.

server3 `/data`: 82433990656 available bytes; 98.86% used; 225847439 free inodes.

server3 `/tmp`: 292731633664 available bytes; 83.66% used; 114201996 free inodes.

server3 `/var/tmp`: 292731633664 available bytes; 83.66% used; 114201996 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106391580672 available bytes; 94.06% used; 114354691 free inodes.

server4 `/home`: 106391580672 available bytes; 94.06% used; 114354691 free inodes.

server4 `/data`: 300090224640 available bytes; 95.85% used; 225437955 free inodes.

server4 `/tmp`: 106391580672 available bytes; 94.06% used; 114354691 free inodes.

server4 `/var/tmp`: 106391580672 available bytes; 94.06% used; 114354691 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
