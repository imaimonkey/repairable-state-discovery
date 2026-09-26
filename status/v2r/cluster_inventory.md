# V2R cluster inventory

2026-09-26T19:23:25.142758+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315545907200 available bytes; 82.40% used; 112445163 free inodes.

server1 `/home`: 315545907200 available bytes; 82.40% used; 112445163 free inodes.

server1 `/tmp`: 315545907200 available bytes; 82.40% used; 112445163 free inodes.

server1 `/var/tmp`: 315545907200 available bytes; 82.40% used; 112445163 free inodes.

server1 `/mnt/raid5`: 645854523392 available bytes; 97.04% used; 337467122 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18029752320 available bytes; 98.99% used; 110367537 free inodes.

server2 `/home`: 18029752320 available bytes; 98.99% used; 110367537 free inodes.

server2 `/tmp`: 18029752320 available bytes; 98.99% used; 110367537 free inodes.

server2 `/var/tmp`: 18029752320 available bytes; 98.99% used; 110367537 free inodes.

server2 `/mnt/raid5`: 602561552384 available bytes; 95.84% used; 444965974 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81263190016 available bytes; 95.47% used; 114065307 free inodes.

server3 `/home`: 81263190016 available bytes; 95.47% used; 114065307 free inodes.

server3 `/data`: 1349032583168 available bytes; 81.36% used; 225833929 free inodes.

server3 `/tmp`: 81263190016 available bytes; 95.47% used; 114065307 free inodes.

server3 `/var/tmp`: 81263190016 available bytes; 95.47% used; 114065307 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105920618496 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105920618496 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410309390336 available bytes; 94.33% used; 224824169 free inodes.

server4 `/tmp`: 105920618496 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105920618496 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
