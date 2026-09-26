# V2R cluster inventory

2026-09-26T05:28:55.550679+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318793863168 available bytes; 82.22% used; 112476281 free inodes.

server1 `/home`: 318793863168 available bytes; 82.22% used; 112476281 free inodes.

server1 `/tmp`: 318793863168 available bytes; 82.22% used; 112476281 free inodes.

server1 `/var/tmp`: 318793863168 available bytes; 82.22% used; 112476281 free inodes.

server1 `/mnt/raid5`: 272207679488 available bytes; 98.75% used; 337541857 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22920957952 available bytes; 98.72% used; 110406215 free inodes.

server2 `/home`: 22920957952 available bytes; 98.72% used; 110406215 free inodes.

server2 `/tmp`: 22920957952 available bytes; 98.72% used; 110406215 free inodes.

server2 `/var/tmp`: 22920957952 available bytes; 98.72% used; 110406215 free inodes.

server2 `/mnt/raid5`: 276545396736 available bytes; 98.09% used; 445048463 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84071018496 available bytes; 95.31% used; 114166387 free inodes.

server3 `/home`: 84071018496 available bytes; 95.31% used; 114166387 free inodes.

server3 `/data`: 124355506176 available bytes; 98.28% used; 225824766 free inodes.

server3 `/tmp`: 84071018496 available bytes; 95.31% used; 114166387 free inodes.

server3 `/var/tmp`: 84071018496 available bytes; 95.31% used; 114166387 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094952448 available bytes; 94.08% used; 114348207 free inodes.

server4 `/home`: 106094952448 available bytes; 94.08% used; 114348207 free inodes.

server4 `/data`: 106992558080 available bytes; 98.52% used; 224929232 free inodes.

server4 `/tmp`: 106094952448 available bytes; 94.08% used; 114348207 free inodes.

server4 `/var/tmp`: 106094952448 available bytes; 94.08% used; 114348207 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
