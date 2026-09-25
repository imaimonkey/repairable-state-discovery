# V2R cluster inventory

2026-09-25T23:47:00.866622+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318672867328 available bytes; 82.22% used; 112476305 free inodes.

server1 `/home`: 318672867328 available bytes; 82.22% used; 112476305 free inodes.

server1 `/tmp`: 318672867328 available bytes; 82.22% used; 112476305 free inodes.

server1 `/var/tmp`: 318672867328 available bytes; 82.22% used; 112476305 free inodes.

server1 `/mnt/raid5`: 360076378112 available bytes; 98.35% used; 337538571 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22949462016 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22949462016 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22949462016 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22949462016 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 296530386944 available bytes; 97.95% used; 445050505 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84350742528 available bytes; 95.29% used; 114152442 free inodes.

server3 `/home`: 84350742528 available bytes; 95.29% used; 114152442 free inodes.

server3 `/data`: 124802011136 available bytes; 98.28% used; 225811180 free inodes.

server3 `/tmp`: 84350742528 available bytes; 95.29% used; 114152442 free inodes.

server3 `/var/tmp`: 84350742528 available bytes; 95.29% used; 114152442 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105082630144 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082630144 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178218504192 available bytes; 97.54% used; 224917593 free inodes.

server4 `/tmp`: 105082630144 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082630144 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
