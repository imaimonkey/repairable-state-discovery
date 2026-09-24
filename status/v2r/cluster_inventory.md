# V2R cluster inventory

2026-09-24T18:09:07.498449+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324006965248 available bytes; 81.92% used; 112481435 free inodes.

server1 `/home`: 324006965248 available bytes; 81.92% used; 112481435 free inodes.

server1 `/tmp`: 324006965248 available bytes; 81.92% used; 112481435 free inodes.

server1 `/var/tmp`: 324006965248 available bytes; 81.92% used; 112481435 free inodes.

server1 `/mnt/raid5`: 416368898048 available bytes; 98.09% used; 337641837 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 54506422272 available bytes; 96.96% used; 110412106 free inodes.

server2 `/home`: 54506422272 available bytes; 96.96% used; 110412106 free inodes.

server2 `/tmp`: 54506422272 available bytes; 96.96% used; 110412106 free inodes.

server2 `/var/tmp`: 54506422272 available bytes; 96.96% used; 110412106 free inodes.

server2 `/mnt/raid5`: 497373851648 available bytes; 96.56% used; 445161261 free inodes.
| server3 | True | ['1'] | [] |

server3 `/`: 84407095296 available bytes; 95.29% used; 114156134 free inodes.

server3 `/home`: 84407095296 available bytes; 95.29% used; 114156134 free inodes.

server3 `/data`: 151713120256 available bytes; 97.90% used; 225786108 free inodes.

server3 `/tmp`: 84407095296 available bytes; 95.29% used; 114156134 free inodes.

server3 `/var/tmp`: 84407095296 available bytes; 95.29% used; 114156134 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105663225856 available bytes; 94.10% used; 114348531 free inodes.

server4 `/home`: 105663225856 available bytes; 94.10% used; 114348531 free inodes.

server4 `/data`: 88677367808 available bytes; 98.77% used; 225253324 free inodes.

server4 `/tmp`: 105663225856 available bytes; 94.10% used; 114348531 free inodes.

server4 `/var/tmp`: 105663225856 available bytes; 94.10% used; 114348531 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
