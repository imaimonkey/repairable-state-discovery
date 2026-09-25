# V2R cluster inventory

2026-09-25T20:39:31.435027+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318707269632 available bytes; 82.22% used; 112476306 free inodes.

server1 `/home`: 318707269632 available bytes; 82.22% used; 112476306 free inodes.

server1 `/tmp`: 318707269632 available bytes; 82.22% used; 112476306 free inodes.

server1 `/var/tmp`: 318707269632 available bytes; 82.22% used; 112476306 free inodes.

server1 `/mnt/raid5`: 368708431872 available bytes; 98.31% used; 337540425 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 22995877888 available bytes; 98.72% used; 110406376 free inodes.

server2 `/home`: 22995877888 available bytes; 98.72% used; 110406376 free inodes.

server2 `/tmp`: 22995877888 available bytes; 98.72% used; 110406376 free inodes.

server2 `/var/tmp`: 22995877888 available bytes; 98.72% used; 110406376 free inodes.

server2 `/mnt/raid5`: 303023464448 available bytes; 97.91% used; 445057144 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381966336 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84381966336 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 127172521984 available bytes; 98.24% used; 225807869 free inodes.

server3 `/tmp`: 84381966336 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84381966336 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655808000 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655808000 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228328210432 available bytes; 96.84% used; 224928545 free inodes.

server4 `/tmp`: 105655808000 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655808000 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
