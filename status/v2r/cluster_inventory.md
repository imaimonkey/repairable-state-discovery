# V2R cluster inventory

2026-09-25T12:51:28.005879+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319109136384 available bytes; 82.20% used; 112477582 free inodes.

server1 `/home`: 319109136384 available bytes; 82.20% used; 112477582 free inodes.

server1 `/tmp`: 319109136384 available bytes; 82.20% used; 112477582 free inodes.

server1 `/var/tmp`: 319109136384 available bytes; 82.20% used; 112477582 free inodes.

server1 `/mnt/raid5`: 364480864256 available bytes; 98.33% used; 337547962 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 13883543552 available bytes; 99.23% used; 110409096 free inodes.

server2 `/home`: 13883543552 available bytes; 99.23% used; 110409096 free inodes.

server2 `/tmp`: 13883543552 available bytes; 99.23% used; 110409096 free inodes.

server2 `/var/tmp`: 13883543552 available bytes; 99.23% used; 110409096 free inodes.

server2 `/mnt/raid5`: 324504424448 available bytes; 97.76% used; 445078708 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84209377280 available bytes; 95.30% used; 114154974 free inodes.

server3 `/home`: 84209377280 available bytes; 95.30% used; 114154974 free inodes.

server3 `/data`: 142273703936 available bytes; 98.03% used; 225810864 free inodes.

server3 `/tmp`: 84209377280 available bytes; 95.30% used; 114154974 free inodes.

server3 `/var/tmp`: 84209377280 available bytes; 95.30% used; 114154974 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105665462272 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665462272 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 232010924032 available bytes; 96.79% used; 224961226 free inodes.

server4 `/tmp`: 105665462272 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665462272 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
