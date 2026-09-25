# V2R cluster inventory

2026-09-25T20:33:24.454250+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318704660480 available bytes; 82.22% used; 112476321 free inodes.

server1 `/home`: 318704660480 available bytes; 82.22% used; 112476321 free inodes.

server1 `/tmp`: 318704660480 available bytes; 82.22% used; 112476321 free inodes.

server1 `/var/tmp`: 318704660480 available bytes; 82.22% used; 112476321 free inodes.

server1 `/mnt/raid5`: 369391132672 available bytes; 98.31% used; 337540476 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 23044079616 available bytes; 98.71% used; 110407154 free inodes.

server2 `/home`: 23044079616 available bytes; 98.71% used; 110407154 free inodes.

server2 `/tmp`: 23044079616 available bytes; 98.71% used; 110407154 free inodes.

server2 `/var/tmp`: 23044079616 available bytes; 98.71% used; 110407154 free inodes.

server2 `/mnt/raid5`: 303205203968 available bytes; 97.90% used; 445057466 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84379025408 available bytes; 95.29% used; 114152620 free inodes.

server3 `/home`: 84379025408 available bytes; 95.29% used; 114152620 free inodes.

server3 `/data`: 127176237056 available bytes; 98.24% used; 225807979 free inodes.

server3 `/tmp`: 84379025408 available bytes; 95.29% used; 114152620 free inodes.

server3 `/var/tmp`: 84379025408 available bytes; 95.29% used; 114152620 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105656041472 available bytes; 94.10% used; 114349563 free inodes.

server4 `/home`: 105656041472 available bytes; 94.10% used; 114349563 free inodes.

server4 `/data`: 228340436992 available bytes; 96.84% used; 224928558 free inodes.

server4 `/tmp`: 105656041472 available bytes; 94.10% used; 114349563 free inodes.

server4 `/var/tmp`: 105656041472 available bytes; 94.10% used; 114349563 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
