# V2R cluster inventory

2026-09-25T03:43:43.082048+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318938529792 available bytes; 82.21% used; 112480346 free inodes.

server1 `/home`: 318938529792 available bytes; 82.21% used; 112480346 free inodes.

server1 `/tmp`: 318938529792 available bytes; 82.21% used; 112480346 free inodes.

server1 `/var/tmp`: 318938529792 available bytes; 82.21% used; 112480346 free inodes.

server1 `/mnt/raid5`: 415752830976 available bytes; 98.09% used; 337597281 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22973800448 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22973800448 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22973800448 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22973800448 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 463935827968 available bytes; 96.79% used; 445111462 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340588544 available bytes; 95.29% used; 114156059 free inodes.

server3 `/home`: 84340588544 available bytes; 95.29% used; 114156059 free inodes.

server3 `/data`: 144360718336 available bytes; 98.00% used; 225817205 free inodes.

server3 `/tmp`: 84340588544 available bytes; 95.29% used; 114156059 free inodes.

server3 `/var/tmp`: 84340588544 available bytes; 95.29% used; 114156059 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105683443712 available bytes; 94.10% used; 114350898 free inodes.

server4 `/home`: 105683443712 available bytes; 94.10% used; 114350898 free inodes.

server4 `/data`: 39149592576 available bytes; 99.46% used; 224965580 free inodes.

server4 `/tmp`: 105683443712 available bytes; 94.10% used; 114350898 free inodes.

server4 `/var/tmp`: 105683443712 available bytes; 94.10% used; 114350898 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
