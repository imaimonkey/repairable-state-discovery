# V2R cluster inventory

2026-09-25T17:52:50.975197+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318668668928 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318668668928 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318668668928 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318668668928 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 371240046592 available bytes; 98.30% used; 337542676 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23096070144 available bytes; 98.71% used; 110407930 free inodes.

server2 `/home`: 23096070144 available bytes; 98.71% used; 110407930 free inodes.

server2 `/tmp`: 23096070144 available bytes; 98.71% used; 110407930 free inodes.

server2 `/var/tmp`: 23096070144 available bytes; 98.71% used; 110407930 free inodes.

server2 `/mnt/raid5`: 315382665216 available bytes; 97.82% used; 445068141 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84391452672 available bytes; 95.29% used; 114152615 free inodes.

server3 `/home`: 84391452672 available bytes; 95.29% used; 114152615 free inodes.

server3 `/data`: 132530565120 available bytes; 98.17% used; 225810698 free inodes.

server3 `/tmp`: 84391452672 available bytes; 95.29% used; 114152615 free inodes.

server3 `/var/tmp`: 84391452672 available bytes; 95.29% used; 114152615 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616941056 available bytes; 94.11% used; 114349621 free inodes.

server4 `/home`: 105616941056 available bytes; 94.11% used; 114349621 free inodes.

server4 `/data`: 229799882752 available bytes; 96.82% used; 224932546 free inodes.

server4 `/tmp`: 105616941056 available bytes; 94.11% used; 114349621 free inodes.

server4 `/var/tmp`: 105616941056 available bytes; 94.11% used; 114349621 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
