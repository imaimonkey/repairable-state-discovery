# V2R cluster inventory

2026-09-25T11:45:17.326615+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319061340160 available bytes; 82.20% used; 112478833 free inodes.

server1 `/home`: 319061340160 available bytes; 82.20% used; 112478833 free inodes.

server1 `/tmp`: 319061340160 available bytes; 82.20% used; 112478833 free inodes.

server1 `/var/tmp`: 319061340160 available bytes; 82.20% used; 112478833 free inodes.

server1 `/mnt/raid5`: 364349607936 available bytes; 98.33% used; 337549176 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22905524224 available bytes; 98.72% used; 110409983 free inodes.

server2 `/home`: 22905524224 available bytes; 98.72% used; 110409983 free inodes.

server2 `/tmp`: 22905524224 available bytes; 98.72% used; 110409983 free inodes.

server2 `/var/tmp`: 22905524224 available bytes; 98.72% used; 110409983 free inodes.

server2 `/mnt/raid5`: 326126936064 available bytes; 97.75% used; 445083006 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 84213690368 available bytes; 95.30% used; 114155009 free inodes.

server3 `/home`: 84213690368 available bytes; 95.30% used; 114155009 free inodes.

server3 `/data`: 142044160000 available bytes; 98.04% used; 225813414 free inodes.

server3 `/tmp`: 84213690368 available bytes; 95.30% used; 114155009 free inodes.

server3 `/var/tmp`: 84213690368 available bytes; 95.30% used; 114155009 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105602727936 available bytes; 94.11% used; 114350248 free inodes.

server4 `/home`: 105602727936 available bytes; 94.11% used; 114350248 free inodes.

server4 `/data`: 232554950656 available bytes; 96.79% used; 224975590 free inodes.

server4 `/tmp`: 105602727936 available bytes; 94.11% used; 114350248 free inodes.

server4 `/var/tmp`: 105602727936 available bytes; 94.11% used; 114350248 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
