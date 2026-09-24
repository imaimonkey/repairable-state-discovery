# V2R cluster inventory

2026-09-24T11:40:11.990246+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324344733696 available bytes; 81.91% used; 112488831 free inodes.

server1 `/home`: 324344733696 available bytes; 81.91% used; 112488831 free inodes.

server1 `/tmp`: 324344733696 available bytes; 81.91% used; 112488831 free inodes.

server1 `/var/tmp`: 324344733696 available bytes; 81.91% used; 112488831 free inodes.

server1 `/mnt/raid5`: 433022603264 available bytes; 98.01% used; 337688220 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57656324096 available bytes; 96.78% used; 110429904 free inodes.

server2 `/home`: 57656324096 available bytes; 96.78% used; 110429904 free inodes.

server2 `/tmp`: 57656324096 available bytes; 96.78% used; 110429904 free inodes.

server2 `/var/tmp`: 57656324096 available bytes; 96.78% used; 110429904 free inodes.

server2 `/mnt/raid5`: 510318247936 available bytes; 96.47% used; 445172968 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84924878848 available bytes; 95.26% used; 114148051 free inodes.

server3 `/home`: 84924878848 available bytes; 95.26% used; 114148051 free inodes.

server3 `/data`: 163733168128 available bytes; 97.74% used; 225816444 free inodes.

server3 `/tmp`: 84924878848 available bytes; 95.26% used; 114148051 free inodes.

server3 `/var/tmp`: 84924878848 available bytes; 95.26% used; 114148051 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105729851392 available bytes; 94.10% used; 114348864 free inodes.

server4 `/home`: 105729851392 available bytes; 94.10% used; 114348864 free inodes.

server4 `/data`: 115425550336 available bytes; 98.40% used; 225257979 free inodes.

server4 `/tmp`: 105729851392 available bytes; 94.10% used; 114348864 free inodes.

server4 `/var/tmp`: 105729851392 available bytes; 94.10% used; 114348864 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
