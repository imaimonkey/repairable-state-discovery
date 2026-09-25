# V2R cluster inventory

2026-09-25T20:31:52.668388+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318704259072 available bytes; 82.22% used; 112476320 free inodes.

server1 `/home`: 318704259072 available bytes; 82.22% used; 112476320 free inodes.

server1 `/tmp`: 318704259072 available bytes; 82.22% used; 112476320 free inodes.

server1 `/var/tmp`: 318704259072 available bytes; 82.22% used; 112476320 free inodes.

server1 `/mnt/raid5`: 369392381952 available bytes; 98.31% used; 337540481 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 23043104768 available bytes; 98.71% used; 110407154 free inodes.

server2 `/home`: 23043104768 available bytes; 98.71% used; 110407154 free inodes.

server2 `/tmp`: 23043104768 available bytes; 98.71% used; 110407154 free inodes.

server2 `/var/tmp`: 23043104768 available bytes; 98.71% used; 110407154 free inodes.

server2 `/mnt/raid5`: 302709129216 available bytes; 97.91% used; 445057502 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381409280 available bytes; 95.29% used; 114152620 free inodes.

server3 `/home`: 84381409280 available bytes; 95.29% used; 114152620 free inodes.

server3 `/data`: 127175868416 available bytes; 98.24% used; 225808008 free inodes.

server3 `/tmp`: 84381409280 available bytes; 95.29% used; 114152620 free inodes.

server3 `/var/tmp`: 84381409280 available bytes; 95.29% used; 114152620 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105664475136 available bytes; 94.10% used; 114349566 free inodes.

server4 `/home`: 105664475136 available bytes; 94.10% used; 114349566 free inodes.

server4 `/data`: 228726169600 available bytes; 96.84% used; 224928807 free inodes.

server4 `/tmp`: 105664475136 available bytes; 94.10% used; 114349566 free inodes.

server4 `/var/tmp`: 105664475136 available bytes; 94.10% used; 114349566 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
