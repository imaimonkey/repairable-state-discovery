# V2R cluster inventory

2026-09-25T13:22:04.410500+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319108894720 available bytes; 82.20% used; 112477575 free inodes.

server1 `/home`: 319108894720 available bytes; 82.20% used; 112477575 free inodes.

server1 `/tmp`: 319108894720 available bytes; 82.20% used; 112477575 free inodes.

server1 `/var/tmp`: 319108894720 available bytes; 82.20% used; 112477575 free inodes.

server1 `/mnt/raid5`: 365299388416 available bytes; 98.32% used; 337547871 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 8382623744 available bytes; 99.53% used; 110408244 free inodes.

server2 `/home`: 8382623744 available bytes; 99.53% used; 110408244 free inodes.

server2 `/tmp`: 8382623744 available bytes; 99.53% used; 110408244 free inodes.

server2 `/var/tmp`: 8382623744 available bytes; 99.53% used; 110408244 free inodes.

server2 `/mnt/raid5`: 323687239680 available bytes; 97.76% used; 445077184 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84198318080 available bytes; 95.30% used; 114154966 free inodes.

server3 `/home`: 84198318080 available bytes; 95.30% used; 114154966 free inodes.

server3 `/data`: 142349148160 available bytes; 98.03% used; 225809846 free inodes.

server3 `/tmp`: 84198318080 available bytes; 95.30% used; 114154966 free inodes.

server3 `/var/tmp`: 84198318080 available bytes; 95.30% used; 114154966 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105656164352 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656164352 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231412330496 available bytes; 96.80% used; 224952784 free inodes.

server4 `/tmp`: 105656164352 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656164352 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
