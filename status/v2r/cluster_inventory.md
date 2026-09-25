# V2R cluster inventory

2026-09-25T22:24:37.011189+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318696116224 available bytes; 82.22% used; 112476305 free inodes.

server1 `/home`: 318696116224 available bytes; 82.22% used; 112476305 free inodes.

server1 `/tmp`: 318696116224 available bytes; 82.22% used; 112476305 free inodes.

server1 `/var/tmp`: 318696116224 available bytes; 82.22% used; 112476305 free inodes.

server1 `/mnt/raid5`: 360261672960 available bytes; 98.35% used; 337538979 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22947672064 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22947672064 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22947672064 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22947672064 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 299134173184 available bytes; 97.93% used; 445053111 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84355604480 available bytes; 95.29% used; 114152442 free inodes.

server3 `/home`: 84355604480 available bytes; 95.29% used; 114152442 free inodes.

server3 `/data`: 124830568448 available bytes; 98.27% used; 225806055 free inodes.

server3 `/tmp`: 84355604480 available bytes; 95.29% used; 114152442 free inodes.

server3 `/var/tmp`: 84355604480 available bytes; 95.29% used; 114152442 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105244622848 available bytes; 94.13% used; 114346967 free inodes.

server4 `/home`: 105244622848 available bytes; 94.13% used; 114346967 free inodes.

server4 `/data`: 195119874048 available bytes; 97.30% used; 224917786 free inodes.

server4 `/tmp`: 105244622848 available bytes; 94.13% used; 114346967 free inodes.

server4 `/var/tmp`: 105244622848 available bytes; 94.13% used; 114346967 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
