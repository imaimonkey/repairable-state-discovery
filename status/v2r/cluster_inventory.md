# V2R cluster inventory

2026-09-24T18:55:21.635412+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323996778496 available bytes; 81.93% used; 112481458 free inodes.

server1 `/home`: 323996778496 available bytes; 81.93% used; 112481458 free inodes.

server1 `/tmp`: 323996778496 available bytes; 81.93% used; 112481458 free inodes.

server1 `/var/tmp`: 323996778496 available bytes; 81.93% used; 112481458 free inodes.

server1 `/mnt/raid5`: 416263229440 available bytes; 98.09% used; 337636444 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 54469693440 available bytes; 96.96% used; 110411939 free inodes.

server2 `/home`: 54469693440 available bytes; 96.96% used; 110411939 free inodes.

server2 `/tmp`: 54469693440 available bytes; 96.96% used; 110411939 free inodes.

server2 `/var/tmp`: 54469693440 available bytes; 96.96% used; 110411939 free inodes.

server2 `/mnt/raid5`: 495958786048 available bytes; 96.57% used; 445159978 free inodes.
| server3 | True | ['1'] | [] |

server3 `/`: 84407808000 available bytes; 95.29% used; 114156139 free inodes.

server3 `/home`: 84407808000 available bytes; 95.29% used; 114156139 free inodes.

server3 `/data`: 152649707520 available bytes; 97.89% used; 225800100 free inodes.

server3 `/tmp`: 84407808000 available bytes; 95.29% used; 114156139 free inodes.

server3 `/var/tmp`: 84407808000 available bytes; 95.29% used; 114156139 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105661177856 available bytes; 94.10% used; 114348479 free inodes.

server4 `/home`: 105661177856 available bytes; 94.10% used; 114348479 free inodes.

server4 `/data`: 89946591232 available bytes; 98.76% used; 225267474 free inodes.

server4 `/tmp`: 105661177856 available bytes; 94.10% used; 114348479 free inodes.

server4 `/var/tmp`: 105661177856 available bytes; 94.10% used; 114348479 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
