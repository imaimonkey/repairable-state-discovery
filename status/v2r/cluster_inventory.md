# V2R cluster inventory

2026-09-26T05:44:13.480372+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318782808064 available bytes; 82.22% used; 112476277 free inodes.

server1 `/home`: 318782808064 available bytes; 82.22% used; 112476277 free inodes.

server1 `/tmp`: 318782808064 available bytes; 82.22% used; 112476277 free inodes.

server1 `/var/tmp`: 318782808064 available bytes; 82.22% used; 112476277 free inodes.

server1 `/mnt/raid5`: 240585101312 available bytes; 98.90% used; 337540068 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22926336000 available bytes; 98.72% used; 110406213 free inodes.

server2 `/home`: 22926336000 available bytes; 98.72% used; 110406213 free inodes.

server2 `/tmp`: 22926336000 available bytes; 98.72% used; 110406213 free inodes.

server2 `/var/tmp`: 22926336000 available bytes; 98.72% used; 110406213 free inodes.

server2 `/mnt/raid5`: 275060838400 available bytes; 98.10% used; 445036663 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83209666560 available bytes; 95.36% used; 114149763 free inodes.

server3 `/home`: 83209666560 available bytes; 95.36% used; 114149763 free inodes.

server3 `/data`: 124335403008 available bytes; 98.28% used; 225824011 free inodes.

server3 `/tmp`: 83209666560 available bytes; 95.36% used; 114149763 free inodes.

server3 `/var/tmp`: 83209666560 available bytes; 95.36% used; 114149763 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094555136 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094555136 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106989977600 available bytes; 98.52% used; 224929134 free inodes.

server4 `/tmp`: 106094555136 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094555136 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
