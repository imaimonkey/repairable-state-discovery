# V2R cluster inventory

2026-09-25T10:03:16.147304+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318837006336 available bytes; 82.21% used; 112480391 free inodes.

server1 `/home`: 318837006336 available bytes; 82.21% used; 112480391 free inodes.

server1 `/tmp`: 318837006336 available bytes; 82.21% used; 112480391 free inodes.

server1 `/var/tmp`: 318837006336 available bytes; 82.21% used; 112480391 free inodes.

server1 `/mnt/raid5`: 364734976000 available bytes; 98.33% used; 337556983 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22826360832 available bytes; 98.73% used; 110410482 free inodes.

server2 `/home`: 22826360832 available bytes; 98.73% used; 110410482 free inodes.

server2 `/tmp`: 22826360832 available bytes; 98.73% used; 110410482 free inodes.

server2 `/var/tmp`: 22826360832 available bytes; 98.73% used; 110410482 free inodes.

server2 `/mnt/raid5`: 316959035392 available bytes; 97.81% used; 445091331 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84419141632 available bytes; 95.29% used; 114156045 free inodes.

server3 `/home`: 84419141632 available bytes; 95.29% used; 114156045 free inodes.

server3 `/data`: 142236921856 available bytes; 98.03% used; 225810087 free inodes.

server3 `/tmp`: 84419141632 available bytes; 95.29% used; 114156045 free inodes.

server3 `/var/tmp`: 84419141632 available bytes; 95.29% used; 114156045 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105614311424 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614311424 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240015310848 available bytes; 96.68% used; 224991332 free inodes.

server4 `/tmp`: 105614311424 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614311424 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
