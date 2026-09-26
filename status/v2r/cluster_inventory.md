# V2R cluster inventory

2026-09-26T15:20:58.774329+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318158974976 available bytes; 82.25% used; 112473933 free inodes.

server1 `/home`: 318158974976 available bytes; 82.25% used; 112473933 free inodes.

server1 `/tmp`: 318158974976 available bytes; 82.25% used; 112473933 free inodes.

server1 `/var/tmp`: 318158974976 available bytes; 82.25% used; 112473933 free inodes.

server1 `/mnt/raid5`: 654127742976 available bytes; 97.00% used; 337531540 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 11535847424 available bytes; 99.36% used; 110367450 free inodes.

server2 `/home`: 11535847424 available bytes; 99.36% used; 110367450 free inodes.

server2 `/tmp`: 11535847424 available bytes; 99.36% used; 110367450 free inodes.

server2 `/var/tmp`: 11535847424 available bytes; 99.36% used; 110367450 free inodes.

server2 `/mnt/raid5`: 609676861440 available bytes; 95.79% used; 444973190 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82442625024 available bytes; 95.40% used; 114101911 free inodes.

server3 `/home`: 82442625024 available bytes; 95.40% used; 114101911 free inodes.

server3 `/data`: 1347192066048 available bytes; 81.38% used; 225809954 free inodes.

server3 `/tmp`: 82442625024 available bytes; 95.40% used; 114101911 free inodes.

server3 `/var/tmp`: 82442625024 available bytes; 95.40% used; 114101911 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954897920 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105954897920 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410803437568 available bytes; 94.32% used; 224826034 free inodes.

server4 `/tmp`: 105954897920 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105954897920 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
