# V2R cluster inventory

2026-09-25T11:23:52.786626+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319062679552 available bytes; 82.20% used; 112478822 free inodes.

server1 `/home`: 319062679552 available bytes; 82.20% used; 112478822 free inodes.

server1 `/tmp`: 319062679552 available bytes; 82.20% used; 112478822 free inodes.

server1 `/var/tmp`: 319062679552 available bytes; 82.20% used; 112478822 free inodes.

server1 `/mnt/raid5`: 366239518720 available bytes; 98.32% used; 337550328 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22911877120 available bytes; 98.72% used; 110409978 free inodes.

server2 `/home`: 22911877120 available bytes; 98.72% used; 110409978 free inodes.

server2 `/tmp`: 22911877120 available bytes; 98.72% used; 110409978 free inodes.

server2 `/var/tmp`: 22911877120 available bytes; 98.72% used; 110409978 free inodes.

server2 `/mnt/raid5`: 327735136256 available bytes; 97.74% used; 445083785 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84131983360 available bytes; 95.31% used; 114155498 free inodes.

server3 `/home`: 84131983360 available bytes; 95.31% used; 114155498 free inodes.

server3 `/data`: 142083313664 available bytes; 98.04% used; 225814303 free inodes.

server3 `/tmp`: 84131983360 available bytes; 95.31% used; 114155498 free inodes.

server3 `/var/tmp`: 84131983360 available bytes; 95.31% used; 114155498 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105611776000 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105611776000 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238627311616 available bytes; 96.70% used; 224980786 free inodes.

server4 `/tmp`: 105611776000 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105611776000 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
