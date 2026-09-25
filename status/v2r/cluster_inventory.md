# V2R cluster inventory

2026-09-25T03:45:52.151733+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318937767936 available bytes; 82.21% used; 112480346 free inodes.

server1 `/home`: 318937767936 available bytes; 82.21% used; 112480346 free inodes.

server1 `/tmp`: 318937767936 available bytes; 82.21% used; 112480346 free inodes.

server1 `/var/tmp`: 318937767936 available bytes; 82.21% used; 112480346 free inodes.

server1 `/mnt/raid5`: 415749201920 available bytes; 98.09% used; 337597035 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22972919808 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22972919808 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22972919808 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22972919808 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 464411697152 available bytes; 96.79% used; 445111409 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341547008 available bytes; 95.29% used; 114156061 free inodes.

server3 `/home`: 84341547008 available bytes; 95.29% used; 114156061 free inodes.

server3 `/data`: 144332455936 available bytes; 98.01% used; 225817152 free inodes.

server3 `/tmp`: 84341547008 available bytes; 95.29% used; 114156061 free inodes.

server3 `/var/tmp`: 84341547008 available bytes; 95.29% used; 114156061 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683386368 available bytes; 94.10% used; 114350898 free inodes.

server4 `/home`: 105683386368 available bytes; 94.10% used; 114350898 free inodes.

server4 `/data`: 38844391424 available bytes; 99.46% used; 224965354 free inodes.

server4 `/tmp`: 105683386368 available bytes; 94.10% used; 114350898 free inodes.

server4 `/var/tmp`: 105683386368 available bytes; 94.10% used; 114350898 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
