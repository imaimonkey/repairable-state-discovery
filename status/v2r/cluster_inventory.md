# V2R cluster inventory

2026-09-26T04:08:47.718244+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318413328384 available bytes; 82.24% used; 112476271 free inodes.

server1 `/home`: 318413328384 available bytes; 82.24% used; 112476271 free inodes.

server1 `/tmp`: 318413328384 available bytes; 82.24% used; 112476271 free inodes.

server1 `/var/tmp`: 318413328384 available bytes; 82.24% used; 112476271 free inodes.

server1 `/mnt/raid5`: 330565808128 available bytes; 98.48% used; 337545567 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22923993088 available bytes; 98.72% used; 110406200 free inodes.

server2 `/home`: 22923993088 available bytes; 98.72% used; 110406200 free inodes.

server2 `/tmp`: 22923993088 available bytes; 98.72% used; 110406200 free inodes.

server2 `/var/tmp`: 22923993088 available bytes; 98.72% used; 110406200 free inodes.

server2 `/mnt/raid5`: 285559705600 available bytes; 98.03% used; 445051116 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84141449216 available bytes; 95.30% used; 114148306 free inodes.

server3 `/home`: 84141449216 available bytes; 95.30% used; 114148306 free inodes.

server3 `/data`: 124591013888 available bytes; 98.28% used; 225819875 free inodes.

server3 `/tmp`: 84141449216 available bytes; 95.30% used; 114148306 free inodes.

server3 `/var/tmp`: 84141449216 available bytes; 95.30% used; 114148306 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106003079168 available bytes; 94.08% used; 114348208 free inodes.

server4 `/home`: 106003079168 available bytes; 94.08% used; 114348208 free inodes.

server4 `/data`: 109677588480 available bytes; 98.48% used; 224929429 free inodes.

server4 `/tmp`: 106003079168 available bytes; 94.08% used; 114348208 free inodes.

server4 `/var/tmp`: 106003079168 available bytes; 94.08% used; 114348208 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
