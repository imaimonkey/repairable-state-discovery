# V2R cluster inventory

2026-09-26T04:43:07.105246+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318397927424 available bytes; 82.24% used; 112476276 free inodes.

server1 `/home`: 318397927424 available bytes; 82.24% used; 112476276 free inodes.

server1 `/tmp`: 318397927424 available bytes; 82.24% used; 112476276 free inodes.

server1 `/var/tmp`: 318397927424 available bytes; 82.24% used; 112476276 free inodes.

server1 `/mnt/raid5`: 330487779328 available bytes; 98.48% used; 337545393 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22937337856 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22937337856 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22937337856 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22937337856 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 285118836736 available bytes; 98.03% used; 445050199 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84502089728 available bytes; 95.28% used; 114169199 free inodes.

server3 `/home`: 84502089728 available bytes; 95.28% used; 114169199 free inodes.

server3 `/data`: 124393586688 available bytes; 98.28% used; 225817538 free inodes.

server3 `/tmp`: 84502089728 available bytes; 95.28% used; 114169199 free inodes.

server3 `/var/tmp`: 84502089728 available bytes; 95.28% used; 114169199 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002051072 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106002051072 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 107065491456 available bytes; 98.52% used; 224929357 free inodes.

server4 `/tmp`: 106002051072 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106002051072 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
