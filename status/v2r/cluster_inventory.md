# V2R cluster inventory

2026-09-25T13:25:11.410425+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319111110656 available bytes; 82.20% used; 112477581 free inodes.

server1 `/home`: 319111110656 available bytes; 82.20% used; 112477581 free inodes.

server1 `/tmp`: 319111110656 available bytes; 82.20% used; 112477581 free inodes.

server1 `/var/tmp`: 319111110656 available bytes; 82.20% used; 112477581 free inodes.

server1 `/mnt/raid5`: 364246994944 available bytes; 98.33% used; 337547856 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 15493558272 available bytes; 99.14% used; 110408609 free inodes.

server2 `/home`: 15493558272 available bytes; 99.14% used; 110408609 free inodes.

server2 `/tmp`: 15493558272 available bytes; 99.14% used; 110408609 free inodes.

server2 `/var/tmp`: 15493558272 available bytes; 99.14% used; 110408609 free inodes.

server2 `/mnt/raid5`: 323606347776 available bytes; 97.76% used; 445077201 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84200407040 available bytes; 95.30% used; 114154968 free inodes.

server3 `/home`: 84200407040 available bytes; 95.30% used; 114154968 free inodes.

server3 `/data`: 142347804672 available bytes; 98.03% used; 225809797 free inodes.

server3 `/tmp`: 84200407040 available bytes; 95.30% used; 114154968 free inodes.

server3 `/var/tmp`: 84200407040 available bytes; 95.30% used; 114154968 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105656078336 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656078336 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231403851776 available bytes; 96.80% used; 224952401 free inodes.

server4 `/tmp`: 105656078336 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656078336 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
