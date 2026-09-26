# V2R cluster inventory

2026-09-26T19:09:41.998004+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315553841152 available bytes; 82.40% used; 112445280 free inodes.

server1 `/home`: 315553841152 available bytes; 82.40% used; 112445280 free inodes.

server1 `/tmp`: 315553841152 available bytes; 82.40% used; 112445280 free inodes.

server1 `/var/tmp`: 315553841152 available bytes; 82.40% used; 112445280 free inodes.

server1 `/mnt/raid5`: 645854728192 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18022817792 available bytes; 98.99% used; 110367602 free inodes.

server2 `/home`: 18022817792 available bytes; 98.99% used; 110367602 free inodes.

server2 `/tmp`: 18022817792 available bytes; 98.99% used; 110367602 free inodes.

server2 `/var/tmp`: 18022817792 available bytes; 98.99% used; 110367602 free inodes.

server2 `/mnt/raid5`: 602960543744 available bytes; 95.83% used; 444966747 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81272766464 available bytes; 95.46% used; 114065371 free inodes.

server3 `/home`: 81272766464 available bytes; 95.46% used; 114065371 free inodes.

server3 `/data`: 1349042843648 available bytes; 81.36% used; 225834144 free inodes.

server3 `/tmp`: 81272766464 available bytes; 95.46% used; 114065371 free inodes.

server3 `/var/tmp`: 81272766464 available bytes; 95.46% used; 114065371 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105920950272 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105920950272 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410322386944 available bytes; 94.33% used; 224824171 free inodes.

server4 `/tmp`: 105920950272 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105920950272 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
