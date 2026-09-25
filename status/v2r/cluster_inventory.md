# V2R cluster inventory

2026-09-25T11:05:29.989944+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319063662592 available bytes; 82.20% used; 112478860 free inodes.

server1 `/home`: 319063662592 available bytes; 82.20% used; 112478860 free inodes.

server1 `/tmp`: 319063662592 available bytes; 82.20% used; 112478860 free inodes.

server1 `/var/tmp`: 319063662592 available bytes; 82.20% used; 112478860 free inodes.

server1 `/mnt/raid5`: 370527961088 available bytes; 98.30% used; 337555217 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] |

server2 `/`: 22905749504 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22905749504 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22905749504 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22905749504 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 328935866368 available bytes; 97.73% used; 445088882 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84140158976 available bytes; 95.30% used; 114155494 free inodes.

server3 `/home`: 84140158976 available bytes; 95.30% used; 114155494 free inodes.

server3 `/data`: 142005391360 available bytes; 98.04% used; 225815111 free inodes.

server3 `/tmp`: 84140158976 available bytes; 95.30% used; 114155494 free inodes.

server3 `/var/tmp`: 84140158976 available bytes; 95.30% used; 114155494 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105612324864 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612324864 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238650253312 available bytes; 96.70% used; 224983155 free inodes.

server4 `/tmp`: 105612324864 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612324864 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
