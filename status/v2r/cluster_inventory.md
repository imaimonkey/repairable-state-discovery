# V2R cluster inventory

2026-09-25T04:59:49.779718+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318904750080 available bytes; 82.21% used; 112480373 free inodes.

server1 `/home`: 318904750080 available bytes; 82.21% used; 112480373 free inodes.

server1 `/tmp`: 318904750080 available bytes; 82.21% used; 112480373 free inodes.

server1 `/var/tmp`: 318904750080 available bytes; 82.21% used; 112480373 free inodes.

server1 `/mnt/raid5`: 408633769984 available bytes; 98.13% used; 337572121 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939066368 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22939066368 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22939066368 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22939066368 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 462114734080 available bytes; 96.81% used; 445108757 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339748864 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84339748864 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 142970884096 available bytes; 98.02% used; 225815563 free inodes.

server3 `/tmp`: 84339748864 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84339748864 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105659396096 available bytes; 94.10% used; 114350405 free inodes.

server4 `/home`: 105659396096 available bytes; 94.10% used; 114350405 free inodes.

server4 `/data`: 27942072320 available bytes; 99.61% used; 224961203 free inodes.

server4 `/tmp`: 105659396096 available bytes; 94.10% used; 114350405 free inodes.

server4 `/var/tmp`: 105659396096 available bytes; 94.10% used; 114350405 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
