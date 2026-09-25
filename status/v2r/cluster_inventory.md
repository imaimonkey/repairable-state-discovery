# V2R cluster inventory

2026-09-25T20:45:38.141994+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318709424128 available bytes; 82.22% used; 112476310 free inodes.

server1 `/home`: 318709424128 available bytes; 82.22% used; 112476310 free inodes.

server1 `/tmp`: 318709424128 available bytes; 82.22% used; 112476310 free inodes.

server1 `/var/tmp`: 318709424128 available bytes; 82.22% used; 112476310 free inodes.

server1 `/mnt/raid5`: 368646443008 available bytes; 98.31% used; 337539586 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 22947090432 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22947090432 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22947090432 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22947090432 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 302852710400 available bytes; 97.91% used; 445057019 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 84380975104 available bytes; 95.29% used; 114152634 free inodes.

server3 `/home`: 84380975104 available bytes; 95.29% used; 114152634 free inodes.

server3 `/data`: 127105720320 available bytes; 98.24% used; 225807784 free inodes.

server3 `/tmp`: 84380975104 available bytes; 95.29% used; 114152634 free inodes.

server3 `/var/tmp`: 84380975104 available bytes; 95.29% used; 114152634 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655652352 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655652352 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228183437312 available bytes; 96.85% used; 224928304 free inodes.

server4 `/tmp`: 105655652352 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655652352 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
