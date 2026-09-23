# V2R cluster inventory

2026-09-23T22:58:17.830908+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325746937856 available bytes; 81.83% used; 112501732 free inodes.

server1 `/home`: 325746937856 available bytes; 81.83% used; 112501732 free inodes.

server1 `/tmp`: 325746937856 available bytes; 81.83% used; 112501732 free inodes.

server1 `/var/tmp`: 325746937856 available bytes; 81.83% used; 112501732 free inodes.

server1 `/mnt/raid5`: 1387999252480 available bytes; 93.63% used; 337739795 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41061650432 available bytes; 97.71% used; 110432601 free inodes.

server2 `/home`: 41061650432 available bytes; 97.71% used; 110432601 free inodes.

server2 `/tmp`: 41061650432 available bytes; 97.71% used; 110432601 free inodes.

server2 `/var/tmp`: 41061650432 available bytes; 97.71% used; 110432601 free inodes.

server2 `/mnt/raid5`: 535464837120 available bytes; 96.30% used; 445206050 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292536688640 available bytes; 83.68% used; 114192878 free inodes.

server3 `/home`: 292536688640 available bytes; 83.68% used; 114192878 free inodes.

server3 `/data`: 82352824320 available bytes; 98.86% used; 225846688 free inodes.

server3 `/tmp`: 292536688640 available bytes; 83.68% used; 114192878 free inodes.

server3 `/var/tmp`: 292536688640 available bytes; 83.68% used; 114192878 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106301100032 available bytes; 94.07% used; 114353515 free inodes.

server4 `/home`: 106301100032 available bytes; 94.07% used; 114353515 free inodes.

server4 `/data`: 300083748864 available bytes; 95.85% used; 225432422 free inodes.

server4 `/tmp`: 106301100032 available bytes; 94.07% used; 114353515 free inodes.

server4 `/var/tmp`: 106301100032 available bytes; 94.07% used; 114353515 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
