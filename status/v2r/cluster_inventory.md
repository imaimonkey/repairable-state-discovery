# V2R cluster inventory

2026-09-26T05:57:58.925488+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318781173760 available bytes; 82.22% used; 112476288 free inodes.

server1 `/home`: 318781173760 available bytes; 82.22% used; 112476288 free inodes.

server1 `/tmp`: 318781173760 available bytes; 82.22% used; 112476288 free inodes.

server1 `/var/tmp`: 318781173760 available bytes; 82.22% used; 112476288 free inodes.

server1 `/mnt/raid5`: 231113515008 available bytes; 98.94% used; 337539989 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22738300928 available bytes; 98.73% used; 110405659 free inodes.

server2 `/home`: 22738300928 available bytes; 98.73% used; 110405659 free inodes.

server2 `/tmp`: 22738300928 available bytes; 98.73% used; 110405659 free inodes.

server2 `/var/tmp`: 22738300928 available bytes; 98.73% used; 110405659 free inodes.

server2 `/mnt/raid5`: 274656546816 available bytes; 98.10% used; 445033780 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82440187904 available bytes; 95.40% used; 114110902 free inodes.

server3 `/home`: 82440187904 available bytes; 95.40% used; 114110902 free inodes.

server3 `/data`: 123999551488 available bytes; 98.29% used; 225822833 free inodes.

server3 `/tmp`: 82440187904 available bytes; 95.40% used; 114110902 free inodes.

server3 `/var/tmp`: 82440187904 available bytes; 95.40% used; 114110902 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094153728 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094153728 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106985476096 available bytes; 98.52% used; 224929124 free inodes.

server4 `/tmp`: 106094153728 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094153728 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
