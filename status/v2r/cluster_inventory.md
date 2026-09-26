# V2R cluster inventory

2026-09-26T06:58:31.338547+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318769233920 available bytes; 82.22% used; 112476290 free inodes.

server1 `/home`: 318769233920 available bytes; 82.22% used; 112476290 free inodes.

server1 `/tmp`: 318769233920 available bytes; 82.22% used; 112476290 free inodes.

server1 `/var/tmp`: 318769233920 available bytes; 82.22% used; 112476290 free inodes.

server1 `/mnt/raid5`: 219300446208 available bytes; 98.99% used; 337539574 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22317195264 available bytes; 98.76% used; 110403882 free inodes.

server2 `/home`: 22317195264 available bytes; 98.76% used; 110403882 free inodes.

server2 `/tmp`: 22317195264 available bytes; 98.76% used; 110403882 free inodes.

server2 `/var/tmp`: 22317195264 available bytes; 98.76% used; 110403882 free inodes.

server2 `/mnt/raid5`: 272194912256 available bytes; 98.12% used; 445028001 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82687647744 available bytes; 95.39% used; 114110899 free inodes.

server3 `/home`: 82687647744 available bytes; 95.39% used; 114110899 free inodes.

server3 `/data`: 123987271680 available bytes; 98.29% used; 225821817 free inodes.

server3 `/tmp`: 82687647744 available bytes; 95.39% used; 114110899 free inodes.

server3 `/var/tmp`: 82687647744 available bytes; 95.39% used; 114110899 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106075418624 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106075418624 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105896263680 available bytes; 98.54% used; 224923052 free inodes.

server4 `/tmp`: 106075418624 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106075418624 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
