# V2R cluster inventory

2026-09-25T02:45:48.010744+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318958047232 available bytes; 82.21% used; 112480430 free inodes.

server1 `/home`: 318958047232 available bytes; 82.21% used; 112480430 free inodes.

server1 `/tmp`: 318958047232 available bytes; 82.21% used; 112480430 free inodes.

server1 `/var/tmp`: 318958047232 available bytes; 82.21% used; 112480430 free inodes.

server1 `/mnt/raid5`: 416188534784 available bytes; 98.09% used; 337604115 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23006523392 available bytes; 98.72% used; 110410441 free inodes.

server2 `/home`: 23006523392 available bytes; 98.72% used; 110410441 free inodes.

server2 `/tmp`: 23006523392 available bytes; 98.72% used; 110410441 free inodes.

server2 `/var/tmp`: 23006523392 available bytes; 98.72% used; 110410441 free inodes.

server2 `/mnt/raid5`: 482635063296 available bytes; 96.67% used; 445113245 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350201856 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84350201856 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145339084800 available bytes; 97.99% used; 225810957 free inodes.

server3 `/tmp`: 84350201856 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84350201856 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 101969231872 available bytes; 94.31% used; 114350980 free inodes.

server4 `/home`: 101969231872 available bytes; 94.31% used; 114350980 free inodes.

server4 `/data`: 3930972160 available bytes; 99.95% used; 224968787 free inodes.

server4 `/tmp`: 101969231872 available bytes; 94.31% used; 114350980 free inodes.

server4 `/var/tmp`: 101969231872 available bytes; 94.31% used; 114350980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
