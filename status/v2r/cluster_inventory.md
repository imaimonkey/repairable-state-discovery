# V2R cluster inventory

2026-09-24T16:19:04.901435+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324024819712 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324024819712 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324024819712 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324024819712 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 395942891520 available bytes; 98.18% used; 337654658 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57334640640 available bytes; 96.80% used; 110426999 free inodes.

server2 `/home`: 57334640640 available bytes; 96.80% used; 110426999 free inodes.

server2 `/tmp`: 57334640640 available bytes; 96.80% used; 110426999 free inodes.

server2 `/var/tmp`: 57334640640 available bytes; 96.80% used; 110426999 free inodes.

server2 `/mnt/raid5`: 501298753536 available bytes; 96.54% used; 445164892 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 84716077056 available bytes; 95.27% used; 114180094 free inodes.

server3 `/home`: 84716077056 available bytes; 95.27% used; 114180094 free inodes.

server3 `/data`: 159617454080 available bytes; 97.79% used; 225789324 free inodes.

server3 `/tmp`: 84716077056 available bytes; 95.27% used; 114180094 free inodes.

server3 `/var/tmp`: 84716077056 available bytes; 95.27% used; 114180094 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105697460224 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105697460224 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89291501568 available bytes; 98.77% used; 225255970 free inodes.

server4 `/tmp`: 105697460224 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105697460224 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
