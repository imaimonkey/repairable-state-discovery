# V2R cluster inventory

2026-09-24T16:30:08.292671+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324023521280 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324023521280 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324023521280 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324023521280 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 416575242240 available bytes; 98.09% used; 337653379 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57326505984 available bytes; 96.80% used; 110426883 free inodes.

server2 `/home`: 57326505984 available bytes; 96.80% used; 110426883 free inodes.

server2 `/tmp`: 57326505984 available bytes; 96.80% used; 110426883 free inodes.

server2 `/var/tmp`: 57326505984 available bytes; 96.80% used; 110426883 free inodes.

server2 `/mnt/raid5`: 500948615168 available bytes; 96.54% used; 445164568 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84704444416 available bytes; 95.27% used; 114179290 free inodes.

server3 `/home`: 84704444416 available bytes; 95.27% used; 114179290 free inodes.

server3 `/data`: 159353987072 available bytes; 97.80% used; 225788027 free inodes.

server3 `/tmp`: 84704444416 available bytes; 95.27% used; 114179290 free inodes.

server3 `/var/tmp`: 84704444416 available bytes; 95.27% used; 114179290 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105688727552 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105688727552 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89281785856 available bytes; 98.77% used; 225255848 free inodes.

server4 `/tmp`: 105688727552 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105688727552 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
