# V2R cluster inventory

2026-09-24T00:40:13.417646+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325541605376 available bytes; 81.84% used; 112500478 free inodes.

server1 `/home`: 325541605376 available bytes; 81.84% used; 112500478 free inodes.

server1 `/tmp`: 325541605376 available bytes; 81.84% used; 112500478 free inodes.

server1 `/var/tmp`: 325541605376 available bytes; 81.84% used; 112500478 free inodes.

server1 `/mnt/raid5`: 1101635420160 available bytes; 94.95% used; 337735040 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40986021888 available bytes; 97.71% used; 110432302 free inodes.

server2 `/home`: 40986021888 available bytes; 97.71% used; 110432302 free inodes.

server2 `/tmp`: 40986021888 available bytes; 97.71% used; 110432302 free inodes.

server2 `/var/tmp`: 40986021888 available bytes; 97.71% used; 110432302 free inodes.

server2 `/mnt/raid5`: 532459905024 available bytes; 96.32% used; 445202907 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292289531904 available bytes; 83.69% used; 114187341 free inodes.

server3 `/home`: 292289531904 available bytes; 83.69% used; 114187341 free inodes.

server3 `/data`: 82234576896 available bytes; 98.86% used; 225844018 free inodes.

server3 `/tmp`: 292289531904 available bytes; 83.69% used; 114187341 free inodes.

server3 `/var/tmp`: 292289531904 available bytes; 83.69% used; 114187341 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106062786560 available bytes; 94.08% used; 114350078 free inodes.

server4 `/home`: 106062786560 available bytes; 94.08% used; 114350078 free inodes.

server4 `/data`: 292917932032 available bytes; 95.95% used; 225414582 free inodes.

server4 `/tmp`: 106062786560 available bytes; 94.08% used; 114350078 free inodes.

server4 `/var/tmp`: 106062786560 available bytes; 94.08% used; 114350078 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
