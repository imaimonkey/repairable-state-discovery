# V2R cluster inventory

2026-09-25T05:26:56.837875+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318871728128 available bytes; 82.21% used; 112480348 free inodes.

server1 `/home`: 318871728128 available bytes; 82.21% used; 112480348 free inodes.

server1 `/tmp`: 318871728128 available bytes; 82.21% used; 112480348 free inodes.

server1 `/var/tmp`: 318871728128 available bytes; 82.21% used; 112480348 free inodes.

server1 `/mnt/raid5`: 408499822592 available bytes; 98.13% used; 337568647 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22922477568 available bytes; 98.72% used; 110410445 free inodes.

server2 `/home`: 22922477568 available bytes; 98.72% used; 110410445 free inodes.

server2 `/tmp`: 22922477568 available bytes; 98.72% used; 110410445 free inodes.

server2 `/var/tmp`: 22922477568 available bytes; 98.72% used; 110410445 free inodes.

server2 `/mnt/raid5`: 461275574272 available bytes; 96.81% used; 445108289 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84317274112 available bytes; 95.29% used; 114156052 free inodes.

server3 `/home`: 84317274112 available bytes; 95.29% used; 114156052 free inodes.

server3 `/data`: 142775881728 available bytes; 98.03% used; 225814868 free inodes.

server3 `/tmp`: 84317274112 available bytes; 95.29% used; 114156052 free inodes.

server3 `/var/tmp`: 84317274112 available bytes; 95.29% used; 114156052 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105658535936 available bytes; 94.10% used; 114350398 free inodes.

server4 `/home`: 105658535936 available bytes; 94.10% used; 114350398 free inodes.

server4 `/data`: 26430205952 available bytes; 99.63% used; 224968483 free inodes.

server4 `/tmp`: 105658535936 available bytes; 94.10% used; 114350398 free inodes.

server4 `/var/tmp`: 105658535936 available bytes; 94.10% used; 114350398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
