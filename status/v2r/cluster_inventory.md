# V2R cluster inventory

2026-09-25T23:04:40.937964+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318692962304 available bytes; 82.22% used; 112476302 free inodes.

server1 `/home`: 318692962304 available bytes; 82.22% used; 112476302 free inodes.

server1 `/tmp`: 318692962304 available bytes; 82.22% used; 112476302 free inodes.

server1 `/var/tmp`: 318692962304 available bytes; 82.22% used; 112476302 free inodes.

server1 `/mnt/raid5`: 360170328064 available bytes; 98.35% used; 337538780 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22952460288 available bytes; 98.72% used; 110406230 free inodes.

server2 `/home`: 22952460288 available bytes; 98.72% used; 110406230 free inodes.

server2 `/tmp`: 22952460288 available bytes; 98.72% used; 110406230 free inodes.

server2 `/var/tmp`: 22952460288 available bytes; 98.72% used; 110406230 free inodes.

server2 `/mnt/raid5`: 297955594240 available bytes; 97.94% used; 445051649 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84354510848 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84354510848 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124757778432 available bytes; 98.28% used; 225805347 free inodes.

server3 `/tmp`: 84354510848 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84354510848 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105159479296 available bytes; 94.13% used; 114346790 free inodes.

server4 `/home`: 105159479296 available bytes; 94.13% used; 114346790 free inodes.

server4 `/data`: 185227276288 available bytes; 97.44% used; 224917658 free inodes.

server4 `/tmp`: 105159479296 available bytes; 94.13% used; 114346790 free inodes.

server4 `/var/tmp`: 105159479296 available bytes; 94.13% used; 114346790 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
