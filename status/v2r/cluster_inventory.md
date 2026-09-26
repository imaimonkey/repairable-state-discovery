# V2R cluster inventory

2026-09-26T06:17:16.255317+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318778380288 available bytes; 82.22% used; 112476286 free inodes.

server1 `/home`: 318778380288 available bytes; 82.22% used; 112476286 free inodes.

server1 `/tmp`: 318778380288 available bytes; 82.22% used; 112476286 free inodes.

server1 `/var/tmp`: 318778380288 available bytes; 82.22% used; 112476286 free inodes.

server1 `/mnt/raid5`: 219708878848 available bytes; 98.99% used; 337539866 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22319390720 available bytes; 98.75% used; 110403783 free inodes.

server2 `/home`: 22319390720 available bytes; 98.75% used; 110403783 free inodes.

server2 `/tmp`: 22319390720 available bytes; 98.75% used; 110403783 free inodes.

server2 `/var/tmp`: 22319390720 available bytes; 98.75% used; 110403783 free inodes.

server2 `/mnt/raid5`: 273409966080 available bytes; 98.11% used; 445029145 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82568790016 available bytes; 95.39% used; 114110905 free inodes.

server3 `/home`: 82568790016 available bytes; 95.39% used; 114110905 free inodes.

server3 `/data`: 123990216704 available bytes; 98.29% used; 225822496 free inodes.

server3 `/tmp`: 82568790016 available bytes; 95.39% used; 114110905 free inodes.

server3 `/var/tmp`: 82568790016 available bytes; 95.39% used; 114110905 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105981714432 available bytes; 94.09% used; 114347060 free inodes.

server4 `/home`: 105981714432 available bytes; 94.09% used; 114347060 free inodes.

server4 `/data`: 106568314880 available bytes; 98.53% used; 224923574 free inodes.

server4 `/tmp`: 105981714432 available bytes; 94.09% used; 114347060 free inodes.

server4 `/var/tmp`: 105981714432 available bytes; 94.09% used; 114347060 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
