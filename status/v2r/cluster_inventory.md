# V2R cluster inventory

2026-09-25T22:06:37.658271+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318694662144 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318694662144 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318694662144 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318694662144 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 360296902656 available bytes; 98.35% used; 337539061 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22904864768 available bytes; 98.72% used; 110405688 free inodes.

server2 `/home`: 22904864768 available bytes; 98.72% used; 110405688 free inodes.

server2 `/tmp`: 22904864768 available bytes; 98.72% used; 110405688 free inodes.

server2 `/var/tmp`: 22904864768 available bytes; 98.72% used; 110405688 free inodes.

server2 `/mnt/raid5`: 300093616128 available bytes; 97.93% used; 445053924 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84359987200 available bytes; 95.29% used; 114152632 free inodes.

server3 `/home`: 84359987200 available bytes; 95.29% used; 114152632 free inodes.

server3 `/data`: 125877493760 available bytes; 98.26% used; 225806358 free inodes.

server3 `/tmp`: 84359987200 available bytes; 95.29% used; 114152632 free inodes.

server3 `/var/tmp`: 84359987200 available bytes; 95.29% used; 114152632 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105312342016 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105312342016 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208748584960 available bytes; 97.12% used; 224919050 free inodes.

server4 `/tmp`: 105312342016 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105312342016 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
