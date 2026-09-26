# V2R cluster inventory

2026-09-26T04:05:44.394468+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318415749120 available bytes; 82.24% used; 112476266 free inodes.

server1 `/home`: 318415749120 available bytes; 82.24% used; 112476266 free inodes.

server1 `/tmp`: 318415749120 available bytes; 82.24% used; 112476266 free inodes.

server1 `/var/tmp`: 318415749120 available bytes; 82.24% used; 112476266 free inodes.

server1 `/mnt/raid5`: 330570448896 available bytes; 98.48% used; 337545581 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22930280448 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22930280448 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22930280448 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22930280448 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 285659373568 available bytes; 98.03% used; 445051442 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84141678592 available bytes; 95.30% used; 114148302 free inodes.

server3 `/home`: 84141678592 available bytes; 95.30% used; 114148302 free inodes.

server3 `/data`: 124586573824 available bytes; 98.28% used; 225819930 free inodes.

server3 `/tmp`: 84141678592 available bytes; 95.30% used; 114148302 free inodes.

server3 `/var/tmp`: 84141678592 available bytes; 95.30% used; 114148302 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106003161088 available bytes; 94.08% used; 114348208 free inodes.

server4 `/home`: 106003161088 available bytes; 94.08% used; 114348208 free inodes.

server4 `/data`: 109677019136 available bytes; 98.48% used; 224929430 free inodes.

server4 `/tmp`: 106003161088 available bytes; 94.08% used; 114348208 free inodes.

server4 `/var/tmp`: 106003161088 available bytes; 94.08% used; 114348208 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
