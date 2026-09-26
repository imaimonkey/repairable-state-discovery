# V2R cluster inventory

2026-09-26T00:21:06.726956+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318657216512 available bytes; 82.22% used; 112476288 free inodes.

server1 `/home`: 318657216512 available bytes; 82.22% used; 112476288 free inodes.

server1 `/tmp`: 318657216512 available bytes; 82.22% used; 112476288 free inodes.

server1 `/var/tmp`: 318657216512 available bytes; 82.22% used; 112476288 free inodes.

server1 `/mnt/raid5`: 359512797184 available bytes; 98.35% used; 337547001 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22946787328 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22946787328 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22946787328 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22946787328 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 295884967936 available bytes; 97.96% used; 445058322 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340338688 available bytes; 95.29% used; 114152433 free inodes.

server3 `/home`: 84340338688 available bytes; 95.29% used; 114152433 free inodes.

server3 `/data`: 124943392768 available bytes; 98.27% used; 225819209 free inodes.

server3 `/tmp`: 84340338688 available bytes; 95.29% used; 114152433 free inodes.

server3 `/var/tmp`: 84340338688 available bytes; 95.29% used; 114152433 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453494272 available bytes; 94.12% used; 114348386 free inodes.

server4 `/home`: 105453494272 available bytes; 94.12% used; 114348386 free inodes.

server4 `/data`: 178015518720 available bytes; 97.54% used; 224917534 free inodes.

server4 `/tmp`: 105453494272 available bytes; 94.12% used; 114348386 free inodes.

server4 `/var/tmp`: 105453494272 available bytes; 94.12% used; 114348386 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
