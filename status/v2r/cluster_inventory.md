# V2R cluster inventory

2026-09-25T21:05:12.489127+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318698127360 available bytes; 82.22% used; 112476316 free inodes.

server1 `/home`: 318698127360 available bytes; 82.22% used; 112476316 free inodes.

server1 `/tmp`: 318698127360 available bytes; 82.22% used; 112476316 free inodes.

server1 `/var/tmp`: 318698127360 available bytes; 82.22% used; 112476316 free inodes.

server1 `/mnt/raid5`: 368610205696 available bytes; 98.31% used; 337539505 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22888452096 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22888452096 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22888452096 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22888452096 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 302272593920 available bytes; 97.91% used; 445056031 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84367036416 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84367036416 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 126046863360 available bytes; 98.26% used; 225807437 free inodes.

server3 `/tmp`: 84367036416 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84367036416 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105468313600 available bytes; 94.11% used; 114347419 free inodes.

server4 `/home`: 105468313600 available bytes; 94.11% used; 114347419 free inodes.

server4 `/data`: 218518593536 available bytes; 96.98% used; 224921701 free inodes.

server4 `/tmp`: 105468313600 available bytes; 94.11% used; 114347419 free inodes.

server4 `/var/tmp`: 105468313600 available bytes; 94.11% used; 114347419 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
