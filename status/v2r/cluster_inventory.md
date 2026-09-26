# V2R cluster inventory

2026-09-26T04:13:22.562043+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318410723328 available bytes; 82.24% used; 112476273 free inodes.

server1 `/home`: 318410723328 available bytes; 82.24% used; 112476273 free inodes.

server1 `/tmp`: 318410723328 available bytes; 82.24% used; 112476273 free inodes.

server1 `/var/tmp`: 318410723328 available bytes; 82.24% used; 112476273 free inodes.

server1 `/mnt/raid5`: 330553229312 available bytes; 98.48% used; 337545540 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22937382912 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22937382912 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22937382912 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22937382912 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 285980442624 available bytes; 98.02% used; 445051216 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84145098752 available bytes; 95.30% used; 114148304 free inodes.

server3 `/home`: 84145098752 available bytes; 95.30% used; 114148304 free inodes.

server3 `/data`: 124587655168 available bytes; 98.28% used; 225819805 free inodes.

server3 `/tmp`: 84145098752 available bytes; 95.30% used; 114148304 free inodes.

server3 `/var/tmp`: 84145098752 available bytes; 95.30% used; 114148304 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002931712 available bytes; 94.08% used; 114348208 free inodes.

server4 `/home`: 106002931712 available bytes; 94.08% used; 114348208 free inodes.

server4 `/data`: 109671202816 available bytes; 98.48% used; 224929427 free inodes.

server4 `/tmp`: 106002931712 available bytes; 94.08% used; 114348208 free inodes.

server4 `/var/tmp`: 106002931712 available bytes; 94.08% used; 114348208 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
