# V2R cluster inventory

2026-09-26T04:19:29.102920+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318410899456 available bytes; 82.24% used; 112476274 free inodes.

server1 `/home`: 318410899456 available bytes; 82.24% used; 112476274 free inodes.

server1 `/tmp`: 318410899456 available bytes; 82.24% used; 112476274 free inodes.

server1 `/var/tmp`: 318410899456 available bytes; 82.24% used; 112476274 free inodes.

server1 `/mnt/raid5`: 330541318144 available bytes; 98.48% used; 337545512 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939529216 available bytes; 98.72% used; 110406206 free inodes.

server2 `/home`: 22939529216 available bytes; 98.72% used; 110406206 free inodes.

server2 `/tmp`: 22939529216 available bytes; 98.72% used; 110406206 free inodes.

server2 `/var/tmp`: 22939529216 available bytes; 98.72% used; 110406206 free inodes.

server2 `/mnt/raid5`: 285266247680 available bytes; 98.03% used; 445050767 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84145143808 available bytes; 95.30% used; 114148308 free inodes.

server3 `/home`: 84145143808 available bytes; 95.30% used; 114148308 free inodes.

server3 `/data`: 124582264832 available bytes; 98.28% used; 225819699 free inodes.

server3 `/tmp`: 84145143808 available bytes; 95.30% used; 114148308 free inodes.

server3 `/var/tmp`: 84145143808 available bytes; 95.30% used; 114148308 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002735104 available bytes; 94.08% used; 114348202 free inodes.

server4 `/home`: 106002735104 available bytes; 94.08% used; 114348202 free inodes.

server4 `/data`: 107388100608 available bytes; 98.52% used; 224929401 free inodes.

server4 `/tmp`: 106002735104 available bytes; 94.08% used; 114348202 free inodes.

server4 `/var/tmp`: 106002735104 available bytes; 94.08% used; 114348202 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
