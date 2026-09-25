# V2R cluster inventory

2026-09-25T20:39:15.157678+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318707306496 available bytes; 82.22% used; 112476322 free inodes.

server1 `/home`: 318707306496 available bytes; 82.22% used; 112476322 free inodes.

server1 `/tmp`: 318707306496 available bytes; 82.22% used; 112476322 free inodes.

server1 `/var/tmp`: 318707306496 available bytes; 82.22% used; 112476322 free inodes.

server1 `/mnt/raid5`: 368708620288 available bytes; 98.31% used; 337540425 free inodes.
| server2 | True | ['4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22996000768 available bytes; 98.72% used; 110406376 free inodes.

server2 `/home`: 22996000768 available bytes; 98.72% used; 110406376 free inodes.

server2 `/tmp`: 22996000768 available bytes; 98.72% used; 110406376 free inodes.

server2 `/var/tmp`: 22996000768 available bytes; 98.72% used; 110406376 free inodes.

server2 `/mnt/raid5`: 303028228096 available bytes; 97.91% used; 445057144 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84381966336 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84381966336 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 127173107712 available bytes; 98.24% used; 225807886 free inodes.

server3 `/tmp`: 84381966336 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84381966336 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655816192 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655816192 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228328419328 available bytes; 96.84% used; 224928546 free inodes.

server4 `/tmp`: 105655816192 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655816192 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
