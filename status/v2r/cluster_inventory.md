# V2R cluster inventory

2026-09-24T22:23:49.314183+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323946020864 available bytes; 81.93% used; 112481420 free inodes.

server1 `/home`: 323946020864 available bytes; 81.93% used; 112481420 free inodes.

server1 `/tmp`: 323946020864 available bytes; 81.93% used; 112481420 free inodes.

server1 `/var/tmp`: 323946020864 available bytes; 81.93% used; 112481420 free inodes.

server1 `/mnt/raid5`: 415386308608 available bytes; 98.09% used; 337621065 free inodes.
| server2 | True | [] | [] |

server2 `/`: 25292468224 available bytes; 98.59% used; 110411077 free inodes.

server2 `/home`: 25292468224 available bytes; 98.59% used; 110411077 free inodes.

server2 `/tmp`: 25292468224 available bytes; 98.59% used; 110411077 free inodes.

server2 `/var/tmp`: 25292468224 available bytes; 98.59% used; 110411077 free inodes.

server2 `/mnt/raid5`: 488199303168 available bytes; 96.63% used; 445153337 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84378439680 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84378439680 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 128732430336 available bytes; 98.22% used; 225802182 free inodes.

server3 `/tmp`: 84378439680 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84378439680 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810530304 available bytes; 94.10% used; 114348324 free inodes.

server4 `/home`: 105810530304 available bytes; 94.10% used; 114348324 free inodes.

server4 `/data`: 73340280832 available bytes; 98.99% used; 225229106 free inodes.

server4 `/tmp`: 105810530304 available bytes; 94.10% used; 114348324 free inodes.

server4 `/var/tmp`: 105810530304 available bytes; 94.10% used; 114348324 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
