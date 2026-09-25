# V2R cluster inventory

2026-09-25T01:53:26.258768+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319025090560 available bytes; 82.20% used; 112480595 free inodes.

server1 `/home`: 319025090560 available bytes; 82.20% used; 112480595 free inodes.

server1 `/tmp`: 319025090560 available bytes; 82.20% used; 112480595 free inodes.

server1 `/var/tmp`: 319025090560 available bytes; 82.20% used; 112480595 free inodes.

server1 `/mnt/raid5`: 416438927360 available bytes; 98.09% used; 337610229 free inodes.
| server2 | True | ['2', '3', '4', '6'] | [] |

server2 `/`: 23039967232 available bytes; 98.71% used; 110410757 free inodes.

server2 `/home`: 23039967232 available bytes; 98.71% used; 110410757 free inodes.

server2 `/tmp`: 23039967232 available bytes; 98.71% used; 110410757 free inodes.

server2 `/var/tmp`: 23039967232 available bytes; 98.71% used; 110410757 free inodes.

server2 `/mnt/raid5`: 493874327552 available bytes; 96.59% used; 445160935 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84357324800 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84357324800 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 146287075328 available bytes; 97.98% used; 225811864 free inodes.

server3 `/tmp`: 84357324800 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84357324800 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761382400 available bytes; 94.10% used; 114348266 free inodes.

server4 `/home`: 105761382400 available bytes; 94.10% used; 114348266 free inodes.

server4 `/data`: 53306490880 available bytes; 99.26% used; 225030491 free inodes.

server4 `/tmp`: 105761382400 available bytes; 94.10% used; 114348266 free inodes.

server4 `/var/tmp`: 105761382400 available bytes; 94.10% used; 114348266 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
