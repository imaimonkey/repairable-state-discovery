# V2R cluster inventory

2026-09-25T01:51:54.249615+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319025328128 available bytes; 82.20% used; 112480595 free inodes.

server1 `/home`: 319025328128 available bytes; 82.20% used; 112480595 free inodes.

server1 `/tmp`: 319025328128 available bytes; 82.20% used; 112480595 free inodes.

server1 `/var/tmp`: 319025328128 available bytes; 82.20% used; 112480595 free inodes.

server1 `/mnt/raid5`: 416442699776 available bytes; 98.09% used; 337610404 free inodes.
| server2 | True | ['2', '3', '6'] | [] |

server2 `/`: 23040094208 available bytes; 98.71% used; 110410753 free inodes.

server2 `/home`: 23040094208 available bytes; 98.71% used; 110410753 free inodes.

server2 `/tmp`: 23040094208 available bytes; 98.71% used; 110410753 free inodes.

server2 `/var/tmp`: 23040094208 available bytes; 98.71% used; 110410753 free inodes.

server2 `/mnt/raid5`: 490435076096 available bytes; 96.61% used; 445160961 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84357615616 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84357615616 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 146323656704 available bytes; 97.98% used; 225811888 free inodes.

server3 `/tmp`: 84357615616 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84357615616 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761415168 available bytes; 94.10% used; 114348267 free inodes.

server4 `/home`: 105761415168 available bytes; 94.10% used; 114348267 free inodes.

server4 `/data`: 53307822080 available bytes; 99.26% used; 225030524 free inodes.

server4 `/tmp`: 105761415168 available bytes; 94.10% used; 114348267 free inodes.

server4 `/var/tmp`: 105761415168 available bytes; 94.10% used; 114348267 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
