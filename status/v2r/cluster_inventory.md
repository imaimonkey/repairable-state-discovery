# V2R cluster inventory

2026-09-24T07:15:09.361473+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324453175296 available bytes; 81.90% used; 112491281 free inodes.

server1 `/home`: 324453175296 available bytes; 81.90% used; 112491281 free inodes.

server1 `/tmp`: 324453175296 available bytes; 81.90% used; 112491281 free inodes.

server1 `/var/tmp`: 324453175296 available bytes; 81.90% used; 112491281 free inodes.

server1 `/mnt/raid5`: 517423710208 available bytes; 97.63% used; 337722818 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57852801024 available bytes; 96.77% used; 110431137 free inodes.

server2 `/home`: 57852801024 available bytes; 96.77% used; 110431137 free inodes.

server2 `/tmp`: 57852801024 available bytes; 96.77% used; 110431137 free inodes.

server2 `/var/tmp`: 57852801024 available bytes; 96.77% used; 110431137 free inodes.

server2 `/mnt/raid5`: 518735650816 available bytes; 96.42% used; 445181399 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127136743424 available bytes; 92.91% used; 114198840 free inodes.

server3 `/home`: 127136743424 available bytes; 92.91% used; 114198840 free inodes.

server3 `/data`: 139083436032 available bytes; 98.08% used; 225834449 free inodes.

server3 `/tmp`: 127136743424 available bytes; 92.91% used; 114198840 free inodes.

server3 `/var/tmp`: 127136743424 available bytes; 92.91% used; 114198840 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105789898752 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105789898752 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 293389385728 available bytes; 95.95% used; 225367240 free inodes.

server4 `/tmp`: 105789898752 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105789898752 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
