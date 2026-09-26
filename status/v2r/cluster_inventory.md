# V2R cluster inventory

2026-09-26T04:52:16.329699+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318401089536 available bytes; 82.24% used; 112476282 free inodes.

server1 `/home`: 318401089536 available bytes; 82.24% used; 112476282 free inodes.

server1 `/tmp`: 318401089536 available bytes; 82.24% used; 112476282 free inodes.

server1 `/var/tmp`: 318401089536 available bytes; 82.24% used; 112476282 free inodes.

server1 `/mnt/raid5`: 330466463744 available bytes; 98.48% used; 337545348 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22937034752 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22937034752 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22937034752 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22937034752 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 284856078336 available bytes; 98.03% used; 445049850 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83475247104 available bytes; 95.34% used; 114122272 free inodes.

server3 `/home`: 83475247104 available bytes; 95.34% used; 114122272 free inodes.

server3 `/data`: 124378935296 available bytes; 98.28% used; 225816551 free inodes.

server3 `/tmp`: 83475247104 available bytes; 95.34% used; 114122272 free inodes.

server3 `/var/tmp`: 83475247104 available bytes; 95.34% used; 114122272 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106001784832 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106001784832 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 107021934592 available bytes; 98.52% used; 224929297 free inodes.

server4 `/tmp`: 106001784832 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106001784832 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
