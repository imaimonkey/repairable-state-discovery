# V2R cluster inventory

2026-09-27T07:59:37.481614+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314469482496 available bytes; 82.46% used; 112440799 free inodes.

server1 `/home`: 314469482496 available bytes; 82.46% used; 112440799 free inodes.

server1 `/tmp`: 314469482496 available bytes; 82.46% used; 112440799 free inodes.

server1 `/var/tmp`: 314469482496 available bytes; 82.46% used; 112440799 free inodes.

server1 `/mnt/raid5`: 634654572544 available bytes; 97.09% used; 337400006 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 17609166848 available bytes; 99.02% used; 110365012 free inodes.

server2 `/home`: 17609166848 available bytes; 99.02% used; 110365012 free inodes.

server2 `/tmp`: 17609166848 available bytes; 99.02% used; 110365012 free inodes.

server2 `/var/tmp`: 17609166848 available bytes; 99.02% used; 110365012 free inodes.

server2 `/mnt/raid5`: 569985105920 available bytes; 96.06% used; 444873349 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78573481984 available bytes; 95.62% used; 114062876 free inodes.

server3 `/home`: 78573481984 available bytes; 95.62% used; 114062876 free inodes.

server3 `/data`: 1332892946432 available bytes; 81.58% used; 225763776 free inodes.

server3 `/tmp`: 78573481984 available bytes; 95.62% used; 114062876 free inodes.

server3 `/var/tmp`: 78573481984 available bytes; 95.62% used; 114062876 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111069753344 available bytes; 93.80% used; 114372878 free inodes.

server4 `/home`: 111069753344 available bytes; 93.80% used; 114372878 free inodes.

server4 `/data`: 374266732544 available bytes; 94.83% used; 224770945 free inodes.

server4 `/tmp`: 111069753344 available bytes; 93.80% used; 114372878 free inodes.

server4 `/var/tmp`: 111069753344 available bytes; 93.80% used; 114372878 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
