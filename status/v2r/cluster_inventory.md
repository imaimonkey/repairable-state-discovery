# V2R cluster inventory

2026-09-24T06:47:08.306607+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324486803456 available bytes; 81.90% used; 112491500 free inodes.

server1 `/home`: 324486803456 available bytes; 81.90% used; 112491500 free inodes.

server1 `/tmp`: 324486803456 available bytes; 81.90% used; 112491500 free inodes.

server1 `/var/tmp`: 324486803456 available bytes; 81.90% used; 112491500 free inodes.

server1 `/mnt/raid5`: 517469368320 available bytes; 97.63% used; 337723365 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57873580032 available bytes; 96.77% used; 110431203 free inodes.

server2 `/home`: 57873580032 available bytes; 96.77% used; 110431203 free inodes.

server2 `/tmp`: 57873580032 available bytes; 96.77% used; 110431203 free inodes.

server2 `/var/tmp`: 57873580032 available bytes; 96.77% used; 110431203 free inodes.

server2 `/mnt/raid5`: 519184457728 available bytes; 96.41% used; 445191501 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126718631936 available bytes; 92.93% used; 114172909 free inodes.

server3 `/home`: 126718631936 available bytes; 92.93% used; 114172909 free inodes.

server3 `/data`: 139323777024 available bytes; 98.07% used; 225835001 free inodes.

server3 `/tmp`: 126718631936 available bytes; 92.93% used; 114172909 free inodes.

server3 `/var/tmp`: 126718631936 available bytes; 92.93% used; 114172909 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105804574720 available bytes; 94.10% used; 114349238 free inodes.

server4 `/home`: 105804574720 available bytes; 94.10% used; 114349238 free inodes.

server4 `/data`: 313901322240 available bytes; 95.66% used; 225368411 free inodes.

server4 `/tmp`: 105804574720 available bytes; 94.10% used; 114349238 free inodes.

server4 `/var/tmp`: 105804574720 available bytes; 94.10% used; 114349238 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
