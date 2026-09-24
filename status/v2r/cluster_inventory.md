# V2R cluster inventory

2026-09-24T19:26:17.379859+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323995652096 available bytes; 81.93% used; 112481465 free inodes.

server1 `/home`: 323995652096 available bytes; 81.93% used; 112481465 free inodes.

server1 `/tmp`: 323995652096 available bytes; 81.93% used; 112481465 free inodes.

server1 `/var/tmp`: 323995652096 available bytes; 81.93% used; 112481465 free inodes.

server1 `/mnt/raid5`: 415620902912 available bytes; 98.09% used; 337632812 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54453911552 available bytes; 96.96% used; 110411894 free inodes.

server2 `/home`: 54453911552 available bytes; 96.96% used; 110411894 free inodes.

server2 `/tmp`: 54453911552 available bytes; 96.96% used; 110411894 free inodes.

server2 `/var/tmp`: 54453911552 available bytes; 96.96% used; 110411894 free inodes.

server2 `/mnt/raid5`: 495004184576 available bytes; 96.58% used; 445159078 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84405944320 available bytes; 95.29% used; 114156135 free inodes.

server3 `/home`: 84405944320 available bytes; 95.29% used; 114156135 free inodes.

server3 `/data`: 152300003328 available bytes; 97.90% used; 225799549 free inodes.

server3 `/tmp`: 84405944320 available bytes; 95.29% used; 114156135 free inodes.

server3 `/var/tmp`: 84405944320 available bytes; 95.29% used; 114156135 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105659932672 available bytes; 94.10% used; 114348452 free inodes.

server4 `/home`: 105659932672 available bytes; 94.10% used; 114348452 free inodes.

server4 `/data`: 89885769728 available bytes; 98.76% used; 225266959 free inodes.

server4 `/tmp`: 105659932672 available bytes; 94.10% used; 114348452 free inodes.

server4 `/var/tmp`: 105659932672 available bytes; 94.10% used; 114348452 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
