# V2R cluster inventory

2026-09-23T19:23:33.026830+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325753630720 available bytes; 81.83% used; 112501868 free inodes.

server1 `/home`: 325753630720 available bytes; 81.83% used; 112501868 free inodes.

server1 `/tmp`: 325753630720 available bytes; 81.83% used; 112501868 free inodes.

server1 `/var/tmp`: 325753630720 available bytes; 81.83% used; 112501868 free inodes.

server1 `/mnt/raid5`: 1389206585344 available bytes; 93.63% used; 337741370 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41329479680 available bytes; 97.69% used; 110435434 free inodes.

server2 `/home`: 41329479680 available bytes; 97.69% used; 110435434 free inodes.

server2 `/tmp`: 41329479680 available bytes; 97.69% used; 110435434 free inodes.

server2 `/var/tmp`: 41329479680 available bytes; 97.69% used; 110435434 free inodes.

server2 `/mnt/raid5`: 543360786432 available bytes; 96.25% used; 445212607 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293896396800 available bytes; 83.60% used; 114253311 free inodes.

server3 `/home`: 293896396800 available bytes; 83.60% used; 114253311 free inodes.

server3 `/data`: 52755791872 available bytes; 99.27% used; 225845641 free inodes.

server3 `/tmp`: 293896396800 available bytes; 83.60% used; 114253311 free inodes.

server3 `/var/tmp`: 293896396800 available bytes; 83.60% used; 114253311 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106529828864 available bytes; 94.06% used; 114356235 free inodes.

server4 `/home`: 106529828864 available bytes; 94.06% used; 114356235 free inodes.

server4 `/data`: 6316032 available bytes; 100.00% used; 225457647 free inodes.

server4 `/tmp`: 106529828864 available bytes; 94.06% used; 114356235 free inodes.

server4 `/var/tmp`: 106529828864 available bytes; 94.06% used; 114356235 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
