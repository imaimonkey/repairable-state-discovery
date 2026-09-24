# V2R cluster inventory

2026-09-24T22:37:34.879048+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323948814336 available bytes; 81.93% used; 112481417 free inodes.

server1 `/home`: 323948814336 available bytes; 81.93% used; 112481417 free inodes.

server1 `/tmp`: 323948814336 available bytes; 81.93% used; 112481417 free inodes.

server1 `/var/tmp`: 323948814336 available bytes; 81.93% used; 112481417 free inodes.

server1 `/mnt/raid5`: 415363776512 available bytes; 98.09% used; 337619462 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23178465280 available bytes; 98.71% used; 110410907 free inodes.

server2 `/home`: 23178465280 available bytes; 98.71% used; 110410907 free inodes.

server2 `/tmp`: 23178465280 available bytes; 98.71% used; 110410907 free inodes.

server2 `/var/tmp`: 23178465280 available bytes; 98.71% used; 110410907 free inodes.

server2 `/mnt/raid5`: 488326324224 available bytes; 96.63% used; 445153310 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84379521024 available bytes; 95.29% used; 114156069 free inodes.

server3 `/home`: 84379521024 available bytes; 95.29% used; 114156069 free inodes.

server3 `/data`: 149169688576 available bytes; 97.94% used; 225801947 free inodes.

server3 `/tmp`: 84379521024 available bytes; 95.29% used; 114156069 free inodes.

server3 `/var/tmp`: 84379521024 available bytes; 95.29% used; 114156069 free inodes.
| server4 | True | ['0', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105801732096 available bytes; 94.10% used; 114348326 free inodes.

server4 `/home`: 105801732096 available bytes; 94.10% used; 114348326 free inodes.

server4 `/data`: 73206902784 available bytes; 98.99% used; 225219619 free inodes.

server4 `/tmp`: 105801732096 available bytes; 94.10% used; 114348326 free inodes.

server4 `/var/tmp`: 105801732096 available bytes; 94.10% used; 114348326 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
