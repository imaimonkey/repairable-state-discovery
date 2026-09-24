# V2R cluster inventory

2026-09-24T17:56:57.027261+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324005306368 available bytes; 81.92% used; 112481435 free inodes.

server1 `/home`: 324005306368 available bytes; 81.92% used; 112481435 free inodes.

server1 `/tmp`: 324005306368 available bytes; 81.92% used; 112481435 free inodes.

server1 `/var/tmp`: 324005306368 available bytes; 81.92% used; 112481435 free inodes.

server1 `/mnt/raid5`: 416384995328 available bytes; 98.09% used; 337643248 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 56899223552 available bytes; 96.83% used; 110412316 free inodes.

server2 `/home`: 56899223552 available bytes; 96.83% used; 110412316 free inodes.

server2 `/tmp`: 56899223552 available bytes; 96.83% used; 110412316 free inodes.

server2 `/var/tmp`: 56899223552 available bytes; 96.83% used; 110412316 free inodes.

server2 `/mnt/raid5`: 498036748288 available bytes; 96.56% used; 445161560 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84407259136 available bytes; 95.29% used; 114156134 free inodes.

server3 `/home`: 84407259136 available bytes; 95.29% used; 114156134 free inodes.

server3 `/data`: 151824945152 available bytes; 97.90% used; 225786309 free inodes.

server3 `/tmp`: 84407259136 available bytes; 95.29% used; 114156134 free inodes.

server3 `/var/tmp`: 84407259136 available bytes; 95.29% used; 114156134 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105672163328 available bytes; 94.10% used; 114348541 free inodes.

server4 `/home`: 105672163328 available bytes; 94.10% used; 114348541 free inodes.

server4 `/data`: 88690520064 available bytes; 98.77% used; 225253559 free inodes.

server4 `/tmp`: 105672163328 available bytes; 94.10% used; 114348541 free inodes.

server4 `/var/tmp`: 105672163328 available bytes; 94.10% used; 114348541 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
