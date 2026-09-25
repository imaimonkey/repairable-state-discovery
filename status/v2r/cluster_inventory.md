# V2R cluster inventory

2026-09-25T16:13:26.718157+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672228352 available bytes; 82.22% used; 112476330 free inodes.

server1 `/home`: 318672228352 available bytes; 82.22% used; 112476330 free inodes.

server1 `/tmp`: 318672228352 available bytes; 82.22% used; 112476330 free inodes.

server1 `/var/tmp`: 318672228352 available bytes; 82.22% used; 112476330 free inodes.

server1 `/mnt/raid5`: 363906543616 available bytes; 98.33% used; 337545026 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23109545984 available bytes; 98.71% used; 110407942 free inodes.

server2 `/home`: 23109545984 available bytes; 98.71% used; 110407942 free inodes.

server2 `/tmp`: 23109545984 available bytes; 98.71% used; 110407942 free inodes.

server2 `/var/tmp`: 23109545984 available bytes; 98.71% used; 110407942 free inodes.

server2 `/mnt/raid5`: 318847410176 available bytes; 97.80% used; 445071233 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84402393088 available bytes; 95.29% used; 114152676 free inodes.

server3 `/home`: 84402393088 available bytes; 95.29% used; 114152676 free inodes.

server3 `/data`: 134932013056 available bytes; 98.14% used; 225806221 free inodes.

server3 `/tmp`: 84402393088 available bytes; 95.29% used; 114152676 free inodes.

server3 `/var/tmp`: 84402393088 available bytes; 95.29% used; 114152676 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636585472 available bytes; 94.11% used; 114349647 free inodes.

server4 `/home`: 105636585472 available bytes; 94.11% used; 114349647 free inodes.

server4 `/data`: 230249865216 available bytes; 96.82% used; 224934566 free inodes.

server4 `/tmp`: 105636585472 available bytes; 94.11% used; 114349647 free inodes.

server4 `/var/tmp`: 105636585472 available bytes; 94.11% used; 114349647 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
