# V2R cluster inventory

2026-09-25T11:38:03.260691+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319061979136 available bytes; 82.20% used; 112478822 free inodes.

server1 `/home`: 319061979136 available bytes; 82.20% used; 112478822 free inodes.

server1 `/tmp`: 319061979136 available bytes; 82.20% used; 112478822 free inodes.

server1 `/var/tmp`: 319061979136 available bytes; 82.20% used; 112478822 free inodes.

server1 `/mnt/raid5`: 364272910336 available bytes; 98.33% used; 337549720 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22903386112 available bytes; 98.72% used; 110409980 free inodes.

server2 `/home`: 22903386112 available bytes; 98.72% used; 110409980 free inodes.

server2 `/tmp`: 22903386112 available bytes; 98.72% used; 110409980 free inodes.

server2 `/var/tmp`: 22903386112 available bytes; 98.72% used; 110409980 free inodes.

server2 `/mnt/raid5`: 326593486848 available bytes; 97.74% used; 445083120 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 84131090432 available bytes; 95.31% used; 114155520 free inodes.

server3 `/home`: 84131090432 available bytes; 95.31% used; 114155520 free inodes.

server3 `/data`: 142115192832 available bytes; 98.04% used; 225813528 free inodes.

server3 `/tmp`: 84131090432 available bytes; 95.31% used; 114155520 free inodes.

server3 `/var/tmp`: 84131090432 available bytes; 95.31% used; 114155520 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105602932736 available bytes; 94.11% used; 114350248 free inodes.

server4 `/home`: 105602932736 available bytes; 94.11% used; 114350248 free inodes.

server4 `/data`: 234803425280 available bytes; 96.75% used; 224976732 free inodes.

server4 `/tmp`: 105602932736 available bytes; 94.11% used; 114350248 free inodes.

server4 `/var/tmp`: 105602932736 available bytes; 94.11% used; 114350248 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
