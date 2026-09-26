# V2R cluster inventory

2026-09-26T09:38:58.593675+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318618107904 available bytes; 82.23% used; 112475085 free inodes.

server1 `/home`: 318618107904 available bytes; 82.23% used; 112475085 free inodes.

server1 `/tmp`: 318618107904 available bytes; 82.23% used; 112475085 free inodes.

server1 `/var/tmp`: 318618107904 available bytes; 82.23% used; 112475085 free inodes.

server1 `/mnt/raid5`: 218947186688 available bytes; 99.00% used; 337538600 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22317727744 available bytes; 98.75% used; 110403896 free inodes.

server2 `/home`: 22317727744 available bytes; 98.75% used; 110403896 free inodes.

server2 `/tmp`: 22317727744 available bytes; 98.75% used; 110403896 free inodes.

server2 `/var/tmp`: 22317727744 available bytes; 98.75% used; 110403896 free inodes.

server2 `/mnt/raid5`: 253929529344 available bytes; 98.25% used; 445022515 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 82656133120 available bytes; 95.39% used; 114110805 free inodes.

server3 `/home`: 82656133120 available bytes; 95.39% used; 114110805 free inodes.

server3 `/data`: 123594465280 available bytes; 98.29% used; 225827645 free inodes.

server3 `/tmp`: 82656133120 available bytes; 95.39% used; 114110805 free inodes.

server3 `/var/tmp`: 82656133120 available bytes; 95.39% used; 114110805 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105934135296 available bytes; 94.09% used; 114348049 free inodes.

server4 `/home`: 105934135296 available bytes; 94.09% used; 114348049 free inodes.

server4 `/data`: 89277616128 available bytes; 98.77% used; 224882606 free inodes.

server4 `/tmp`: 105934135296 available bytes; 94.09% used; 114348049 free inodes.

server4 `/var/tmp`: 105934135296 available bytes; 94.09% used; 114348049 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
