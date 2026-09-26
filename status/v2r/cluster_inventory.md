# V2R cluster inventory

2026-09-26T05:18:13.909025+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318397710336 available bytes; 82.24% used; 112476277 free inodes.

server1 `/home`: 318397710336 available bytes; 82.24% used; 112476277 free inodes.

server1 `/tmp`: 318397710336 available bytes; 82.24% used; 112476277 free inodes.

server1 `/var/tmp`: 318397710336 available bytes; 82.24% used; 112476277 free inodes.

server1 `/mnt/raid5`: 302710030336 available bytes; 98.61% used; 337542768 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22922211328 available bytes; 98.72% used; 110406203 free inodes.

server2 `/home`: 22922211328 available bytes; 98.72% used; 110406203 free inodes.

server2 `/tmp`: 22922211328 available bytes; 98.72% used; 110406203 free inodes.

server2 `/var/tmp`: 22922211328 available bytes; 98.72% used; 110406203 free inodes.

server2 `/mnt/raid5`: 263379451904 available bytes; 98.18% used; 445049067 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84086140928 available bytes; 95.31% used; 114166169 free inodes.

server3 `/home`: 84086140928 available bytes; 95.31% used; 114166169 free inodes.

server3 `/data`: 124362145792 available bytes; 98.28% used; 225824944 free inodes.

server3 `/tmp`: 84086140928 available bytes; 95.31% used; 114166169 free inodes.

server3 `/var/tmp`: 84086140928 available bytes; 95.31% used; 114166169 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106095280128 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106095280128 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 106993598464 available bytes; 98.52% used; 224929211 free inodes.

server4 `/tmp`: 106095280128 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106095280128 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
