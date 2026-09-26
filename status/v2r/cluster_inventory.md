# V2R cluster inventory

2026-09-26T05:12:56.754304+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318397644800 available bytes; 82.24% used; 112476280 free inodes.

server1 `/home`: 318397644800 available bytes; 82.24% used; 112476280 free inodes.

server1 `/tmp`: 318397644800 available bytes; 82.24% used; 112476280 free inodes.

server1 `/var/tmp`: 318397644800 available bytes; 82.24% used; 112476280 free inodes.

server1 `/mnt/raid5`: 314672041984 available bytes; 98.56% used; 337543228 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22927867904 available bytes; 98.72% used; 110406200 free inodes.

server2 `/home`: 22927867904 available bytes; 98.72% used; 110406200 free inodes.

server2 `/tmp`: 22927867904 available bytes; 98.72% used; 110406200 free inodes.

server2 `/var/tmp`: 22927867904 available bytes; 98.72% used; 110406200 free inodes.

server2 `/mnt/raid5`: 263522975744 available bytes; 98.18% used; 445049115 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84081098752 available bytes; 95.31% used; 114165620 free inodes.

server3 `/home`: 84081098752 available bytes; 95.31% used; 114165620 free inodes.

server3 `/data`: 124565184512 available bytes; 98.28% used; 225825206 free inodes.

server3 `/tmp`: 84081098752 available bytes; 95.31% used; 114165620 free inodes.

server3 `/var/tmp`: 84081098752 available bytes; 95.31% used; 114165620 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106095435776 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106095435776 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 106993303552 available bytes; 98.52% used; 224929207 free inodes.

server4 `/tmp`: 106095435776 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106095435776 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
