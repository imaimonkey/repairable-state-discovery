# V2R cluster inventory

2026-09-26T20:33:33.231461+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315481096192 available bytes; 82.40% used; 112444696 free inodes.

server1 `/home`: 315481096192 available bytes; 82.40% used; 112444696 free inodes.

server1 `/tmp`: 315481096192 available bytes; 82.40% used; 112444696 free inodes.

server1 `/var/tmp`: 315481096192 available bytes; 82.40% used; 112444696 free inodes.

server1 `/mnt/raid5`: 645855952896 available bytes; 97.04% used; 337467125 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17981620224 available bytes; 99.00% used; 110367110 free inodes.

server2 `/home`: 17981620224 available bytes; 99.00% used; 110367110 free inodes.

server2 `/tmp`: 17981620224 available bytes; 99.00% used; 110367110 free inodes.

server2 `/var/tmp`: 17981620224 available bytes; 99.00% used; 110367110 free inodes.

server2 `/mnt/raid5`: 600049414144 available bytes; 95.85% used; 444964698 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81263124480 available bytes; 95.47% used; 114065295 free inodes.

server3 `/home`: 81263124480 available bytes; 95.47% used; 114065295 free inodes.

server3 `/data`: 1348613443584 available bytes; 81.36% used; 225831710 free inodes.

server3 `/tmp`: 81263124480 available bytes; 95.47% used; 114065295 free inodes.

server3 `/var/tmp`: 81263124480 available bytes; 95.47% used; 114065295 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918976000 available bytes; 94.09% used; 114347833 free inodes.

server4 `/home`: 105918976000 available bytes; 94.09% used; 114347833 free inodes.

server4 `/data`: 410199891968 available bytes; 94.33% used; 224823722 free inodes.

server4 `/tmp`: 105918976000 available bytes; 94.09% used; 114347833 free inodes.

server4 `/var/tmp`: 105918976000 available bytes; 94.09% used; 114347833 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
