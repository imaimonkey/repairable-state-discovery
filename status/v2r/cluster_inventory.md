# V2R cluster inventory

2026-09-25T05:38:19.207527+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872625152 available bytes; 82.21% used; 112480333 free inodes.

server1 `/home`: 318872625152 available bytes; 82.21% used; 112480333 free inodes.

server1 `/tmp`: 318872625152 available bytes; 82.21% used; 112480333 free inodes.

server1 `/var/tmp`: 318872625152 available bytes; 82.21% used; 112480333 free inodes.

server1 `/mnt/raid5`: 408467128320 available bytes; 98.13% used; 337567273 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22918995968 available bytes; 98.72% used; 110410443 free inodes.

server2 `/home`: 22918995968 available bytes; 98.72% used; 110410443 free inodes.

server2 `/tmp`: 22918995968 available bytes; 98.72% used; 110410443 free inodes.

server2 `/var/tmp`: 22918995968 available bytes; 98.72% used; 110410443 free inodes.

server2 `/mnt/raid5`: 459469217792 available bytes; 96.83% used; 445102871 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84313575424 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84313575424 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142778441728 available bytes; 98.03% used; 225814680 free inodes.

server3 `/tmp`: 84313575424 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84313575424 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649762304 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105649762304 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 24781312000 available bytes; 99.66% used; 224966907 free inodes.

server4 `/tmp`: 105649762304 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105649762304 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
