# V2R cluster inventory

2026-09-24T19:46:20.662429+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323988758528 available bytes; 81.93% used; 112481463 free inodes.

server1 `/home`: 323988758528 available bytes; 81.93% used; 112481463 free inodes.

server1 `/tmp`: 323988758528 available bytes; 81.93% used; 112481463 free inodes.

server1 `/var/tmp`: 323988758528 available bytes; 81.93% used; 112481463 free inodes.

server1 `/mnt/raid5`: 415584858112 available bytes; 98.09% used; 337630476 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 44743122944 available bytes; 97.50% used; 110411674 free inodes.

server2 `/home`: 44743122944 available bytes; 97.50% used; 110411674 free inodes.

server2 `/tmp`: 44743122944 available bytes; 97.50% used; 110411674 free inodes.

server2 `/var/tmp`: 44743122944 available bytes; 97.50% used; 110411674 free inodes.

server2 `/mnt/raid5`: 494367698944 available bytes; 96.58% used; 445158212 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84399603712 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84399603712 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152121028608 available bytes; 97.90% used; 225799188 free inodes.

server3 `/tmp`: 84399603712 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84399603712 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105642237952 available bytes; 94.10% used; 114348430 free inodes.

server4 `/home`: 105642237952 available bytes; 94.10% used; 114348430 free inodes.

server4 `/data`: 89854046208 available bytes; 98.76% used; 225266563 free inodes.

server4 `/tmp`: 105642237952 available bytes; 94.10% used; 114348430 free inodes.

server4 `/var/tmp`: 105642237952 available bytes; 94.10% used; 114348430 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
