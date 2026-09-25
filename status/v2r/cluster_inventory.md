# V2R cluster inventory

2026-09-25T20:41:03.138519+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318708379648 available bytes; 82.22% used; 112476308 free inodes.

server1 `/home`: 318708379648 available bytes; 82.22% used; 112476308 free inodes.

server1 `/tmp`: 318708379648 available bytes; 82.22% used; 112476308 free inodes.

server1 `/var/tmp`: 318708379648 available bytes; 82.22% used; 112476308 free inodes.

server1 `/mnt/raid5`: 368703602688 available bytes; 98.31% used; 337540412 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 22956290048 available bytes; 98.72% used; 110406251 free inodes.

server2 `/home`: 22956290048 available bytes; 98.72% used; 110406251 free inodes.

server2 `/tmp`: 22956290048 available bytes; 98.72% used; 110406251 free inodes.

server2 `/var/tmp`: 22956290048 available bytes; 98.72% used; 110406251 free inodes.

server2 `/mnt/raid5`: 302977503232 available bytes; 97.91% used; 445057030 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381831168 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84381831168 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 127170240512 available bytes; 98.24% used; 225807854 free inodes.

server3 `/tmp`: 84381831168 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84381831168 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655750656 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655750656 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228327596032 available bytes; 96.84% used; 224928538 free inodes.

server4 `/tmp`: 105655750656 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655750656 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
