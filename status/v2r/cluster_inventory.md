# V2R cluster inventory

2026-09-25T01:19:36.578103+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319078170624 available bytes; 82.20% used; 112480770 free inodes.

server1 `/home`: 319078170624 available bytes; 82.20% used; 112480770 free inodes.

server1 `/tmp`: 319078170624 available bytes; 82.20% used; 112480770 free inodes.

server1 `/var/tmp`: 319078170624 available bytes; 82.20% used; 112480770 free inodes.

server1 `/mnt/raid5`: 416509353984 available bytes; 98.09% used; 337614179 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23059148800 available bytes; 98.71% used; 110410772 free inodes.

server2 `/home`: 23059148800 available bytes; 98.71% used; 110410772 free inodes.

server2 `/tmp`: 23059148800 available bytes; 98.71% used; 110410772 free inodes.

server2 `/var/tmp`: 23059148800 available bytes; 98.71% used; 110410772 free inodes.

server2 `/mnt/raid5`: 497889337344 available bytes; 96.56% used; 445161946 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84360470528 available bytes; 95.29% used; 114156087 free inodes.

server3 `/home`: 84360470528 available bytes; 95.29% used; 114156087 free inodes.

server3 `/data`: 146870984704 available bytes; 97.97% used; 225812499 free inodes.

server3 `/tmp`: 84360470528 available bytes; 95.29% used; 114156087 free inodes.

server3 `/var/tmp`: 84360470528 available bytes; 95.29% used; 114156087 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105779204096 available bytes; 94.10% used; 114348295 free inodes.

server4 `/home`: 105779204096 available bytes; 94.10% used; 114348295 free inodes.

server4 `/data`: 53323374592 available bytes; 99.26% used; 225030748 free inodes.

server4 `/tmp`: 105779204096 available bytes; 94.10% used; 114348295 free inodes.

server4 `/var/tmp`: 105779204096 available bytes; 94.10% used; 114348295 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
