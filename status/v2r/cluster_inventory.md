# V2R cluster inventory

2026-09-25T10:01:44.424175+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318837374976 available bytes; 82.21% used; 112480391 free inodes.

server1 `/home`: 318837374976 available bytes; 82.21% used; 112480391 free inodes.

server1 `/tmp`: 318837374976 available bytes; 82.21% used; 112480391 free inodes.

server1 `/var/tmp`: 318837374976 available bytes; 82.21% used; 112480391 free inodes.

server1 `/mnt/raid5`: 364735610880 available bytes; 98.33% used; 337556980 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22826815488 available bytes; 98.73% used; 110410482 free inodes.

server2 `/home`: 22826815488 available bytes; 98.73% used; 110410482 free inodes.

server2 `/tmp`: 22826815488 available bytes; 98.73% used; 110410482 free inodes.

server2 `/var/tmp`: 22826815488 available bytes; 98.73% used; 110410482 free inodes.

server2 `/mnt/raid5`: 317006798848 available bytes; 97.81% used; 445091503 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84418207744 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84418207744 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142237257728 available bytes; 98.03% used; 225810105 free inodes.

server3 `/tmp`: 84418207744 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84418207744 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105614348288 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614348288 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240019066880 available bytes; 96.68% used; 224991508 free inodes.

server4 `/tmp`: 105614348288 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614348288 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
