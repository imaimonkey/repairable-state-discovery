# V2R cluster inventory

2026-09-25T03:19:36.578537+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318938976256 available bytes; 82.21% used; 112480360 free inodes.

server1 `/home`: 318938976256 available bytes; 82.21% used; 112480360 free inodes.

server1 `/tmp`: 318938976256 available bytes; 82.21% used; 112480360 free inodes.

server1 `/var/tmp`: 318938976256 available bytes; 82.21% used; 112480360 free inodes.

server1 `/mnt/raid5`: 416112427008 available bytes; 98.09% used; 337600155 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22988734464 available bytes; 98.72% used; 110410452 free inodes.

server2 `/home`: 22988734464 available bytes; 98.72% used; 110410452 free inodes.

server2 `/tmp`: 22988734464 available bytes; 98.72% used; 110410452 free inodes.

server2 `/var/tmp`: 22988734464 available bytes; 98.72% used; 110410452 free inodes.

server2 `/mnt/raid5`: 464696291328 available bytes; 96.79% used; 445112205 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342620160 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84342620160 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144701890560 available bytes; 98.00% used; 225810107 free inodes.

server3 `/tmp`: 84342620160 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84342620160 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105692635136 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692635136 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 45424291840 available bytes; 99.37% used; 224966940 free inodes.

server4 `/tmp`: 105692635136 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692635136 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
