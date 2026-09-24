# V2R cluster inventory

2026-09-24T22:39:13.629945+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323945562112 available bytes; 81.93% used; 112481416 free inodes.

server1 `/home`: 323945562112 available bytes; 81.93% used; 112481416 free inodes.

server1 `/tmp`: 323945562112 available bytes; 81.93% used; 112481416 free inodes.

server1 `/var/tmp`: 323945562112 available bytes; 81.93% used; 112481416 free inodes.

server1 `/mnt/raid5`: 415356084224 available bytes; 98.09% used; 337619274 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23177949184 available bytes; 98.71% used; 110410915 free inodes.

server2 `/home`: 23177949184 available bytes; 98.71% used; 110410915 free inodes.

server2 `/tmp`: 23177949184 available bytes; 98.71% used; 110410915 free inodes.

server2 `/var/tmp`: 23177949184 available bytes; 98.71% used; 110410915 free inodes.

server2 `/mnt/raid5`: 488271339520 available bytes; 96.63% used; 445153133 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84370624512 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84370624512 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 149142941696 available bytes; 97.94% used; 225801911 free inodes.

server3 `/tmp`: 84370624512 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84370624512 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105801678848 available bytes; 94.10% used; 114348324 free inodes.

server4 `/home`: 105801678848 available bytes; 94.10% used; 114348324 free inodes.

server4 `/data`: 66039910400 available bytes; 99.09% used; 225217904 free inodes.

server4 `/tmp`: 105801678848 available bytes; 94.10% used; 114348324 free inodes.

server4 `/var/tmp`: 105801678848 available bytes; 94.10% used; 114348324 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
