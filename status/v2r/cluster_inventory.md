# V2R cluster inventory

2026-09-25T01:07:14.106072+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319077847040 available bytes; 82.20% used; 112480764 free inodes.

server1 `/home`: 319077847040 available bytes; 82.20% used; 112480764 free inodes.

server1 `/tmp`: 319077847040 available bytes; 82.20% used; 112480764 free inodes.

server1 `/var/tmp`: 319077847040 available bytes; 82.20% used; 112480764 free inodes.

server1 `/mnt/raid5`: 416533532672 available bytes; 98.09% used; 337615626 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23061045248 available bytes; 98.71% used; 110410768 free inodes.

server2 `/home`: 23061045248 available bytes; 98.71% used; 110410768 free inodes.

server2 `/tmp`: 23061045248 available bytes; 98.71% used; 110410768 free inodes.

server2 `/var/tmp`: 23061045248 available bytes; 98.71% used; 110410768 free inodes.

server2 `/mnt/raid5`: 498259034112 available bytes; 96.56% used; 445162192 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353400832 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84353400832 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148261117952 available bytes; 97.95% used; 225812737 free inodes.

server3 `/tmp`: 84353400832 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84353400832 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105779560448 available bytes; 94.10% used; 114348301 free inodes.

server4 `/home`: 105779560448 available bytes; 94.10% used; 114348301 free inodes.

server4 `/data`: 53345083392 available bytes; 99.26% used; 225030816 free inodes.

server4 `/tmp`: 105779560448 available bytes; 94.10% used; 114348301 free inodes.

server4 `/var/tmp`: 105779560448 available bytes; 94.10% used; 114348301 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
