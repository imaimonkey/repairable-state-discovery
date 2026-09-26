# V2R cluster inventory

2026-09-26T00:34:51.523177+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318651584512 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318651584512 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318651584512 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318651584512 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 345623216128 available bytes; 98.41% used; 337546814 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22942814208 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22942814208 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22942814208 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22942814208 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 294947123200 available bytes; 97.96% used; 445057646 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339359744 available bytes; 95.29% used; 114152439 free inodes.

server3 `/home`: 84339359744 available bytes; 95.29% used; 114152439 free inodes.

server3 `/data`: 124942594048 available bytes; 98.27% used; 225818954 free inodes.

server3 `/tmp`: 84339359744 available bytes; 95.29% used; 114152439 free inodes.

server3 `/var/tmp`: 84339359744 available bytes; 95.29% used; 114152439 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105349640192 available bytes; 94.12% used; 114347249 free inodes.

server4 `/home`: 105349640192 available bytes; 94.12% used; 114347249 free inodes.

server4 `/data`: 160107241472 available bytes; 97.79% used; 224917406 free inodes.

server4 `/tmp`: 105349640192 available bytes; 94.12% used; 114347249 free inodes.

server4 `/var/tmp`: 105349640192 available bytes; 94.12% used; 114347249 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
