# V2R cluster inventory

2026-09-25T20:34:56.145065+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318704357376 available bytes; 82.22% used; 112476321 free inodes.

server1 `/home`: 318704357376 available bytes; 82.22% used; 112476321 free inodes.

server1 `/tmp`: 318704357376 available bytes; 82.22% used; 112476321 free inodes.

server1 `/var/tmp`: 318704357376 available bytes; 82.22% used; 112476321 free inodes.

server1 `/mnt/raid5`: 369390411776 available bytes; 98.31% used; 337540474 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 23046856704 available bytes; 98.71% used; 110407156 free inodes.

server2 `/home`: 23046856704 available bytes; 98.71% used; 110407156 free inodes.

server2 `/tmp`: 23046856704 available bytes; 98.71% used; 110407156 free inodes.

server2 `/var/tmp`: 23046856704 available bytes; 98.71% used; 110407156 free inodes.

server2 `/mnt/raid5`: 303154364416 available bytes; 97.91% used; 445057299 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381323264 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84381323264 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127173156864 available bytes; 98.24% used; 225807957 free inodes.

server3 `/tmp`: 84381323264 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84381323264 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655939072 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655939072 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228337786880 available bytes; 96.84% used; 224928557 free inodes.

server4 `/tmp`: 105655939072 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655939072 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
