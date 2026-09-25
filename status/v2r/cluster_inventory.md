# V2R cluster inventory

2026-09-25T03:18:04.557264+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318939025408 available bytes; 82.21% used; 112480360 free inodes.

server1 `/home`: 318939025408 available bytes; 82.21% used; 112480360 free inodes.

server1 `/tmp`: 318939025408 available bytes; 82.21% used; 112480360 free inodes.

server1 `/var/tmp`: 318939025408 available bytes; 82.21% used; 112480360 free inodes.

server1 `/mnt/raid5`: 416114802688 available bytes; 98.09% used; 337600330 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22989697024 available bytes; 98.72% used; 110410452 free inodes.

server2 `/home`: 22989697024 available bytes; 98.72% used; 110410452 free inodes.

server2 `/tmp`: 22989697024 available bytes; 98.72% used; 110410452 free inodes.

server2 `/var/tmp`: 22989697024 available bytes; 98.72% used; 110410452 free inodes.

server2 `/mnt/raid5`: 465276600320 available bytes; 96.79% used; 445112270 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84343078912 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84343078912 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144728780800 available bytes; 98.00% used; 225810149 free inodes.

server3 `/tmp`: 84343078912 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84343078912 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105692676096 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692676096 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 47031009280 available bytes; 99.35% used; 224967015 free inodes.

server4 `/tmp`: 105692676096 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692676096 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
