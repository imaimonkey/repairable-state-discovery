# V2R cluster inventory

2026-09-25T23:29:09.724843+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318675582976 available bytes; 82.22% used; 112476314 free inodes.

server1 `/home`: 318675582976 available bytes; 82.22% used; 112476314 free inodes.

server1 `/tmp`: 318675582976 available bytes; 82.22% used; 112476314 free inodes.

server1 `/var/tmp`: 318675582976 available bytes; 82.22% used; 112476314 free inodes.

server1 `/mnt/raid5`: 360119300096 available bytes; 98.35% used; 337538657 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22945828864 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22945828864 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22945828864 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22945828864 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 297335734272 available bytes; 97.95% used; 445051145 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84348133376 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84348133376 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124821229568 available bytes; 98.27% used; 225811652 free inodes.

server3 `/tmp`: 84348133376 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84348133376 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105125138432 available bytes; 94.13% used; 114346703 free inodes.

server4 `/home`: 105125138432 available bytes; 94.13% used; 114346703 free inodes.

server4 `/data`: 178226409472 available bytes; 97.54% used; 224917606 free inodes.

server4 `/tmp`: 105125138432 available bytes; 94.13% used; 114346703 free inodes.

server4 `/var/tmp`: 105125138432 available bytes; 94.13% used; 114346703 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
