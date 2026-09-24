# V2R cluster inventory

2026-09-24T03:00:21.486451+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325374836736 available bytes; 81.85% used; 112498535 free inodes.

server1 `/home`: 325374836736 available bytes; 81.85% used; 112498535 free inodes.

server1 `/tmp`: 325374836736 available bytes; 81.85% used; 112498535 free inodes.

server1 `/var/tmp`: 325374836736 available bytes; 81.85% used; 112498535 free inodes.

server1 `/mnt/raid5`: 518386253824 available bytes; 97.62% used; 337732358 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40862781440 available bytes; 97.72% used; 110431324 free inodes.

server2 `/home`: 40862781440 available bytes; 97.72% used; 110431324 free inodes.

server2 `/tmp`: 40862781440 available bytes; 97.72% used; 110431324 free inodes.

server2 `/var/tmp`: 40862781440 available bytes; 97.72% used; 110431324 free inodes.

server2 `/mnt/raid5`: 528058757120 available bytes; 96.35% used; 445198496 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292286738432 available bytes; 83.69% used; 114186958 free inodes.

server3 `/home`: 292286738432 available bytes; 83.69% used; 114186958 free inodes.

server3 `/data`: 39708168192 available bytes; 99.45% used; 225845338 free inodes.

server3 `/tmp`: 292286738432 available bytes; 83.69% used; 114186958 free inodes.

server3 `/var/tmp`: 292286738432 available bytes; 83.69% used; 114186958 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105988395008 available bytes; 94.09% used; 114349629 free inodes.

server4 `/home`: 105988395008 available bytes; 94.09% used; 114349629 free inodes.

server4 `/data`: 289712947200 available bytes; 96.00% used; 225386861 free inodes.

server4 `/tmp`: 105988395008 available bytes; 94.09% used; 114349629 free inodes.

server4 `/var/tmp`: 105988395008 available bytes; 94.09% used; 114349629 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
