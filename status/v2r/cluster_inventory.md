# V2R cluster inventory

2026-09-26T10:43:21.779530+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318213849088 available bytes; 82.25% used; 112474736 free inodes.

server1 `/home`: 318213849088 available bytes; 82.25% used; 112474736 free inodes.

server1 `/tmp`: 318213849088 available bytes; 82.25% used; 112474736 free inodes.

server1 `/var/tmp`: 318213849088 available bytes; 82.25% used; 112474736 free inodes.

server1 `/mnt/raid5`: 218803195904 available bytes; 99.00% used; 337538296 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19845713920 available bytes; 98.89% used; 110384895 free inodes.

server2 `/home`: 19845713920 available bytes; 98.89% used; 110384895 free inodes.

server2 `/tmp`: 19845713920 available bytes; 98.89% used; 110384895 free inodes.

server2 `/var/tmp`: 19845713920 available bytes; 98.89% used; 110384895 free inodes.

server2 `/mnt/raid5`: 242797309952 available bytes; 98.32% used; 444979088 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82657550336 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82657550336 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 123574194176 available bytes; 98.29% used; 225826557 free inodes.

server3 `/tmp`: 82657550336 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82657550336 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105927192576 available bytes; 94.09% used; 114347977 free inodes.

server4 `/home`: 105927192576 available bytes; 94.09% used; 114347977 free inodes.

server4 `/data`: 89064128512 available bytes; 98.77% used; 224880644 free inodes.

server4 `/tmp`: 105927192576 available bytes; 94.09% used; 114347977 free inodes.

server4 `/var/tmp`: 105927192576 available bytes; 94.09% used; 114347977 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
