# V2R cluster inventory

2026-09-24T05:57:49.607625+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324533907456 available bytes; 81.90% used; 112491982 free inodes.

server1 `/home`: 324533907456 available bytes; 81.90% used; 112491982 free inodes.

server1 `/tmp`: 324533907456 available bytes; 81.90% used; 112491982 free inodes.

server1 `/var/tmp`: 324533907456 available bytes; 81.90% used; 112491982 free inodes.

server1 `/mnt/raid5`: 517603934208 available bytes; 97.63% used; 337723843 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57904177152 available bytes; 96.77% used; 110431298 free inodes.

server2 `/home`: 57904177152 available bytes; 96.77% used; 110431298 free inodes.

server2 `/tmp`: 57904177152 available bytes; 96.77% used; 110431298 free inodes.

server2 `/var/tmp`: 57904177152 available bytes; 96.77% used; 110431298 free inodes.

server2 `/mnt/raid5`: 521260433408 available bytes; 96.40% used; 445193155 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127179591680 available bytes; 92.90% used; 114199816 free inodes.

server3 `/home`: 127179591680 available bytes; 92.90% used; 114199816 free inodes.

server3 `/data`: 185857888256 available bytes; 97.43% used; 225838534 free inodes.

server3 `/tmp`: 127179591680 available bytes; 92.90% used; 114199816 free inodes.

server3 `/var/tmp`: 127179591680 available bytes; 92.90% used; 114199816 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105815597056 available bytes; 94.10% used; 114349331 free inodes.

server4 `/home`: 105815597056 available bytes; 94.10% used; 114349331 free inodes.

server4 `/data`: 339830824960 available bytes; 95.30% used; 225374797 free inodes.

server4 `/tmp`: 105815597056 available bytes; 94.10% used; 114349331 free inodes.

server4 `/var/tmp`: 105815597056 available bytes; 94.10% used; 114349331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
