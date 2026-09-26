# V2R cluster inventory

2026-09-26T04:11:50.965627+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318419451904 available bytes; 82.24% used; 112476273 free inodes.

server1 `/home`: 318419451904 available bytes; 82.24% used; 112476273 free inodes.

server1 `/tmp`: 318419451904 available bytes; 82.24% used; 112476273 free inodes.

server1 `/var/tmp`: 318419451904 available bytes; 82.24% used; 112476273 free inodes.

server1 `/mnt/raid5`: 330556416000 available bytes; 98.48% used; 337545550 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22936596480 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22936596480 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22936596480 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22936596480 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 286012559360 available bytes; 98.02% used; 445051001 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84141195264 available bytes; 95.30% used; 114148302 free inodes.

server3 `/home`: 84141195264 available bytes; 95.30% used; 114148302 free inodes.

server3 `/data`: 124588417024 available bytes; 98.28% used; 225819822 free inodes.

server3 `/tmp`: 84141195264 available bytes; 95.30% used; 114148302 free inodes.

server3 `/var/tmp`: 84141195264 available bytes; 95.30% used; 114148302 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002968576 available bytes; 94.08% used; 114348208 free inodes.

server4 `/home`: 106002968576 available bytes; 94.08% used; 114348208 free inodes.

server4 `/data`: 109671317504 available bytes; 98.48% used; 224929429 free inodes.

server4 `/tmp`: 106002968576 available bytes; 94.08% used; 114348208 free inodes.

server4 `/var/tmp`: 106002968576 available bytes; 94.08% used; 114348208 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
