# V2R cluster inventory

2026-09-25T10:33:19.226956+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319000330240 available bytes; 82.20% used; 112479388 free inodes.

server1 `/home`: 319000330240 available bytes; 82.20% used; 112479388 free inodes.

server1 `/tmp`: 319000330240 available bytes; 82.20% used; 112479388 free inodes.

server1 `/var/tmp`: 319000330240 available bytes; 82.20% used; 112479388 free inodes.

server1 `/mnt/raid5`: 364837007360 available bytes; 98.33% used; 337555268 free inodes.
| server2 | True | ['0', '3', '5', '6'] | [] |

server2 `/`: 22825259008 available bytes; 98.73% used; 110410496 free inodes.

server2 `/home`: 22825259008 available bytes; 98.73% used; 110410496 free inodes.

server2 `/tmp`: 22825259008 available bytes; 98.73% used; 110410496 free inodes.

server2 `/var/tmp`: 22825259008 available bytes; 98.73% used; 110410496 free inodes.

server2 `/mnt/raid5`: 316128219136 available bytes; 97.82% used; 445089998 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84416770048 available bytes; 95.29% used; 114156033 free inodes.

server3 `/home`: 84416770048 available bytes; 95.29% used; 114156033 free inodes.

server3 `/data`: 142007357440 available bytes; 98.04% used; 225815688 free inodes.

server3 `/tmp`: 84416770048 available bytes; 95.29% used; 114156033 free inodes.

server3 `/var/tmp`: 84416770048 available bytes; 95.29% used; 114156033 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105613271040 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105613271040 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238521790464 available bytes; 96.70% used; 224986784 free inodes.

server4 `/tmp`: 105613271040 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105613271040 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
