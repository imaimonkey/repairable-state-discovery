# V2R cluster inventory

2026-09-25T22:05:06.010415+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318695190528 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318695190528 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318695190528 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318695190528 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 360297234432 available bytes; 98.35% used; 337539059 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22905094144 available bytes; 98.72% used; 110405688 free inodes.

server2 `/home`: 22905094144 available bytes; 98.72% used; 110405688 free inodes.

server2 `/tmp`: 22905094144 available bytes; 98.72% used; 110405688 free inodes.

server2 `/var/tmp`: 22905094144 available bytes; 98.72% used; 110405688 free inodes.

server2 `/mnt/raid5`: 300136853504 available bytes; 97.93% used; 445054074 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84360286208 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84360286208 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 125878587392 available bytes; 98.26% used; 225806395 free inodes.

server3 `/tmp`: 84360286208 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84360286208 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105312395264 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105312395264 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208748068864 available bytes; 97.12% used; 224919071 free inodes.

server4 `/tmp`: 105312395264 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105312395264 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
