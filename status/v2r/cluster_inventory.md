# V2R cluster inventory

2026-09-26T12:16:26.537693+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318192459776 available bytes; 82.25% used; 112474775 free inodes.

server1 `/home`: 318192459776 available bytes; 82.25% used; 112474775 free inodes.

server1 `/tmp`: 318192459776 available bytes; 82.25% used; 112474775 free inodes.

server1 `/var/tmp`: 318192459776 available bytes; 82.25% used; 112474775 free inodes.

server1 `/mnt/raid5`: 197943730176 available bytes; 99.09% used; 337537865 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19787071488 available bytes; 98.90% used; 110383632 free inodes.

server2 `/home`: 19787071488 available bytes; 98.90% used; 110383632 free inodes.

server2 `/tmp`: 19787071488 available bytes; 98.90% used; 110383632 free inodes.

server2 `/var/tmp`: 19787071488 available bytes; 98.90% used; 110383632 free inodes.

server2 `/mnt/raid5`: 240700710912 available bytes; 98.34% used; 444980718 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82650615808 available bytes; 95.39% used; 114110822 free inodes.

server3 `/home`: 82650615808 available bytes; 95.39% used; 114110822 free inodes.

server3 `/data`: 123423797248 available bytes; 98.29% used; 225824305 free inodes.

server3 `/tmp`: 82650615808 available bytes; 95.39% used; 114110822 free inodes.

server3 `/var/tmp`: 82650615808 available bytes; 95.39% used; 114110822 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105900072960 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105900072960 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88583028736 available bytes; 98.78% used; 224879227 free inodes.

server4 `/tmp`: 105900072960 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105900072960 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
