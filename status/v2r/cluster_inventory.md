# V2R cluster inventory

2026-09-24T22:20:44.482965+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323946999808 available bytes; 81.93% used; 112481411 free inodes.

server1 `/home`: 323946999808 available bytes; 81.93% used; 112481411 free inodes.

server1 `/tmp`: 323946999808 available bytes; 81.93% used; 112481411 free inodes.

server1 `/var/tmp`: 323946999808 available bytes; 81.93% used; 112481411 free inodes.

server1 `/mnt/raid5`: 415394611200 available bytes; 98.09% used; 337621429 free inodes.
| server2 | True | [] | [] |

server2 `/`: 27359858688 available bytes; 98.47% used; 110411179 free inodes.

server2 `/home`: 27359858688 available bytes; 98.47% used; 110411179 free inodes.

server2 `/tmp`: 27359858688 available bytes; 98.47% used; 110411179 free inodes.

server2 `/var/tmp`: 27359858688 available bytes; 98.47% used; 110411179 free inodes.

server2 `/mnt/raid5`: 488295190528 available bytes; 96.63% used; 445153262 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84378734592 available bytes; 95.29% used; 114156089 free inodes.

server3 `/home`: 84378734592 available bytes; 95.29% used; 114156089 free inodes.

server3 `/data`: 149430145024 available bytes; 97.93% used; 225802240 free inodes.

server3 `/tmp`: 84378734592 available bytes; 95.29% used; 114156089 free inodes.

server3 `/var/tmp`: 84378734592 available bytes; 95.29% used; 114156089 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810599936 available bytes; 94.10% used; 114348324 free inodes.

server4 `/home`: 105810599936 available bytes; 94.10% used; 114348324 free inodes.

server4 `/data`: 73362186240 available bytes; 98.99% used; 225230631 free inodes.

server4 `/tmp`: 105810599936 available bytes; 94.10% used; 114348324 free inodes.

server4 `/var/tmp`: 105810599936 available bytes; 94.10% used; 114348324 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
