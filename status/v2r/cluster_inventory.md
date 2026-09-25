# V2R cluster inventory

2026-09-25T21:07:01.990897+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318697738240 available bytes; 82.22% used; 112476315 free inodes.

server1 `/home`: 318697738240 available bytes; 82.22% used; 112476315 free inodes.

server1 `/tmp`: 318697738240 available bytes; 82.22% used; 112476315 free inodes.

server1 `/var/tmp`: 318697738240 available bytes; 82.22% used; 112476315 free inodes.

server1 `/mnt/raid5`: 368603762688 available bytes; 98.31% used; 337539495 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22889619456 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22889619456 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22889619456 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22889619456 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 302216261632 available bytes; 97.91% used; 445055851 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84366409728 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84366409728 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 126045417472 available bytes; 98.26% used; 225807407 free inodes.

server3 `/tmp`: 84366409728 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84366409728 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105414766592 available bytes; 94.12% used; 114347366 free inodes.

server4 `/home`: 105414766592 available bytes; 94.12% used; 114347366 free inodes.

server4 `/data`: 218510508032 available bytes; 96.98% used; 224920841 free inodes.

server4 `/tmp`: 105414766592 available bytes; 94.12% used; 114347366 free inodes.

server4 `/var/tmp`: 105414766592 available bytes; 94.12% used; 114347366 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
