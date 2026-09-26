# V2R cluster inventory

2026-09-26T17:48:53.173877+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315583479808 available bytes; 82.39% used; 112445766 free inodes.

server1 `/home`: 315583479808 available bytes; 82.39% used; 112445766 free inodes.

server1 `/tmp`: 315583479808 available bytes; 82.39% used; 112445766 free inodes.

server1 `/var/tmp`: 315583479808 available bytes; 82.39% used; 112445766 free inodes.

server1 `/mnt/raid5`: 645851910144 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18025762816 available bytes; 98.99% used; 110367620 free inodes.

server2 `/home`: 18025762816 available bytes; 98.99% used; 110367620 free inodes.

server2 `/tmp`: 18025762816 available bytes; 98.99% used; 110367620 free inodes.

server2 `/var/tmp`: 18025762816 available bytes; 98.99% used; 110367620 free inodes.

server2 `/mnt/raid5`: 605257453568 available bytes; 95.82% used; 444968788 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81273913344 available bytes; 95.46% used; 114065378 free inodes.

server3 `/home`: 81273913344 available bytes; 95.46% used; 114065378 free inodes.

server3 `/data`: 1349372186624 available bytes; 81.35% used; 225835521 free inodes.

server3 `/tmp`: 81273913344 available bytes; 95.46% used; 114065378 free inodes.

server3 `/var/tmp`: 81273913344 available bytes; 95.46% used; 114065378 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105939660800 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105939660800 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410389987328 available bytes; 94.33% used; 224824225 free inodes.

server4 `/tmp`: 105939660800 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105939660800 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
