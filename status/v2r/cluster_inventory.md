# V2R cluster inventory

2026-09-26T04:30:10.537635+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318407544832 available bytes; 82.24% used; 112476265 free inodes.

server1 `/home`: 318407544832 available bytes; 82.24% used; 112476265 free inodes.

server1 `/tmp`: 318407544832 available bytes; 82.24% used; 112476265 free inodes.

server1 `/var/tmp`: 318407544832 available bytes; 82.24% used; 112476265 free inodes.

server1 `/mnt/raid5`: 330512613376 available bytes; 98.48% used; 337545448 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22930849792 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22930849792 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22930849792 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22930849792 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 285503008768 available bytes; 98.03% used; 445050866 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84140036096 available bytes; 95.30% used; 114148305 free inodes.

server3 `/home`: 84140036096 available bytes; 95.30% used; 114148305 free inodes.

server3 `/data`: 124581748736 available bytes; 98.28% used; 225819521 free inodes.

server3 `/tmp`: 84140036096 available bytes; 95.30% used; 114148305 free inodes.

server3 `/var/tmp`: 84140036096 available bytes; 95.30% used; 114148305 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002432000 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106002432000 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 107084259328 available bytes; 98.52% used; 224929406 free inodes.

server4 `/tmp`: 106002432000 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106002432000 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
