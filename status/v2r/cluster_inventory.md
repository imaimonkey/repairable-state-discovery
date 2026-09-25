# V2R cluster inventory

2026-09-25T21:20:47.123064+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318703710208 available bytes; 82.22% used; 112476327 free inodes.

server1 `/home`: 318703710208 available bytes; 82.22% used; 112476327 free inodes.

server1 `/tmp`: 318703710208 available bytes; 82.22% used; 112476327 free inodes.

server1 `/var/tmp`: 318703710208 available bytes; 82.22% used; 112476327 free inodes.

server1 `/mnt/raid5`: 327037153280 available bytes; 98.50% used; 337539378 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22896390144 available bytes; 98.72% used; 110405692 free inodes.

server2 `/home`: 22896390144 available bytes; 98.72% used; 110405692 free inodes.

server2 `/tmp`: 22896390144 available bytes; 98.72% used; 110405692 free inodes.

server2 `/var/tmp`: 22896390144 available bytes; 98.72% used; 110405692 free inodes.

server2 `/mnt/raid5`: 301818912768 available bytes; 97.91% used; 445055329 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84366741504 available bytes; 95.29% used; 114152628 free inodes.

server3 `/home`: 84366741504 available bytes; 95.29% used; 114152628 free inodes.

server3 `/data`: 125904711680 available bytes; 98.26% used; 225807153 free inodes.

server3 `/tmp`: 84366741504 available bytes; 95.29% used; 114152628 free inodes.

server3 `/var/tmp`: 84366741504 available bytes; 95.29% used; 114152628 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389301760 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389301760 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217853378560 available bytes; 96.99% used; 224920383 free inodes.

server4 `/tmp`: 105389301760 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389301760 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
