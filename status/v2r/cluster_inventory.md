# V2R cluster inventory

2026-09-25T21:19:15.478586+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318703722496 available bytes; 82.22% used; 112476321 free inodes.

server1 `/home`: 318703722496 available bytes; 82.22% used; 112476321 free inodes.

server1 `/tmp`: 318703722496 available bytes; 82.22% used; 112476321 free inodes.

server1 `/var/tmp`: 318703722496 available bytes; 82.22% used; 112476321 free inodes.

server1 `/mnt/raid5`: 351117676544 available bytes; 98.39% used; 337539382 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22896713728 available bytes; 98.72% used; 110405692 free inodes.

server2 `/home`: 22896713728 available bytes; 98.72% used; 110405692 free inodes.

server2 `/tmp`: 22896713728 available bytes; 98.72% used; 110405692 free inodes.

server2 `/var/tmp`: 22896713728 available bytes; 98.72% used; 110405692 free inodes.

server2 `/mnt/raid5`: 301332238336 available bytes; 97.92% used; 445055463 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367196160 available bytes; 95.29% used; 114152628 free inodes.

server3 `/home`: 84367196160 available bytes; 95.29% used; 114152628 free inodes.

server3 `/data`: 125899890688 available bytes; 98.26% used; 225807164 free inodes.

server3 `/tmp`: 84367196160 available bytes; 95.29% used; 114152628 free inodes.

server3 `/var/tmp`: 84367196160 available bytes; 95.29% used; 114152628 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389359104 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389359104 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217848279040 available bytes; 96.99% used; 224920389 free inodes.

server4 `/tmp`: 105389359104 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389359104 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
