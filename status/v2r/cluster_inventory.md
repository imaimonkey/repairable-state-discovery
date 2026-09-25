# V2R cluster inventory

2026-09-25T00:24:08.033465+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319087624192 available bytes; 82.20% used; 112480779 free inodes.

server1 `/home`: 319087624192 available bytes; 82.20% used; 112480779 free inodes.

server1 `/tmp`: 319087624192 available bytes; 82.20% used; 112480779 free inodes.

server1 `/var/tmp`: 319087624192 available bytes; 82.20% used; 112480779 free inodes.

server1 `/mnt/raid5`: 416863174656 available bytes; 98.09% used; 337620564 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23081521152 available bytes; 98.71% used; 110410769 free inodes.

server2 `/home`: 23081521152 available bytes; 98.71% used; 110410769 free inodes.

server2 `/tmp`: 23081521152 available bytes; 98.71% used; 110410769 free inodes.

server2 `/var/tmp`: 23081521152 available bytes; 98.71% used; 110410769 free inodes.

server2 `/mnt/raid5`: 502009094144 available bytes; 96.53% used; 445163037 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351037440 available bytes; 95.29% used; 114156082 free inodes.

server3 `/home`: 84351037440 available bytes; 95.29% used; 114156082 free inodes.

server3 `/data`: 148988411904 available bytes; 97.94% used; 225813537 free inodes.

server3 `/tmp`: 84351037440 available bytes; 95.29% used; 114156082 free inodes.

server3 `/var/tmp`: 84351037440 available bytes; 95.29% used; 114156082 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105789112320 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105789112320 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56733872128 available bytes; 99.22% used; 225065962 free inodes.

server4 `/tmp`: 105789112320 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105789112320 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
