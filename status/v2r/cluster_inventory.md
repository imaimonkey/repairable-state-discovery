# V2R cluster inventory

2026-09-25T03:44:17.343640+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318938279936 available bytes; 82.21% used; 112480346 free inodes.

server1 `/home`: 318938279936 available bytes; 82.21% used; 112480346 free inodes.

server1 `/tmp`: 318938279936 available bytes; 82.21% used; 112480346 free inodes.

server1 `/var/tmp`: 318938279936 available bytes; 82.21% used; 112480346 free inodes.

server1 `/mnt/raid5`: 415752843264 available bytes; 98.09% used; 337597219 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22973648896 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22973648896 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22973648896 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22973648896 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 464458051584 available bytes; 96.79% used; 445111368 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341567488 available bytes; 95.29% used; 114156061 free inodes.

server3 `/home`: 84341567488 available bytes; 95.29% used; 114156061 free inodes.

server3 `/data`: 144353722368 available bytes; 98.00% used; 225817176 free inodes.

server3 `/tmp`: 84341567488 available bytes; 95.29% used; 114156061 free inodes.

server3 `/var/tmp`: 84341567488 available bytes; 95.29% used; 114156061 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683439616 available bytes; 94.10% used; 114350898 free inodes.

server4 `/home`: 105683439616 available bytes; 94.10% used; 114350898 free inodes.

server4 `/data`: 39151882240 available bytes; 99.46% used; 224965552 free inodes.

server4 `/tmp`: 105683439616 available bytes; 94.10% used; 114350898 free inodes.

server4 `/var/tmp`: 105683439616 available bytes; 94.10% used; 114350898 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
