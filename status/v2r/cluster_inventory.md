# V2R cluster inventory

2026-09-27T09:03:40.694999+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314464792576 available bytes; 82.46% used; 112440730 free inodes.

server1 `/home`: 314464792576 available bytes; 82.46% used; 112440730 free inodes.

server1 `/tmp`: 314464792576 available bytes; 82.46% used; 112440730 free inodes.

server1 `/var/tmp`: 314464792576 available bytes; 82.46% used; 112440730 free inodes.

server1 `/mnt/raid5`: 634581532672 available bytes; 97.09% used; 337400191 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 16649601024 available bytes; 99.07% used; 110357775 free inodes.

server2 `/home`: 16649601024 available bytes; 99.07% used; 110357775 free inodes.

server2 `/tmp`: 16649601024 available bytes; 99.07% used; 110357775 free inodes.

server2 `/var/tmp`: 16649601024 available bytes; 99.07% used; 110357775 free inodes.

server2 `/mnt/raid5`: 574508257280 available bytes; 96.03% used; 444744136 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78557048832 available bytes; 95.62% used; 114062921 free inodes.

server3 `/home`: 78557048832 available bytes; 95.62% used; 114062921 free inodes.

server3 `/data`: 1332582039552 available bytes; 81.58% used; 225762919 free inodes.

server3 `/tmp`: 78557048832 available bytes; 95.62% used; 114062921 free inodes.

server3 `/var/tmp`: 78557048832 available bytes; 95.62% used; 114062921 free inodes.
| server4 | True | ['6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111051206656 available bytes; 93.80% used; 114372864 free inodes.

server4 `/home`: 111051206656 available bytes; 93.80% used; 114372864 free inodes.

server4 `/data`: 364332814336 available bytes; 94.96% used; 224768488 free inodes.

server4 `/tmp`: 111051206656 available bytes; 93.80% used; 114372864 free inodes.

server4 `/var/tmp`: 111051206656 available bytes; 93.80% used; 114372864 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
