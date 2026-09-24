# V2R cluster inventory

2026-09-24T00:27:21.235674+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325551153152 available bytes; 81.84% used; 112500626 free inodes.

server1 `/home`: 325551153152 available bytes; 81.84% used; 112500626 free inodes.

server1 `/tmp`: 325551153152 available bytes; 81.84% used; 112500626 free inodes.

server1 `/var/tmp`: 325551153152 available bytes; 81.84% used; 112500626 free inodes.

server1 `/mnt/raid5`: 1155333406720 available bytes; 94.70% used; 337735183 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40997220352 available bytes; 97.71% used; 110432352 free inodes.

server2 `/home`: 40997220352 available bytes; 97.71% used; 110432352 free inodes.

server2 `/tmp`: 40997220352 available bytes; 97.71% used; 110432352 free inodes.

server2 `/var/tmp`: 40997220352 available bytes; 97.71% used; 110432352 free inodes.

server2 `/mnt/raid5`: 532879478784 available bytes; 96.32% used; 445203393 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292280328192 available bytes; 83.69% used; 114186805 free inodes.

server3 `/home`: 292280328192 available bytes; 83.69% used; 114186805 free inodes.

server3 `/data`: 82240937984 available bytes; 98.86% used; 225844282 free inodes.

server3 `/tmp`: 292280328192 available bytes; 83.69% used; 114186805 free inodes.

server3 `/var/tmp`: 292280328192 available bytes; 83.69% used; 114186805 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106084593664 available bytes; 94.08% used; 114350419 free inodes.

server4 `/home`: 106084593664 available bytes; 94.08% used; 114350419 free inodes.

server4 `/data`: 292922146816 available bytes; 95.95% used; 225414581 free inodes.

server4 `/tmp`: 106084593664 available bytes; 94.08% used; 114350419 free inodes.

server4 `/var/tmp`: 106084593664 available bytes; 94.08% used; 114350419 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
