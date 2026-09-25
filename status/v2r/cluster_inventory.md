# V2R cluster inventory

2026-09-25T02:25:48.741945+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318969663488 available bytes; 82.21% used; 112480501 free inodes.

server1 `/home`: 318969663488 available bytes; 82.21% used; 112480501 free inodes.

server1 `/tmp`: 318969663488 available bytes; 82.21% used; 112480501 free inodes.

server1 `/var/tmp`: 318969663488 available bytes; 82.21% used; 112480501 free inodes.

server1 `/mnt/raid5`: 416224415744 available bytes; 98.09% used; 337606437 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23016861696 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 23016861696 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 23016861696 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 23016861696 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 483550478336 available bytes; 96.66% used; 445113994 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352471040 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84352471040 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145672704000 available bytes; 97.99% used; 225811124 free inodes.

server3 `/tmp`: 84352471040 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84352471040 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['1', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105895972864 available bytes; 94.09% used; 114350978 free inodes.

server4 `/home`: 105895972864 available bytes; 94.09% used; 114350978 free inodes.

server4 `/data`: 31194071040 available bytes; 99.57% used; 224969761 free inodes.

server4 `/tmp`: 105895972864 available bytes; 94.09% used; 114350978 free inodes.

server4 `/var/tmp`: 105895972864 available bytes; 94.09% used; 114350978 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
