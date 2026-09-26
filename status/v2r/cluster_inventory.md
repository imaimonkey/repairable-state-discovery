# V2R cluster inventory

2026-09-26T18:57:30.161662+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315557212160 available bytes; 82.40% used; 112445748 free inodes.

server1 `/home`: 315557212160 available bytes; 82.40% used; 112445748 free inodes.

server1 `/tmp`: 315557212160 available bytes; 82.40% used; 112445748 free inodes.

server1 `/var/tmp`: 315557212160 available bytes; 82.40% used; 112445748 free inodes.

server1 `/mnt/raid5`: 645853921280 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18025541632 available bytes; 98.99% used; 110367610 free inodes.

server2 `/home`: 18025541632 available bytes; 98.99% used; 110367610 free inodes.

server2 `/tmp`: 18025541632 available bytes; 98.99% used; 110367610 free inodes.

server2 `/var/tmp`: 18025541632 available bytes; 98.99% used; 110367610 free inodes.

server2 `/mnt/raid5`: 602777706496 available bytes; 95.83% used; 444967077 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81274585088 available bytes; 95.46% used; 114065385 free inodes.

server3 `/home`: 81274585088 available bytes; 95.46% used; 114065385 free inodes.

server3 `/data`: 1349140447232 available bytes; 81.35% used; 225834347 free inodes.

server3 `/tmp`: 81274585088 available bytes; 95.46% used; 114065385 free inodes.

server3 `/var/tmp`: 81274585088 available bytes; 95.46% used; 114065385 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105929629696 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105929629696 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410336215040 available bytes; 94.33% used; 224824181 free inodes.

server4 `/tmp`: 105929629696 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105929629696 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
