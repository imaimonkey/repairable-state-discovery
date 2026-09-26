# V2R cluster inventory

2026-09-26T05:25:52.118537+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318400532480 available bytes; 82.24% used; 112476289 free inodes.

server1 `/home`: 318400532480 available bytes; 82.24% used; 112476289 free inodes.

server1 `/tmp`: 318400532480 available bytes; 82.24% used; 112476289 free inodes.

server1 `/var/tmp`: 318400532480 available bytes; 82.24% used; 112476289 free inodes.

server1 `/mnt/raid5`: 283894390784 available bytes; 98.70% used; 337542141 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22920462336 available bytes; 98.72% used; 110406201 free inodes.

server2 `/home`: 22920462336 available bytes; 98.72% used; 110406201 free inodes.

server2 `/tmp`: 22920462336 available bytes; 98.72% used; 110406201 free inodes.

server2 `/var/tmp`: 22920462336 available bytes; 98.72% used; 110406201 free inodes.

server2 `/mnt/raid5`: 276648202240 available bytes; 98.09% used; 445048792 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84082724864 available bytes; 95.31% used; 114165920 free inodes.

server3 `/home`: 84082724864 available bytes; 95.31% used; 114165920 free inodes.

server3 `/data`: 124359897088 available bytes; 98.28% used; 225824816 free inodes.

server3 `/tmp`: 84082724864 available bytes; 95.31% used; 114165920 free inodes.

server3 `/var/tmp`: 84082724864 available bytes; 95.31% used; 114165920 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106095050752 available bytes; 94.08% used; 114348205 free inodes.

server4 `/home`: 106095050752 available bytes; 94.08% used; 114348205 free inodes.

server4 `/data`: 106992975872 available bytes; 98.52% used; 224929232 free inodes.

server4 `/tmp`: 106095050752 available bytes; 94.08% used; 114348205 free inodes.

server4 `/var/tmp`: 106095050752 available bytes; 94.08% used; 114348205 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
