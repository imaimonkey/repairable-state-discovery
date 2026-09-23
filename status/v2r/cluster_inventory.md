# V2R cluster inventory

2026-09-23T23:58:27.274491+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325582999552 available bytes; 81.84% used; 112500934 free inodes.

server1 `/home`: 325582999552 available bytes; 81.84% used; 112500934 free inodes.

server1 `/tmp`: 325582999552 available bytes; 81.84% used; 112500934 free inodes.

server1 `/var/tmp`: 325582999552 available bytes; 81.84% used; 112500934 free inodes.

server1 `/mnt/raid5`: 1274059517952 available bytes; 94.16% used; 337735387 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41019478016 available bytes; 97.71% used; 110432452 free inodes.

server2 `/home`: 41019478016 available bytes; 97.71% used; 110432452 free inodes.

server2 `/tmp`: 41019478016 available bytes; 97.71% used; 110432452 free inodes.

server2 `/var/tmp`: 41019478016 available bytes; 97.71% used; 110432452 free inodes.

server2 `/mnt/raid5`: 533594095616 available bytes; 96.31% used; 445204448 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292802056192 available bytes; 83.66% used; 114211668 free inodes.

server3 `/home`: 292802056192 available bytes; 83.66% used; 114211668 free inodes.

server3 `/data`: 82274508800 available bytes; 98.86% used; 225844871 free inodes.

server3 `/tmp`: 292802056192 available bytes; 83.66% used; 114211668 free inodes.

server3 `/var/tmp`: 292802056192 available bytes; 83.66% used; 114211668 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106142167040 available bytes; 94.08% used; 114351337 free inodes.

server4 `/home`: 106142167040 available bytes; 94.08% used; 114351337 free inodes.

server4 `/data`: 292943347712 available bytes; 95.95% used; 225415656 free inodes.

server4 `/tmp`: 106142167040 available bytes; 94.08% used; 114351337 free inodes.

server4 `/var/tmp`: 106142167040 available bytes; 94.08% used; 114351337 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
