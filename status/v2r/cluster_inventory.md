# V2R cluster inventory

2026-09-24T05:52:36.961368+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324526669824 available bytes; 81.90% used; 112492025 free inodes.

server1 `/home`: 324526669824 available bytes; 81.90% used; 112492025 free inodes.

server1 `/tmp`: 324526669824 available bytes; 81.90% used; 112492025 free inodes.

server1 `/var/tmp`: 324526669824 available bytes; 81.90% used; 112492025 free inodes.

server1 `/mnt/raid5`: 517609054208 available bytes; 97.63% used; 337723874 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57906540544 available bytes; 96.77% used; 110431316 free inodes.

server2 `/home`: 57906540544 available bytes; 96.77% used; 110431316 free inodes.

server2 `/tmp`: 57906540544 available bytes; 96.77% used; 110431316 free inodes.

server2 `/var/tmp`: 57906540544 available bytes; 96.77% used; 110431316 free inodes.

server2 `/mnt/raid5`: 521687793664 available bytes; 96.40% used; 445193219 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126806519808 available bytes; 92.92% used; 114175505 free inodes.

server3 `/home`: 126806519808 available bytes; 92.92% used; 114175505 free inodes.

server3 `/data`: 185877442560 available bytes; 97.43% used; 225838634 free inodes.

server3 `/tmp`: 126806519808 available bytes; 92.92% used; 114175505 free inodes.

server3 `/var/tmp`: 126806519808 available bytes; 92.92% used; 114175505 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105815879680 available bytes; 94.10% used; 114349341 free inodes.

server4 `/home`: 105815879680 available bytes; 94.10% used; 114349341 free inodes.

server4 `/data`: 252144214016 available bytes; 96.52% used; 225357937 free inodes.

server4 `/tmp`: 105815879680 available bytes; 94.10% used; 114349341 free inodes.

server4 `/var/tmp`: 105815879680 available bytes; 94.10% used; 114349341 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
