# V2R cluster inventory

2026-09-26T02:39:27.881570+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318418296832 available bytes; 82.24% used; 112476272 free inodes.

server1 `/home`: 318418296832 available bytes; 82.24% used; 112476272 free inodes.

server1 `/tmp`: 318418296832 available bytes; 82.24% used; 112476272 free inodes.

server1 `/var/tmp`: 318418296832 available bytes; 82.24% used; 112476272 free inodes.

server1 `/mnt/raid5`: 331157422080 available bytes; 98.48% used; 337546085 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22941822976 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22941822976 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22941822976 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22941822976 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 288706322432 available bytes; 98.01% used; 445054186 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84318244864 available bytes; 95.29% used; 114152374 free inodes.

server3 `/home`: 84318244864 available bytes; 95.29% used; 114152374 free inodes.

server3 `/data`: 124786020352 available bytes; 98.28% used; 225816828 free inodes.

server3 `/tmp`: 84318244864 available bytes; 95.29% used; 114152374 free inodes.

server3 `/var/tmp`: 84318244864 available bytes; 95.29% used; 114152374 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106022916096 available bytes; 94.08% used; 114348272 free inodes.

server4 `/home`: 106022916096 available bytes; 94.08% used; 114348272 free inodes.

server4 `/data`: 109800415232 available bytes; 98.48% used; 224915430 free inodes.

server4 `/tmp`: 106022916096 available bytes; 94.08% used; 114348272 free inodes.

server4 `/var/tmp`: 106022916096 available bytes; 94.08% used; 114348272 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
