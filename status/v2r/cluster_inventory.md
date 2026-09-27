# V2R cluster inventory

2026-09-27T15:25:17.701648+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304745897984 available bytes; 83.00% used; 112401390 free inodes.

server1 `/home`: 304745897984 available bytes; 83.00% used; 112401390 free inodes.

server1 `/tmp`: 304745897984 available bytes; 83.00% used; 112401390 free inodes.

server1 `/var/tmp`: 304745897984 available bytes; 83.00% used; 112401390 free inodes.

server1 `/mnt/raid5`: 626090049536 available bytes; 97.13% used; 337423995 free inodes.
| server2 | True | ['5', '6', '7'] | [] |

server2 `/`: 13396451328 available bytes; 99.25% used; 110351754 free inodes.

server2 `/home`: 13396451328 available bytes; 99.25% used; 110351754 free inodes.

server2 `/tmp`: 13396451328 available bytes; 99.25% used; 110351754 free inodes.

server2 `/var/tmp`: 13396451328 available bytes; 99.25% used; 110351754 free inodes.

server2 `/mnt/raid5`: 524055420928 available bytes; 96.38% used; 444720915 free inodes.
| server3 | True | ['0', '1', '2'] | [] |

server3 `/`: 78560559104 available bytes; 95.62% used; 114062768 free inodes.

server3 `/home`: 78560559104 available bytes; 95.62% used; 114062768 free inodes.

server3 `/data`: 1326815703040 available bytes; 81.66% used; 225762685 free inodes.

server3 `/tmp`: 78560559104 available bytes; 95.62% used; 114062768 free inodes.

server3 `/var/tmp`: 78560559104 available bytes; 95.62% used; 114062768 free inodes.
| server4 | True | ['1', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 108536487936 available bytes; 93.94% used; 114372706 free inodes.

server4 `/home`: 108536487936 available bytes; 93.94% used; 114372706 free inodes.

server4 `/data`: 350348402688 available bytes; 95.16% used; 224727124 free inodes.

server4 `/tmp`: 108536487936 available bytes; 93.94% used; 114372706 free inodes.

server4 `/var/tmp`: 108536487936 available bytes; 93.94% used; 114372706 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
