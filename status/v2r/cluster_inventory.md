# V2R cluster inventory

2026-09-25T11:02:26.609922+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319063609344 available bytes; 82.20% used; 112478858 free inodes.

server1 `/home`: 319063609344 available bytes; 82.20% used; 112478858 free inodes.

server1 `/tmp`: 319063609344 available bytes; 82.20% used; 112478858 free inodes.

server1 `/var/tmp`: 319063609344 available bytes; 82.20% used; 112478858 free inodes.

server1 `/mnt/raid5`: 364839686144 available bytes; 98.33% used; 337555172 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] |

server2 `/`: 22911250432 available bytes; 98.72% used; 110409988 free inodes.

server2 `/home`: 22911250432 available bytes; 98.72% used; 110409988 free inodes.

server2 `/tmp`: 22911250432 available bytes; 98.72% used; 110409988 free inodes.

server2 `/var/tmp`: 22911250432 available bytes; 98.72% used; 110409988 free inodes.

server2 `/mnt/raid5`: 329024647168 available bytes; 97.73% used; 445088995 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84501729280 available bytes; 95.28% used; 114155531 free inodes.

server3 `/home`: 84501729280 available bytes; 95.28% used; 114155531 free inodes.

server3 `/data`: 142003044352 available bytes; 98.04% used; 225815163 free inodes.

server3 `/tmp`: 84501729280 available bytes; 95.28% used; 114155531 free inodes.

server3 `/var/tmp`: 84501729280 available bytes; 95.28% used; 114155531 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105612402688 available bytes; 94.11% used; 114350252 free inodes.

server4 `/home`: 105612402688 available bytes; 94.11% used; 114350252 free inodes.

server4 `/data`: 238653538304 available bytes; 96.70% used; 224983418 free inodes.

server4 `/tmp`: 105612402688 available bytes; 94.11% used; 114350252 free inodes.

server4 `/var/tmp`: 105612402688 available bytes; 94.11% used; 114350252 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
