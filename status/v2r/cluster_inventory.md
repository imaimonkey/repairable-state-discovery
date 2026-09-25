# V2R cluster inventory

2026-09-25T06:13:44.206188+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318877581312 available bytes; 82.21% used; 112480344 free inodes.

server1 `/home`: 318877581312 available bytes; 82.21% used; 112480344 free inodes.

server1 `/tmp`: 318877581312 available bytes; 82.21% used; 112480344 free inodes.

server1 `/var/tmp`: 318877581312 available bytes; 82.21% used; 112480344 free inodes.

server1 `/mnt/raid5`: 401481437184 available bytes; 98.16% used; 337563009 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22893654016 available bytes; 98.72% used; 110410512 free inodes.

server2 `/home`: 22893654016 available bytes; 98.72% used; 110410512 free inodes.

server2 `/tmp`: 22893654016 available bytes; 98.72% used; 110410512 free inodes.

server2 `/var/tmp`: 22893654016 available bytes; 98.72% used; 110410512 free inodes.

server2 `/mnt/raid5`: 375172673536 available bytes; 97.41% used; 445100513 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84316930048 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84316930048 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142534008832 available bytes; 98.03% used; 225814072 free inodes.

server3 `/tmp`: 84316930048 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84316930048 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648709632 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105648709632 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 254654021632 available bytes; 96.48% used; 225023862 free inodes.

server4 `/tmp`: 105648709632 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105648709632 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
