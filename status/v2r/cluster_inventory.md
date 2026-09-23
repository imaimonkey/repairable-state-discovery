# V2R cluster inventory

2026-09-23T19:37:17.250181+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325754839040 available bytes; 81.83% used; 112501878 free inodes.

server1 `/home`: 325754839040 available bytes; 81.83% used; 112501878 free inodes.

server1 `/tmp`: 325754839040 available bytes; 81.83% used; 112501878 free inodes.

server1 `/var/tmp`: 325754839040 available bytes; 81.83% used; 112501878 free inodes.

server1 `/mnt/raid5`: 1389182341120 available bytes; 93.63% used; 337741326 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41323642880 available bytes; 97.69% used; 110435440 free inodes.

server2 `/home`: 41323642880 available bytes; 97.69% used; 110435440 free inodes.

server2 `/tmp`: 41323642880 available bytes; 97.69% used; 110435440 free inodes.

server2 `/var/tmp`: 41323642880 available bytes; 97.69% used; 110435440 free inodes.

server2 `/mnt/raid5`: 542949470208 available bytes; 96.25% used; 445212335 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293692203008 available bytes; 83.61% used; 114247536 free inodes.

server3 `/home`: 293692203008 available bytes; 83.61% used; 114247536 free inodes.

server3 `/data`: 52737273856 available bytes; 99.27% used; 225845054 free inodes.

server3 `/tmp`: 293692203008 available bytes; 83.61% used; 114247536 free inodes.

server3 `/var/tmp`: 293692203008 available bytes; 83.61% used; 114247536 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106529746944 available bytes; 94.06% used; 114356236 free inodes.

server4 `/home`: 106529746944 available bytes; 94.06% used; 114356236 free inodes.

server4 `/data`: 3518464 available bytes; 100.00% used; 225457642 free inodes.

server4 `/tmp`: 106529746944 available bytes; 94.06% used; 114356236 free inodes.

server4 `/var/tmp`: 106529746944 available bytes; 94.06% used; 114356236 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
