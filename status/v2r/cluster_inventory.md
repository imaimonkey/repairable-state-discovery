# V2R cluster inventory

2026-09-24T19:35:31.977671+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323990876160 available bytes; 81.93% used; 112481455 free inodes.

server1 `/home`: 323990876160 available bytes; 81.93% used; 112481455 free inodes.

server1 `/tmp`: 323990876160 available bytes; 81.93% used; 112481455 free inodes.

server1 `/var/tmp`: 323990876160 available bytes; 81.93% used; 112481455 free inodes.

server1 `/mnt/raid5`: 415603388416 available bytes; 98.09% used; 337631732 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54453002240 available bytes; 96.96% used; 110411859 free inodes.

server2 `/home`: 54453002240 available bytes; 96.96% used; 110411859 free inodes.

server2 `/tmp`: 54453002240 available bytes; 96.96% used; 110411859 free inodes.

server2 `/var/tmp`: 54453002240 available bytes; 96.96% used; 110411859 free inodes.

server2 `/mnt/raid5`: 494692962304 available bytes; 96.58% used; 445158648 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84400730112 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84400730112 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152220000256 available bytes; 97.90% used; 225799391 free inodes.

server3 `/tmp`: 84400730112 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84400730112 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105659625472 available bytes; 94.10% used; 114348452 free inodes.

server4 `/home`: 105659625472 available bytes; 94.10% used; 114348452 free inodes.

server4 `/data`: 89866186752 available bytes; 98.76% used; 225266761 free inodes.

server4 `/tmp`: 105659625472 available bytes; 94.10% used; 114348452 free inodes.

server4 `/var/tmp`: 105659625472 available bytes; 94.10% used; 114348452 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
