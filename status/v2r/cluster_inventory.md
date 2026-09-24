# V2R cluster inventory

2026-09-24T00:00:00.028801+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325582794752 available bytes; 81.84% used; 112500913 free inodes.

server1 `/home`: 325582794752 available bytes; 81.84% used; 112500913 free inodes.

server1 `/tmp`: 325582794752 available bytes; 81.84% used; 112500913 free inodes.

server1 `/var/tmp`: 325582794752 available bytes; 81.84% used; 112500913 free inodes.

server1 `/mnt/raid5`: 1267568128000 available bytes; 94.19% used; 337735474 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41019121664 available bytes; 97.71% used; 110432448 free inodes.

server2 `/home`: 41019121664 available bytes; 97.71% used; 110432448 free inodes.

server2 `/tmp`: 41019121664 available bytes; 97.71% used; 110432448 free inodes.

server2 `/var/tmp`: 41019121664 available bytes; 97.71% used; 110432448 free inodes.

server2 `/mnt/raid5`: 533545467904 available bytes; 96.31% used; 445204383 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292802109440 available bytes; 83.66% used; 114213631 free inodes.

server3 `/home`: 292802109440 available bytes; 83.66% used; 114213631 free inodes.

server3 `/data`: 82269696000 available bytes; 98.86% used; 225844852 free inodes.

server3 `/tmp`: 292802109440 available bytes; 83.66% used; 114213631 free inodes.

server3 `/var/tmp`: 292802109440 available bytes; 83.66% used; 114213631 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106139447296 available bytes; 94.08% used; 114351275 free inodes.

server4 `/home`: 106139447296 available bytes; 94.08% used; 114351275 free inodes.

server4 `/data`: 292940189696 available bytes; 95.95% used; 225415180 free inodes.

server4 `/tmp`: 106139447296 available bytes; 94.08% used; 114351275 free inodes.

server4 `/var/tmp`: 106139447296 available bytes; 94.08% used; 114351275 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
