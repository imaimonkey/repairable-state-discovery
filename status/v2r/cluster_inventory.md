# V2R cluster inventory

2026-09-26T05:30:27.164541+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318792683520 available bytes; 82.22% used; 112476275 free inodes.

server1 `/home`: 318792683520 available bytes; 82.22% used; 112476275 free inodes.

server1 `/tmp`: 318792683520 available bytes; 82.22% used; 112476275 free inodes.

server1 `/var/tmp`: 318792683520 available bytes; 82.22% used; 112476275 free inodes.

server1 `/mnt/raid5`: 267533770752 available bytes; 98.77% used; 337541699 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22920818688 available bytes; 98.72% used; 110406215 free inodes.

server2 `/home`: 22920818688 available bytes; 98.72% used; 110406215 free inodes.

server2 `/tmp`: 22920818688 available bytes; 98.72% used; 110406215 free inodes.

server2 `/var/tmp`: 22920818688 available bytes; 98.72% used; 110406215 free inodes.

server2 `/mnt/raid5`: 276485726208 available bytes; 98.09% used; 445048399 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84070924288 available bytes; 95.31% used; 114166389 free inodes.

server3 `/home`: 84070924288 available bytes; 95.31% used; 114166389 free inodes.

server3 `/data`: 124353818624 available bytes; 98.28% used; 225824679 free inodes.

server3 `/tmp`: 84070924288 available bytes; 95.31% used; 114166389 free inodes.

server3 `/var/tmp`: 84070924288 available bytes; 95.31% used; 114166389 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094915584 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094915584 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106992087040 available bytes; 98.52% used; 224929230 free inodes.

server4 `/tmp`: 106094915584 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094915584 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
