# V2R cluster inventory

2026-09-24T18:58:33.954570+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323996012544 available bytes; 81.93% used; 112481461 free inodes.

server1 `/home`: 323996012544 available bytes; 81.93% used; 112481461 free inodes.

server1 `/tmp`: 323996012544 available bytes; 81.93% used; 112481461 free inodes.

server1 `/var/tmp`: 323996012544 available bytes; 81.93% used; 112481461 free inodes.

server1 `/mnt/raid5`: 416260734976 available bytes; 98.09% used; 337636066 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54469795840 available bytes; 96.96% used; 110411933 free inodes.

server2 `/home`: 54469795840 available bytes; 96.96% used; 110411933 free inodes.

server2 `/tmp`: 54469795840 available bytes; 96.96% used; 110411933 free inodes.

server2 `/var/tmp`: 54469795840 available bytes; 96.96% used; 110411933 free inodes.

server2 `/mnt/raid5`: 495853813760 available bytes; 96.57% used; 445159767 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84407230464 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84407230464 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152556331008 available bytes; 97.89% used; 225800036 free inodes.

server3 `/tmp`: 84407230464 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84407230464 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105660997632 available bytes; 94.10% used; 114348475 free inodes.

server4 `/home`: 105660997632 available bytes; 94.10% used; 114348475 free inodes.

server4 `/data`: 89932271616 available bytes; 98.76% used; 225267371 free inodes.

server4 `/tmp`: 105660997632 available bytes; 94.10% used; 114348475 free inodes.

server4 `/var/tmp`: 105660997632 available bytes; 94.10% used; 114348475 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
