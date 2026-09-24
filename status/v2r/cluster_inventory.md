# V2R cluster inventory

2026-09-24T20:51:13.264137+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323979091968 available bytes; 81.93% used; 112481427 free inodes.

server1 `/home`: 323979091968 available bytes; 81.93% used; 112481427 free inodes.

server1 `/tmp`: 323979091968 available bytes; 81.93% used; 112481427 free inodes.

server1 `/var/tmp`: 323979091968 available bytes; 81.93% used; 112481427 free inodes.

server1 `/mnt/raid5`: 415578701824 available bytes; 98.09% used; 337631988 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30146408448 available bytes; 98.32% used; 110411380 free inodes.

server2 `/home`: 30146408448 available bytes; 98.32% used; 110411380 free inodes.

server2 `/tmp`: 30146408448 available bytes; 98.32% used; 110411380 free inodes.

server2 `/var/tmp`: 30146408448 available bytes; 98.32% used; 110411380 free inodes.

server2 `/mnt/raid5`: 491626188800 available bytes; 96.60% used; 445156305 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84384718848 available bytes; 95.29% used; 114156102 free inodes.

server3 `/home`: 84384718848 available bytes; 95.29% used; 114156102 free inodes.

server3 `/data`: 151119118336 available bytes; 97.91% used; 225803930 free inodes.

server3 `/tmp`: 84384718848 available bytes; 95.29% used; 114156102 free inodes.

server3 `/var/tmp`: 84384718848 available bytes; 95.29% used; 114156102 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639436288 available bytes; 94.10% used; 114348381 free inodes.

server4 `/home`: 105639436288 available bytes; 94.10% used; 114348381 free inodes.

server4 `/data`: 79052394496 available bytes; 98.91% used; 225255903 free inodes.

server4 `/tmp`: 105639436288 available bytes; 94.10% used; 114348381 free inodes.

server4 `/var/tmp`: 105639436288 available bytes; 94.10% used; 114348381 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
