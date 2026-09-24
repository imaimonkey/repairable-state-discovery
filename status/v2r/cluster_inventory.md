# V2R cluster inventory

2026-09-24T08:06:32.275929+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324411826176 available bytes; 81.90% used; 112490708 free inodes.

server1 `/home`: 324411826176 available bytes; 81.90% used; 112490708 free inodes.

server1 `/tmp`: 324411826176 available bytes; 81.90% used; 112490708 free inodes.

server1 `/var/tmp`: 324411826176 available bytes; 81.90% used; 112490708 free inodes.

server1 `/mnt/raid5`: 502072852480 available bytes; 97.70% used; 337721502 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57820422144 available bytes; 96.77% used; 110431062 free inodes.

server2 `/home`: 57820422144 available bytes; 96.77% used; 110431062 free inodes.

server2 `/tmp`: 57820422144 available bytes; 96.77% used; 110431062 free inodes.

server2 `/var/tmp`: 57820422144 available bytes; 96.77% used; 110431062 free inodes.

server2 `/mnt/raid5`: 517152825344 available bytes; 96.43% used; 445180360 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 85482987520 available bytes; 95.23% used; 114175187 free inodes.

server3 `/home`: 85482987520 available bytes; 95.23% used; 114175187 free inodes.

server3 `/data`: 177675300864 available bytes; 97.54% used; 225837145 free inodes.

server3 `/tmp`: 85482987520 available bytes; 95.23% used; 114175187 free inodes.

server3 `/var/tmp`: 85482987520 available bytes; 95.23% used; 114175187 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105778921472 available bytes; 94.10% used; 114349156 free inodes.

server4 `/home`: 105778921472 available bytes; 94.10% used; 114349156 free inodes.

server4 `/data`: 284226592768 available bytes; 96.07% used; 225365941 free inodes.

server4 `/tmp`: 105778921472 available bytes; 94.10% used; 114349156 free inodes.

server4 `/var/tmp`: 105778921472 available bytes; 94.10% used; 114349156 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
