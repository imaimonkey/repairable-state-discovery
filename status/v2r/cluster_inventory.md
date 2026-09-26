# V2R cluster inventory

2026-09-26T19:31:02.642675+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315546034176 available bytes; 82.40% used; 112445157 free inodes.

server1 `/home`: 315546034176 available bytes; 82.40% used; 112445157 free inodes.

server1 `/tmp`: 315546034176 available bytes; 82.40% used; 112445157 free inodes.

server1 `/var/tmp`: 315546034176 available bytes; 82.40% used; 112445157 free inodes.

server1 `/mnt/raid5`: 645855195136 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18024288256 available bytes; 98.99% used; 110367537 free inodes.

server2 `/home`: 18024288256 available bytes; 98.99% used; 110367537 free inodes.

server2 `/tmp`: 18024288256 available bytes; 98.99% used; 110367537 free inodes.

server2 `/var/tmp`: 18024288256 available bytes; 98.99% used; 110367537 free inodes.

server2 `/mnt/raid5`: 602362597376 available bytes; 95.84% used; 444966438 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81264209920 available bytes; 95.47% used; 114065305 free inodes.

server3 `/home`: 81264209920 available bytes; 95.47% used; 114065305 free inodes.

server3 `/data`: 1349023080448 available bytes; 81.36% used; 225833805 free inodes.

server3 `/tmp`: 81264209920 available bytes; 95.47% used; 114065305 free inodes.

server3 `/var/tmp`: 81264209920 available bytes; 95.47% used; 114065305 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105920450560 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105920450560 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410303348736 available bytes; 94.33% used; 224824173 free inodes.

server4 `/tmp`: 105920450560 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105920450560 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
