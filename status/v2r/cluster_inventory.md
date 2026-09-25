# V2R cluster inventory

2026-09-25T07:23:58.506799+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318872158208 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318872158208 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318872158208 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318872158208 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 385920798720 available bytes; 98.23% used; 337558474 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22860099584 available bytes; 98.72% used; 110410500 free inodes.

server2 `/home`: 22860099584 available bytes; 98.72% used; 110410500 free inodes.

server2 `/tmp`: 22860099584 available bytes; 98.72% used; 110410500 free inodes.

server2 `/var/tmp`: 22860099584 available bytes; 98.72% used; 110410500 free inodes.

server2 `/mnt/raid5`: 343357636608 available bytes; 97.63% used; 445097508 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 84446568448 available bytes; 95.29% used; 114156032 free inodes.

server3 `/home`: 84446568448 available bytes; 95.29% used; 114156032 free inodes.

server3 `/data`: 142396129280 available bytes; 98.03% used; 225812805 free inodes.

server3 `/tmp`: 84446568448 available bytes; 95.29% used; 114156032 free inodes.

server3 `/var/tmp`: 84446568448 available bytes; 95.29% used; 114156032 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638064128 available bytes; 94.11% used; 114350361 free inodes.

server4 `/home`: 105638064128 available bytes; 94.11% used; 114350361 free inodes.

server4 `/data`: 249108570112 available bytes; 96.56% used; 225015104 free inodes.

server4 `/tmp`: 105638064128 available bytes; 94.11% used; 114350361 free inodes.

server4 `/var/tmp`: 105638064128 available bytes; 94.11% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
