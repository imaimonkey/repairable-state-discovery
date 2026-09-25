# V2R cluster inventory

2026-09-25T23:19:59.850174+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318682234880 available bytes; 82.22% used; 112476296 free inodes.

server1 `/home`: 318682234880 available bytes; 82.22% used; 112476296 free inodes.

server1 `/tmp`: 318682234880 available bytes; 82.22% used; 112476296 free inodes.

server1 `/var/tmp`: 318682234880 available bytes; 82.22% used; 112476296 free inodes.

server1 `/mnt/raid5`: 360132444160 available bytes; 98.35% used; 337538703 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22946934784 available bytes; 98.72% used; 110406230 free inodes.

server2 `/home`: 22946934784 available bytes; 98.72% used; 110406230 free inodes.

server2 `/tmp`: 22946934784 available bytes; 98.72% used; 110406230 free inodes.

server2 `/var/tmp`: 22946934784 available bytes; 98.72% used; 110406230 free inodes.

server2 `/mnt/raid5`: 297599934464 available bytes; 97.94% used; 445051415 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84348231680 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84348231680 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124751421440 available bytes; 98.28% used; 225805105 free inodes.

server3 `/tmp`: 84348231680 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84348231680 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105158987776 available bytes; 94.13% used; 114346790 free inodes.

server4 `/home`: 105158987776 available bytes; 94.13% used; 114346790 free inodes.

server4 `/data`: 185129795584 available bytes; 97.44% used; 224917631 free inodes.

server4 `/tmp`: 105158987776 available bytes; 94.13% used; 114346790 free inodes.

server4 `/var/tmp`: 105158987776 available bytes; 94.13% used; 114346790 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
