# V2R cluster inventory

2026-09-25T13:15:55.889630+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319110090752 available bytes; 82.20% used; 112477575 free inodes.

server1 `/home`: 319110090752 available bytes; 82.20% used; 112477575 free inodes.

server1 `/tmp`: 319110090752 available bytes; 82.20% used; 112477575 free inodes.

server1 `/var/tmp`: 319110090752 available bytes; 82.20% used; 112477575 free inodes.

server1 `/mnt/raid5`: 364252766208 available bytes; 98.33% used; 337547883 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 8375275520 available bytes; 99.53% used; 110408249 free inodes.

server2 `/home`: 8375275520 available bytes; 99.53% used; 110408249 free inodes.

server2 `/tmp`: 8375275520 available bytes; 99.53% used; 110408249 free inodes.

server2 `/var/tmp`: 8375275520 available bytes; 99.53% used; 110408249 free inodes.

server2 `/mnt/raid5`: 323870720000 available bytes; 97.76% used; 445077349 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84207423488 available bytes; 95.30% used; 114154966 free inodes.

server3 `/home`: 84207423488 available bytes; 95.30% used; 114154966 free inodes.

server3 `/data`: 142350610432 available bytes; 98.03% used; 225809934 free inodes.

server3 `/tmp`: 84207423488 available bytes; 95.30% used; 114154966 free inodes.

server3 `/var/tmp`: 84207423488 available bytes; 95.30% used; 114154966 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105656360960 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656360960 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231418818560 available bytes; 96.80% used; 224953545 free inodes.

server4 `/tmp`: 105656360960 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656360960 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
