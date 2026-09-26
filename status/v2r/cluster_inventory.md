# V2R cluster inventory

2026-09-26T19:29:31.154574+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315544895488 available bytes; 82.40% used; 112445158 free inodes.

server1 `/home`: 315544895488 available bytes; 82.40% used; 112445158 free inodes.

server1 `/tmp`: 315544895488 available bytes; 82.40% used; 112445158 free inodes.

server1 `/var/tmp`: 315544895488 available bytes; 82.40% used; 112445158 free inodes.

server1 `/mnt/raid5`: 645855657984 available bytes; 97.04% used; 337467122 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18024910848 available bytes; 98.99% used; 110367537 free inodes.

server2 `/home`: 18024910848 available bytes; 98.99% used; 110367537 free inodes.

server2 `/tmp`: 18024910848 available bytes; 98.99% used; 110367537 free inodes.

server2 `/var/tmp`: 18024910848 available bytes; 98.99% used; 110367537 free inodes.

server2 `/mnt/raid5`: 602423656448 available bytes; 95.84% used; 444966590 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81264513024 available bytes; 95.47% used; 114065305 free inodes.

server3 `/home`: 81264513024 available bytes; 95.47% used; 114065305 free inodes.

server3 `/data`: 1349026189312 available bytes; 81.36% used; 225833831 free inodes.

server3 `/tmp`: 81264513024 available bytes; 95.47% used; 114065305 free inodes.

server3 `/var/tmp`: 81264513024 available bytes; 95.47% used; 114065305 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105920503808 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105920503808 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410305298432 available bytes; 94.33% used; 224824169 free inodes.

server4 `/tmp`: 105920503808 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105920503808 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
