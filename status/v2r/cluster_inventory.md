# V2R cluster inventory

2026-09-25T00:04:09.510156+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319089426432 available bytes; 82.20% used; 112480778 free inodes.

server1 `/home`: 319089426432 available bytes; 82.20% used; 112480778 free inodes.

server1 `/tmp`: 319089426432 available bytes; 82.20% used; 112480778 free inodes.

server1 `/var/tmp`: 319089426432 available bytes; 82.20% used; 112480778 free inodes.

server1 `/mnt/raid5`: 416901611520 available bytes; 98.09% used; 337622896 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23093063680 available bytes; 98.71% used; 110410784 free inodes.

server2 `/home`: 23093063680 available bytes; 98.71% used; 110410784 free inodes.

server2 `/tmp`: 23093063680 available bytes; 98.71% used; 110410784 free inodes.

server2 `/var/tmp`: 23093063680 available bytes; 98.71% used; 110410784 free inodes.

server2 `/mnt/raid5`: 486752976896 available bytes; 96.64% used; 445163711 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352200704 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84352200704 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149402259456 available bytes; 97.94% used; 225813930 free inodes.

server3 `/tmp`: 84352200704 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84352200704 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105798230016 available bytes; 94.10% used; 114348299 free inodes.

server4 `/home`: 105798230016 available bytes; 94.10% used; 114348299 free inodes.

server4 `/data`: 59928195072 available bytes; 99.17% used; 225096060 free inodes.

server4 `/tmp`: 105798230016 available bytes; 94.10% used; 114348299 free inodes.

server4 `/var/tmp`: 105798230016 available bytes; 94.10% used; 114348299 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
