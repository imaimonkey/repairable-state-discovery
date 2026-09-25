# V2R cluster inventory

2026-09-25T07:55:14.253495+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318862106624 available bytes; 82.21% used; 112480375 free inodes.

server1 `/home`: 318862106624 available bytes; 82.21% used; 112480375 free inodes.

server1 `/tmp`: 318862106624 available bytes; 82.21% used; 112480375 free inodes.

server1 `/var/tmp`: 318862106624 available bytes; 82.21% used; 112480375 free inodes.

server1 `/mnt/raid5`: 386637799424 available bytes; 98.23% used; 337557947 free inodes.
| server2 | True | ['0'] | [] |

server2 `/`: 22847713280 available bytes; 98.73% used; 110410483 free inodes.

server2 `/home`: 22847713280 available bytes; 98.73% used; 110410483 free inodes.

server2 `/tmp`: 22847713280 available bytes; 98.73% used; 110410483 free inodes.

server2 `/var/tmp`: 22847713280 available bytes; 98.73% used; 110410483 free inodes.

server2 `/mnt/raid5`: 333820002304 available bytes; 97.69% used; 445095403 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84438155264 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84438155264 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142389698560 available bytes; 98.03% used; 225812277 free inodes.

server3 `/tmp`: 84438155264 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84438155264 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105625702400 available bytes; 94.11% used; 114350336 free inodes.

server4 `/home`: 105625702400 available bytes; 94.11% used; 114350336 free inodes.

server4 `/data`: 249042567168 available bytes; 96.56% used; 225010621 free inodes.

server4 `/tmp`: 105625702400 available bytes; 94.11% used; 114350336 free inodes.

server4 `/var/tmp`: 105625702400 available bytes; 94.11% used; 114350336 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
