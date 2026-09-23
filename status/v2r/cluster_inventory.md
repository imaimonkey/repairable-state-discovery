# V2R cluster inventory

2026-09-23T19:12:51.913804+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325754003456 available bytes; 81.83% used; 112501851 free inodes.

server1 `/home`: 325754003456 available bytes; 81.83% used; 112501851 free inodes.

server1 `/tmp`: 325754003456 available bytes; 81.83% used; 112501851 free inodes.

server1 `/var/tmp`: 325754003456 available bytes; 81.83% used; 112501851 free inodes.

server1 `/mnt/raid5`: 1389234352128 available bytes; 93.63% used; 337741404 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41337257984 available bytes; 97.69% used; 110435426 free inodes.

server2 `/home`: 41337257984 available bytes; 97.69% used; 110435426 free inodes.

server2 `/tmp`: 41337257984 available bytes; 97.69% used; 110435426 free inodes.

server2 `/var/tmp`: 41337257984 available bytes; 97.69% used; 110435426 free inodes.

server2 `/mnt/raid5`: 543665647616 available bytes; 96.24% used; 445213076 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293622407168 available bytes; 83.61% used; 114236822 free inodes.

server3 `/home`: 293622407168 available bytes; 83.61% used; 114236822 free inodes.

server3 `/data`: 52765908992 available bytes; 99.27% used; 225845834 free inodes.

server3 `/tmp`: 293622407168 available bytes; 83.61% used; 114236822 free inodes.

server3 `/var/tmp`: 293622407168 available bytes; 83.61% used; 114236822 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106475159552 available bytes; 94.06% used; 114356233 free inodes.

server4 `/home`: 106475159552 available bytes; 94.06% used; 114356233 free inodes.

server4 `/data`: 11771904 available bytes; 100.00% used; 225457652 free inodes.

server4 `/tmp`: 106475159552 available bytes; 94.06% used; 114356233 free inodes.

server4 `/var/tmp`: 106475159552 available bytes; 94.06% used; 114356233 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
