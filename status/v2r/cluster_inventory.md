# V2R cluster inventory

2026-09-26T05:25:10.570858+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318400811008 available bytes; 82.24% used; 112476288 free inodes.

server1 `/home`: 318400811008 available bytes; 82.24% used; 112476288 free inodes.

server1 `/tmp`: 318400811008 available bytes; 82.24% used; 112476288 free inodes.

server1 `/var/tmp`: 318400811008 available bytes; 82.24% used; 112476288 free inodes.

server1 `/mnt/raid5`: 285544349696 available bytes; 98.69% used; 337542211 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22920777728 available bytes; 98.72% used; 110406201 free inodes.

server2 `/home`: 22920777728 available bytes; 98.72% used; 110406201 free inodes.

server2 `/tmp`: 22920777728 available bytes; 98.72% used; 110406201 free inodes.

server2 `/var/tmp`: 22920777728 available bytes; 98.72% used; 110406201 free inodes.

server2 `/mnt/raid5`: 276131561472 available bytes; 98.09% used; 445048808 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84088389632 available bytes; 95.31% used; 114166331 free inodes.

server3 `/home`: 84088389632 available bytes; 95.31% used; 114166331 free inodes.

server3 `/data`: 124360753152 available bytes; 98.28% used; 225824835 free inodes.

server3 `/tmp`: 84088389632 available bytes; 95.31% used; 114166331 free inodes.

server3 `/var/tmp`: 84088389632 available bytes; 95.31% used; 114166331 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106095063040 available bytes; 94.08% used; 114348207 free inodes.

server4 `/home`: 106095063040 available bytes; 94.08% used; 114348207 free inodes.

server4 `/data`: 106993319936 available bytes; 98.52% used; 224929234 free inodes.

server4 `/tmp`: 106095063040 available bytes; 94.08% used; 114348207 free inodes.

server4 `/var/tmp`: 106095063040 available bytes; 94.08% used; 114348207 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
