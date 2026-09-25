# V2R cluster inventory

2026-09-25T00:31:48.443629+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319087190016 available bytes; 82.20% used; 112480776 free inodes.

server1 `/home`: 319087190016 available bytes; 82.20% used; 112480776 free inodes.

server1 `/tmp`: 319087190016 available bytes; 82.20% used; 112480776 free inodes.

server1 `/var/tmp`: 319087190016 available bytes; 82.20% used; 112480776 free inodes.

server1 `/mnt/raid5`: 416851861504 available bytes; 98.09% used; 337619683 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23080783872 available bytes; 98.71% used; 110410771 free inodes.

server2 `/home`: 23080783872 available bytes; 98.71% used; 110410771 free inodes.

server2 `/tmp`: 23080783872 available bytes; 98.71% used; 110410771 free inodes.

server2 `/var/tmp`: 23080783872 available bytes; 98.71% used; 110410771 free inodes.

server2 `/mnt/raid5`: 501764022272 available bytes; 96.53% used; 445162899 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84349829120 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84349829120 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 148860067840 available bytes; 97.94% used; 225813404 free inodes.

server3 `/tmp`: 84349829120 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84349829120 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788895232 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105788895232 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56626221056 available bytes; 99.22% used; 225056035 free inodes.

server4 `/tmp`: 105788895232 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105788895232 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
