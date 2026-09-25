# V2R cluster inventory

2026-09-25T03:21:09.601170+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318939750400 available bytes; 82.21% used; 112480365 free inodes.

server1 `/home`: 318939750400 available bytes; 82.21% used; 112480365 free inodes.

server1 `/tmp`: 318939750400 available bytes; 82.21% used; 112480365 free inodes.

server1 `/var/tmp`: 318939750400 available bytes; 82.21% used; 112480365 free inodes.

server1 `/mnt/raid5`: 416108625920 available bytes; 98.09% used; 337599976 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22988242944 available bytes; 98.72% used; 110410452 free inodes.

server2 `/home`: 22988242944 available bytes; 98.72% used; 110410452 free inodes.

server2 `/tmp`: 22988242944 available bytes; 98.72% used; 110410452 free inodes.

server2 `/var/tmp`: 22988242944 available bytes; 98.72% used; 110410452 free inodes.

server2 `/mnt/raid5`: 465174695936 available bytes; 96.79% used; 445112149 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342513664 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84342513664 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144676675584 available bytes; 98.00% used; 225810066 free inodes.

server3 `/tmp`: 84342513664 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84342513664 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105692557312 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692557312 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 45421813760 available bytes; 99.37% used; 224966876 free inodes.

server4 `/tmp`: 105692557312 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692557312 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
