# V2R cluster inventory

2026-09-26T00:19:35.088300+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318660132864 available bytes; 82.22% used; 112476290 free inodes.

server1 `/home`: 318660132864 available bytes; 82.22% used; 112476290 free inodes.

server1 `/tmp`: 318660132864 available bytes; 82.22% used; 112476290 free inodes.

server1 `/var/tmp`: 318660132864 available bytes; 82.22% used; 112476290 free inodes.

server1 `/mnt/raid5`: 359518359552 available bytes; 98.35% used; 337547019 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22947110912 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22947110912 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22947110912 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22947110912 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 295388393472 available bytes; 97.96% used; 445058239 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340731904 available bytes; 95.29% used; 114152433 free inodes.

server3 `/home`: 84340731904 available bytes; 95.29% used; 114152433 free inodes.

server3 `/data`: 124943306752 available bytes; 98.27% used; 225819222 free inodes.

server3 `/tmp`: 84340731904 available bytes; 95.29% used; 114152433 free inodes.

server3 `/var/tmp`: 84340731904 available bytes; 95.29% used; 114152433 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453551616 available bytes; 94.12% used; 114348386 free inodes.

server4 `/home`: 105453551616 available bytes; 94.12% used; 114348386 free inodes.

server4 `/data`: 178011504640 available bytes; 97.54% used; 224917533 free inodes.

server4 `/tmp`: 105453551616 available bytes; 94.12% used; 114348386 free inodes.

server4 `/var/tmp`: 105453551616 available bytes; 94.12% used; 114348386 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
