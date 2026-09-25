# V2R cluster inventory

2026-09-25T08:33:44.109818+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318825172992 available bytes; 82.21% used; 112480369 free inodes.

server1 `/home`: 318825172992 available bytes; 82.21% used; 112480369 free inodes.

server1 `/tmp`: 318825172992 available bytes; 82.21% used; 112480369 free inodes.

server1 `/var/tmp`: 318825172992 available bytes; 82.21% used; 112480369 free inodes.

server1 `/mnt/raid5`: 364222443520 available bytes; 98.33% used; 337557081 free inodes.
| server2 | True | ['5', '6'] | [] |

server2 `/`: 22842527744 available bytes; 98.73% used; 110410490 free inodes.

server2 `/home`: 22842527744 available bytes; 98.73% used; 110410490 free inodes.

server2 `/tmp`: 22842527744 available bytes; 98.73% used; 110410490 free inodes.

server2 `/var/tmp`: 22842527744 available bytes; 98.73% used; 110410490 free inodes.

server2 `/mnt/raid5`: 333131894784 available bytes; 97.70% used; 445094189 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436353024 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84436353024 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142383783936 available bytes; 98.03% used; 225811612 free inodes.

server3 `/tmp`: 84436353024 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84436353024 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | ['0', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105634013184 available bytes; 94.11% used; 114350319 free inodes.

server4 `/home`: 105634013184 available bytes; 94.11% used; 114350319 free inodes.

server4 `/data`: 245041479680 available bytes; 96.61% used; 225003645 free inodes.

server4 `/tmp`: 105634013184 available bytes; 94.11% used; 114350319 free inodes.

server4 `/var/tmp`: 105634013184 available bytes; 94.11% used; 114350319 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
