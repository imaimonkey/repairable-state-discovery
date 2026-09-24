# V2R cluster inventory

2026-09-24T07:31:07.048526+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324452925440 available bytes; 81.90% used; 112491135 free inodes.

server1 `/home`: 324452925440 available bytes; 81.90% used; 112491135 free inodes.

server1 `/tmp`: 324452925440 available bytes; 81.90% used; 112491135 free inodes.

server1 `/var/tmp`: 324452925440 available bytes; 81.90% used; 112491135 free inodes.

server1 `/mnt/raid5`: 517410729984 available bytes; 97.63% used; 337722794 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57842876416 available bytes; 96.77% used; 110431162 free inodes.

server2 `/home`: 57842876416 available bytes; 96.77% used; 110431162 free inodes.

server2 `/tmp`: 57842876416 available bytes; 96.77% used; 110431162 free inodes.

server2 `/var/tmp`: 57842876416 available bytes; 96.77% used; 110431162 free inodes.

server2 `/mnt/raid5`: 518228049920 available bytes; 96.42% used; 445180768 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126364217344 available bytes; 92.95% used; 114149779 free inodes.

server3 `/home`: 126364217344 available bytes; 92.95% used; 114149779 free inodes.

server3 `/data`: 138786754560 available bytes; 98.08% used; 225834087 free inodes.

server3 `/tmp`: 126364217344 available bytes; 92.95% used; 114149779 free inodes.

server3 `/var/tmp`: 126364217344 available bytes; 92.95% used; 114149779 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780690944 available bytes; 94.10% used; 114349185 free inodes.

server4 `/home`: 105780690944 available bytes; 94.10% used; 114349185 free inodes.

server4 `/data`: 285813768192 available bytes; 96.05% used; 225366893 free inodes.

server4 `/tmp`: 105780690944 available bytes; 94.10% used; 114349185 free inodes.

server4 `/var/tmp`: 105780690944 available bytes; 94.10% used; 114349185 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
