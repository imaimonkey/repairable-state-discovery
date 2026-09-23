# V2R cluster inventory

2026-09-23T23:44:31.149881+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325606236160 available bytes; 81.84% used; 112501109 free inodes.

server1 `/home`: 325606236160 available bytes; 81.84% used; 112501109 free inodes.

server1 `/tmp`: 325606236160 available bytes; 81.84% used; 112501109 free inodes.

server1 `/var/tmp`: 325606236160 available bytes; 81.84% used; 112501109 free inodes.

server1 `/mnt/raid5`: 1332714672128 available bytes; 93.89% used; 337735772 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41034100736 available bytes; 97.71% used; 110432507 free inodes.

server2 `/home`: 41034100736 available bytes; 97.71% used; 110432507 free inodes.

server2 `/tmp`: 41034100736 available bytes; 97.71% used; 110432507 free inodes.

server2 `/var/tmp`: 41034100736 available bytes; 97.71% used; 110432507 free inodes.

server2 `/mnt/raid5`: 534011932672 available bytes; 96.31% used; 445204891 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292491460608 available bytes; 83.68% used; 114191260 free inodes.

server3 `/home`: 292491460608 available bytes; 83.68% used; 114191260 free inodes.

server3 `/data`: 82293248000 available bytes; 98.86% used; 225845157 free inodes.

server3 `/tmp`: 292491460608 available bytes; 83.68% used; 114191260 free inodes.

server3 `/var/tmp`: 292491460608 available bytes; 83.68% used; 114191260 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106182463488 available bytes; 94.07% used; 114351827 free inodes.

server4 `/home`: 106182463488 available bytes; 94.07% used; 114351827 free inodes.

server4 `/data`: 292986257408 available bytes; 95.95% used; 225419595 free inodes.

server4 `/tmp`: 106182463488 available bytes; 94.07% used; 114351827 free inodes.

server4 `/var/tmp`: 106182463488 available bytes; 94.07% used; 114351827 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
