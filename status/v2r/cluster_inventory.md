# V2R cluster inventory

2026-09-25T00:05:41.886127+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319088713728 available bytes; 82.20% used; 112480781 free inodes.

server1 `/home`: 319088713728 available bytes; 82.20% used; 112480781 free inodes.

server1 `/tmp`: 319088713728 available bytes; 82.20% used; 112480781 free inodes.

server1 `/var/tmp`: 319088713728 available bytes; 82.20% used; 112480781 free inodes.

server1 `/mnt/raid5`: 416902598656 available bytes; 98.09% used; 337622718 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23094620160 available bytes; 98.71% used; 110410784 free inodes.

server2 `/home`: 23094620160 available bytes; 98.71% used; 110410784 free inodes.

server2 `/tmp`: 23094620160 available bytes; 98.71% used; 110410784 free inodes.

server2 `/var/tmp`: 23094620160 available bytes; 98.71% used; 110410784 free inodes.

server2 `/mnt/raid5`: 487251410944 available bytes; 96.63% used; 445163868 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 84354019328 available bytes; 95.29% used; 114156100 free inodes.

server3 `/home`: 84354019328 available bytes; 95.29% used; 114156100 free inodes.

server3 `/data`: 149309546496 available bytes; 97.94% used; 225813906 free inodes.

server3 `/tmp`: 84354019328 available bytes; 95.29% used; 114156100 free inodes.

server3 `/var/tmp`: 84354019328 available bytes; 95.29% used; 114156100 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105798201344 available bytes; 94.10% used; 114348299 free inodes.

server4 `/home`: 105798201344 available bytes; 94.10% used; 114348299 free inodes.

server4 `/data`: 59349454848 available bytes; 99.18% used; 225093925 free inodes.

server4 `/tmp`: 105798201344 available bytes; 94.10% used; 114348299 free inodes.

server4 `/var/tmp`: 105798201344 available bytes; 94.10% used; 114348299 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
