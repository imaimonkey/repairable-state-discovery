# V2R cluster inventory

2026-09-25T10:51:42.243226+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318982156288 available bytes; 82.21% used; 112479390 free inodes.

server1 `/home`: 318982156288 available bytes; 82.21% used; 112479390 free inodes.

server1 `/tmp`: 318982156288 available bytes; 82.21% used; 112479390 free inodes.

server1 `/var/tmp`: 318982156288 available bytes; 82.21% used; 112479390 free inodes.

server1 `/mnt/raid5`: 364802568192 available bytes; 98.33% used; 337555225 free inodes.
| server2 | True | ['1', '2', '3', '5', '6'] | [] |

server2 `/`: 22913359872 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22913359872 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22913359872 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22913359872 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 328274100224 available bytes; 97.73% used; 445089153 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84420616192 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84420616192 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142007238656 available bytes; 98.04% used; 225815370 free inodes.

server3 `/tmp`: 84420616192 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84420616192 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105612726272 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612726272 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238496509952 available bytes; 96.70% used; 224985209 free inodes.

server4 `/tmp`: 105612726272 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612726272 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
