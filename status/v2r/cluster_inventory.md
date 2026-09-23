# V2R cluster inventory

2026-09-23T23:22:57.065741+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325662339072 available bytes; 81.83% used; 112501609 free inodes.

server1 `/home`: 325662339072 available bytes; 81.83% used; 112501609 free inodes.

server1 `/tmp`: 325662339072 available bytes; 81.83% used; 112501609 free inodes.

server1 `/var/tmp`: 325662339072 available bytes; 81.83% used; 112501609 free inodes.

server1 `/mnt/raid5`: 1374014459904 available bytes; 93.70% used; 337739862 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41047330816 available bytes; 97.71% used; 110432602 free inodes.

server2 `/home`: 41047330816 available bytes; 97.71% used; 110432602 free inodes.

server2 `/tmp`: 41047330816 available bytes; 97.71% used; 110432602 free inodes.

server2 `/var/tmp`: 41047330816 available bytes; 97.71% used; 110432602 free inodes.

server2 `/mnt/raid5`: 534715158528 available bytes; 96.31% used; 445205705 free inodes.
| server3 | True | ['1', '3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292856811520 available bytes; 83.66% used; 114208539 free inodes.

server3 `/home`: 292856811520 available bytes; 83.66% used; 114208539 free inodes.

server3 `/data`: 82318209024 available bytes; 98.86% used; 225845910 free inodes.

server3 `/tmp`: 292856811520 available bytes; 83.66% used; 114208539 free inodes.

server3 `/var/tmp`: 292856811520 available bytes; 83.66% used; 114208539 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106245439488 available bytes; 94.07% used; 114352614 free inodes.

server4 `/home`: 106245439488 available bytes; 94.07% used; 114352614 free inodes.

server4 `/data`: 293295251456 available bytes; 95.95% used; 225426030 free inodes.

server4 `/tmp`: 106245439488 available bytes; 94.07% used; 114352614 free inodes.

server4 `/var/tmp`: 106245439488 available bytes; 94.07% used; 114352614 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
