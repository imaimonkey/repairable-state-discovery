# V2R cluster inventory

2026-09-24T06:23:48.334409+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324509798400 available bytes; 81.90% used; 112491718 free inodes.

server1 `/home`: 324509798400 available bytes; 81.90% used; 112491718 free inodes.

server1 `/tmp`: 324509798400 available bytes; 81.90% used; 112491718 free inodes.

server1 `/var/tmp`: 324509798400 available bytes; 81.90% used; 112491718 free inodes.

server1 `/mnt/raid5`: 517574139904 available bytes; 97.63% used; 337723765 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57883533312 available bytes; 96.77% used; 110431221 free inodes.

server2 `/home`: 57883533312 available bytes; 96.77% used; 110431221 free inodes.

server2 `/tmp`: 57883533312 available bytes; 96.77% used; 110431221 free inodes.

server2 `/var/tmp`: 57883533312 available bytes; 96.77% used; 110431221 free inodes.

server2 `/mnt/raid5`: 520453165056 available bytes; 96.40% used; 445192236 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127170457600 available bytes; 92.90% used; 114196704 free inodes.

server3 `/home`: 127170457600 available bytes; 92.90% used; 114196704 free inodes.

server3 `/data`: 140561104896 available bytes; 98.06% used; 225835882 free inodes.

server3 `/tmp`: 127170457600 available bytes; 92.90% used; 114196704 free inodes.

server3 `/var/tmp`: 127170457600 available bytes; 92.90% used; 114196704 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105805836288 available bytes; 94.10% used; 114349291 free inodes.

server4 `/home`: 105805836288 available bytes; 94.10% used; 114349291 free inodes.

server4 `/data`: 332923465728 available bytes; 95.40% used; 225373445 free inodes.

server4 `/tmp`: 105805836288 available bytes; 94.10% used; 114349291 free inodes.

server4 `/var/tmp`: 105805836288 available bytes; 94.10% used; 114349291 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
