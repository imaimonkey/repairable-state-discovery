# V2R cluster inventory

2026-09-26T00:11:56.303875+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318670569472 available bytes; 82.22% used; 112476310 free inodes.

server1 `/home`: 318670569472 available bytes; 82.22% used; 112476310 free inodes.

server1 `/tmp`: 318670569472 available bytes; 82.22% used; 112476310 free inodes.

server1 `/var/tmp`: 318670569472 available bytes; 82.22% used; 112476310 free inodes.

server1 `/mnt/raid5`: 359571812352 available bytes; 98.35% used; 337547066 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22949445632 available bytes; 98.72% used; 110406226 free inodes.

server2 `/home`: 22949445632 available bytes; 98.72% used; 110406226 free inodes.

server2 `/tmp`: 22949445632 available bytes; 98.72% used; 110406226 free inodes.

server2 `/var/tmp`: 22949445632 available bytes; 98.72% used; 110406226 free inodes.

server2 `/mnt/raid5`: 295484837888 available bytes; 97.96% used; 445058063 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342288384 available bytes; 95.29% used; 114152433 free inodes.

server3 `/home`: 84342288384 available bytes; 95.29% used; 114152433 free inodes.

server3 `/data`: 124949221376 available bytes; 98.27% used; 225819365 free inodes.

server3 `/tmp`: 84342288384 available bytes; 95.29% used; 114152433 free inodes.

server3 `/var/tmp`: 84342288384 available bytes; 95.29% used; 114152433 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453801472 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105453801472 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178052108288 available bytes; 97.54% used; 224917555 free inodes.

server4 `/tmp`: 105453801472 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105453801472 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
