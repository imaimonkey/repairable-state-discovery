# V2R cluster inventory

2026-09-24T21:39:14.702183+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323954999296 available bytes; 81.93% used; 112481419 free inodes.

server1 `/home`: 323954999296 available bytes; 81.93% used; 112481419 free inodes.

server1 `/tmp`: 323954999296 available bytes; 81.93% used; 112481419 free inodes.

server1 `/var/tmp`: 323954999296 available bytes; 81.93% used; 112481419 free inodes.

server1 `/mnt/raid5`: 415480639488 available bytes; 98.09% used; 337626398 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30137225216 available bytes; 98.32% used; 110411334 free inodes.

server2 `/home`: 30137225216 available bytes; 98.32% used; 110411334 free inodes.

server2 `/tmp`: 30137225216 available bytes; 98.32% used; 110411334 free inodes.

server2 `/var/tmp`: 30137225216 available bytes; 98.32% used; 110411334 free inodes.

server2 `/mnt/raid5`: 490129166336 available bytes; 96.61% used; 445154836 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84385099776 available bytes; 95.29% used; 114156093 free inodes.

server3 `/home`: 84385099776 available bytes; 95.29% used; 114156093 free inodes.

server3 `/data`: 150156873728 available bytes; 97.92% used; 225803029 free inodes.

server3 `/tmp`: 84385099776 available bytes; 95.29% used; 114156093 free inodes.

server3 `/var/tmp`: 84385099776 available bytes; 95.29% used; 114156093 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105629872128 available bytes; 94.11% used; 114348347 free inodes.

server4 `/home`: 105629872128 available bytes; 94.11% used; 114348347 free inodes.

server4 `/data`: 82192261120 available bytes; 98.86% used; 225252431 free inodes.

server4 `/tmp`: 105629872128 available bytes; 94.11% used; 114348347 free inodes.

server4 `/var/tmp`: 105629872128 available bytes; 94.11% used; 114348347 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
