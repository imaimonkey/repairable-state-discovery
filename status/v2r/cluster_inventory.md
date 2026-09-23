# V2R cluster inventory

2026-09-23T19:38:48.800099+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325751484416 available bytes; 81.83% used; 112501832 free inodes.

server1 `/home`: 325751484416 available bytes; 81.83% used; 112501832 free inodes.

server1 `/tmp`: 325751484416 available bytes; 81.83% used; 112501832 free inodes.

server1 `/var/tmp`: 325751484416 available bytes; 81.83% used; 112501832 free inodes.

server1 `/mnt/raid5`: 1389179359232 available bytes; 93.63% used; 337741320 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41323184128 available bytes; 97.69% used; 110435430 free inodes.

server2 `/home`: 41323184128 available bytes; 97.69% used; 110435430 free inodes.

server2 `/tmp`: 41323184128 available bytes; 97.69% used; 110435430 free inodes.

server2 `/var/tmp`: 41323184128 available bytes; 97.69% used; 110435430 free inodes.

server2 `/mnt/raid5`: 542907158528 available bytes; 96.25% used; 445212184 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293683126272 available bytes; 83.61% used; 114247498 free inodes.

server3 `/home`: 293683126272 available bytes; 83.61% used; 114247498 free inodes.

server3 `/data`: 52733640704 available bytes; 99.27% used; 225845016 free inodes.

server3 `/tmp`: 293683126272 available bytes; 83.61% used; 114247498 free inodes.

server3 `/var/tmp`: 293683126272 available bytes; 83.61% used; 114247498 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106529718272 available bytes; 94.06% used; 114356236 free inodes.

server4 `/home`: 106529718272 available bytes; 94.06% used; 114356236 free inodes.

server4 `/data`: 2883584 available bytes; 100.00% used; 225457644 free inodes.

server4 `/tmp`: 106529718272 available bytes; 94.06% used; 114356236 free inodes.

server4 `/var/tmp`: 106529718272 available bytes; 94.06% used; 114356236 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
