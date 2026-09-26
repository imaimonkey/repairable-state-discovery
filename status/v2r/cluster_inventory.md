# V2R cluster inventory

2026-09-26T22:11:07.114905+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315468267520 available bytes; 82.40% used; 112445697 free inodes.

server1 `/home`: 315468267520 available bytes; 82.40% used; 112445697 free inodes.

server1 `/tmp`: 315468267520 available bytes; 82.40% used; 112445697 free inodes.

server1 `/var/tmp`: 315468267520 available bytes; 82.40% used; 112445697 free inodes.

server1 `/mnt/raid5`: 645856088064 available bytes; 97.04% used; 337467237 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17949167616 available bytes; 99.00% used; 110367525 free inodes.

server2 `/home`: 17949167616 available bytes; 99.00% used; 110367525 free inodes.

server2 `/tmp`: 17949167616 available bytes; 99.00% used; 110367525 free inodes.

server2 `/var/tmp`: 17949167616 available bytes; 99.00% used; 110367525 free inodes.

server2 `/mnt/raid5`: 597065666560 available bytes; 95.87% used; 444961745 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81085665280 available bytes; 95.48% used; 114069867 free inodes.

server3 `/home`: 81085665280 available bytes; 95.48% used; 114069867 free inodes.

server3 `/data`: 1349258932224 available bytes; 81.35% used; 225827261 free inodes.

server3 `/tmp`: 81085665280 available bytes; 95.48% used; 114069867 free inodes.

server3 `/var/tmp`: 81085665280 available bytes; 95.48% used; 114069867 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105899671552 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105899671552 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409653125120 available bytes; 94.34% used; 224823833 free inodes.

server4 `/tmp`: 105899671552 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105899671552 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
