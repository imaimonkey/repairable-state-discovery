# V2R cluster inventory

2026-09-25T06:12:12.146262+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318877941760 available bytes; 82.21% used; 112480344 free inodes.

server1 `/home`: 318877941760 available bytes; 82.21% used; 112480344 free inodes.

server1 `/tmp`: 318877941760 available bytes; 82.21% used; 112480344 free inodes.

server1 `/var/tmp`: 318877941760 available bytes; 82.21% used; 112480344 free inodes.

server1 `/mnt/raid5`: 401485225984 available bytes; 98.16% used; 337563190 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22900416512 available bytes; 98.72% used; 110410514 free inodes.

server2 `/home`: 22900416512 available bytes; 98.72% used; 110410514 free inodes.

server2 `/tmp`: 22900416512 available bytes; 98.72% used; 110410514 free inodes.

server2 `/var/tmp`: 22900416512 available bytes; 98.72% used; 110410514 free inodes.

server2 `/mnt/raid5`: 375210893312 available bytes; 97.41% used; 445100353 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84317450240 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84317450240 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142534971392 available bytes; 98.03% used; 225814109 free inodes.

server3 `/tmp`: 84317450240 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84317450240 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648766976 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105648766976 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 254658211840 available bytes; 96.48% used; 225024010 free inodes.

server4 `/tmp`: 105648766976 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105648766976 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
