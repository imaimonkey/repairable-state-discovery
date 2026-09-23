# V2R cluster inventory

2026-09-23T20:41:23.457481+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325736194048 available bytes; 81.83% used; 112501751 free inodes.

server1 `/home`: 325736194048 available bytes; 81.83% used; 112501751 free inodes.

server1 `/tmp`: 325736194048 available bytes; 81.83% used; 112501751 free inodes.

server1 `/var/tmp`: 325736194048 available bytes; 81.83% used; 112501751 free inodes.

server1 `/mnt/raid5`: 1388251623424 available bytes; 93.63% used; 337740888 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 41134403584 available bytes; 97.71% used; 110432778 free inodes.

server2 `/home`: 41134403584 available bytes; 97.71% used; 110432778 free inodes.

server2 `/tmp`: 41134403584 available bytes; 97.71% used; 110432778 free inodes.

server2 `/var/tmp`: 41134403584 available bytes; 97.71% used; 110432778 free inodes.

server2 `/mnt/raid5`: 540023427072 available bytes; 96.27% used; 445210210 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293130440704 available bytes; 83.64% used; 114216735 free inodes.

server3 `/home`: 293130440704 available bytes; 83.64% used; 114216735 free inodes.

server3 `/data`: 52578242560 available bytes; 99.27% used; 225843145 free inodes.

server3 `/tmp`: 293130440704 available bytes; 83.64% used; 114216735 free inodes.

server3 `/var/tmp`: 293130440704 available bytes; 83.64% used; 114216735 free inodes.
| server4 | True | ['1', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106523901952 available bytes; 94.06% used; 114356128 free inodes.

server4 `/home`: 106523901952 available bytes; 94.06% used; 114356128 free inodes.

server4 `/data`: 300689039360 available bytes; 95.84% used; 225460743 free inodes.

server4 `/tmp`: 106523901952 available bytes; 94.06% used; 114356128 free inodes.

server4 `/var/tmp`: 106523901952 available bytes; 94.06% used; 114356128 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
