# V2R cluster inventory

2026-09-26T08:10:21.090929+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318751567872 available bytes; 82.22% used; 112476264 free inodes.

server1 `/home`: 318751567872 available bytes; 82.22% used; 112476264 free inodes.

server1 `/tmp`: 318751567872 available bytes; 82.22% used; 112476264 free inodes.

server1 `/var/tmp`: 318751567872 available bytes; 82.22% used; 112476264 free inodes.

server1 `/mnt/raid5`: 219152666624 available bytes; 98.99% used; 337539052 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22314180608 available bytes; 98.76% used; 110403907 free inodes.

server2 `/home`: 22314180608 available bytes; 98.76% used; 110403907 free inodes.

server2 `/tmp`: 22314180608 available bytes; 98.76% used; 110403907 free inodes.

server2 `/var/tmp`: 22314180608 available bytes; 98.76% used; 110403907 free inodes.

server2 `/mnt/raid5`: 255757213696 available bytes; 98.23% used; 445025360 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82679730176 available bytes; 95.39% used; 114110818 free inodes.

server3 `/home`: 82679730176 available bytes; 95.39% used; 114110818 free inodes.

server3 `/data`: 123916775424 available bytes; 98.29% used; 225829359 free inodes.

server3 `/tmp`: 82679730176 available bytes; 95.39% used; 114110818 free inodes.

server3 `/var/tmp`: 82679730176 available bytes; 95.39% used; 114110818 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106064752640 available bytes; 94.08% used; 114348143 free inodes.

server4 `/home`: 106064752640 available bytes; 94.08% used; 114348143 free inodes.

server4 `/data`: 89390657536 available bytes; 98.76% used; 224883491 free inodes.

server4 `/tmp`: 106064752640 available bytes; 94.08% used; 114348143 free inodes.

server4 `/var/tmp`: 106064752640 available bytes; 94.08% used; 114348143 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
