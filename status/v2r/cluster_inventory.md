# V2R cluster inventory

2026-09-23T19:11:20.338143+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325754585088 available bytes; 81.83% used; 112501856 free inodes.

server1 `/home`: 325754585088 available bytes; 81.83% used; 112501856 free inodes.

server1 `/tmp`: 325754585088 available bytes; 81.83% used; 112501856 free inodes.

server1 `/var/tmp`: 325754585088 available bytes; 81.83% used; 112501856 free inodes.

server1 `/mnt/raid5`: 1389231054848 available bytes; 93.63% used; 337741405 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41337110528 available bytes; 97.69% used; 110435430 free inodes.

server2 `/home`: 41337110528 available bytes; 97.69% used; 110435430 free inodes.

server2 `/tmp`: 41337110528 available bytes; 97.69% used; 110435430 free inodes.

server2 `/var/tmp`: 41337110528 available bytes; 97.69% used; 110435430 free inodes.

server2 `/mnt/raid5`: 523076440064 available bytes; 96.39% used; 445213219 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293621874688 available bytes; 83.61% used; 114236822 free inodes.

server3 `/home`: 293621874688 available bytes; 83.61% used; 114236822 free inodes.

server3 `/data`: 52770271232 available bytes; 99.27% used; 225845854 free inodes.

server3 `/tmp`: 293621874688 available bytes; 83.61% used; 114236822 free inodes.

server3 `/var/tmp`: 293621874688 available bytes; 83.61% used; 114236822 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106475200512 available bytes; 94.06% used; 114356233 free inodes.

server4 `/home`: 106475200512 available bytes; 94.06% used; 114356233 free inodes.

server4 `/data`: 14872576 available bytes; 100.00% used; 225457656 free inodes.

server4 `/tmp`: 106475200512 available bytes; 94.06% used; 114356233 free inodes.

server4 `/var/tmp`: 106475200512 available bytes; 94.06% used; 114356233 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
