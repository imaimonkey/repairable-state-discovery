# V2R cluster inventory

2026-09-24T02:13:22.373094+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325439713280 available bytes; 81.84% used; 112499173 free inodes.

server1 `/home`: 325439713280 available bytes; 81.84% used; 112499173 free inodes.

server1 `/tmp`: 325439713280 available bytes; 81.84% used; 112499173 free inodes.

server1 `/var/tmp`: 325439713280 available bytes; 81.84% used; 112499173 free inodes.

server1 `/mnt/raid5`: 718603436032 available bytes; 96.70% used; 337733492 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40907169792 available bytes; 97.72% used; 110431658 free inodes.

server2 `/home`: 40907169792 available bytes; 97.72% used; 110431658 free inodes.

server2 `/tmp`: 40907169792 available bytes; 97.72% used; 110431658 free inodes.

server2 `/var/tmp`: 40907169792 available bytes; 97.72% used; 110431658 free inodes.

server2 `/mnt/raid5`: 529537994752 available bytes; 96.34% used; 445200145 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292684464128 available bytes; 83.67% used; 114210519 free inodes.

server3 `/home`: 292684464128 available bytes; 83.67% used; 114210519 free inodes.

server3 `/data`: 18079346688 available bytes; 99.75% used; 225841264 free inodes.

server3 `/tmp`: 292684464128 available bytes; 83.67% used; 114210519 free inodes.

server3 `/var/tmp`: 292684464128 available bytes; 83.67% used; 114210519 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105932386304 available bytes; 94.09% used; 114348278 free inodes.

server4 `/home`: 105932386304 available bytes; 94.09% used; 114348278 free inodes.

server4 `/data`: 289760403456 available bytes; 96.00% used; 225388458 free inodes.

server4 `/tmp`: 105932386304 available bytes; 94.09% used; 114348278 free inodes.

server4 `/var/tmp`: 105932386304 available bytes; 94.09% used; 114348278 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
