# V2R cluster inventory

2026-09-27T03:43:28.221564+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315086090240 available bytes; 82.42% used; 112443053 free inodes.

server1 `/home`: 315086090240 available bytes; 82.42% used; 112443053 free inodes.

server1 `/tmp`: 315086090240 available bytes; 82.42% used; 112443053 free inodes.

server1 `/var/tmp`: 315086090240 available bytes; 82.42% used; 112443053 free inodes.

server1 `/mnt/raid5`: 636783091712 available bytes; 97.08% used; 337401379 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17633046528 available bytes; 99.02% used; 110365019 free inodes.

server2 `/home`: 17633046528 available bytes; 99.02% used; 110365019 free inodes.

server2 `/tmp`: 17633046528 available bytes; 99.02% used; 110365019 free inodes.

server2 `/var/tmp`: 17633046528 available bytes; 99.02% used; 110365019 free inodes.

server2 `/mnt/raid5`: 577678123008 available bytes; 96.01% used; 444882388 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78698971136 available bytes; 95.61% used; 114062950 free inodes.

server3 `/home`: 78698971136 available bytes; 95.61% used; 114062950 free inodes.

server3 `/data`: 1335361318912 available bytes; 81.54% used; 225761337 free inodes.

server3 `/tmp`: 78698971136 available bytes; 95.61% used; 114062950 free inodes.

server3 `/var/tmp`: 78698971136 available bytes; 95.61% used; 114062950 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111027826688 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111027826688 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 385466241024 available bytes; 94.67% used; 224780862 free inodes.

server4 `/tmp`: 111027826688 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111027826688 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
