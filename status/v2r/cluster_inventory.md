# V2R cluster inventory

2026-09-24T13:37:23.386927+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324029894656 available bytes; 81.92% used; 112481515 free inodes.

server1 `/home`: 324029894656 available bytes; 81.92% used; 112481515 free inodes.

server1 `/tmp`: 324029894656 available bytes; 81.92% used; 112481515 free inodes.

server1 `/var/tmp`: 324029894656 available bytes; 81.92% used; 112481515 free inodes.

server1 `/mnt/raid5`: 417013485568 available bytes; 98.09% used; 337674355 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57518149632 available bytes; 96.79% used; 110428651 free inodes.

server2 `/home`: 57518149632 available bytes; 96.79% used; 110428651 free inodes.

server2 `/tmp`: 57518149632 available bytes; 96.79% used; 110428651 free inodes.

server2 `/var/tmp`: 57518149632 available bytes; 96.79% used; 110428651 free inodes.

server2 `/mnt/raid5`: 506415042560 available bytes; 96.50% used; 445169709 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84704325632 available bytes; 95.27% used; 114165420 free inodes.

server3 `/home`: 84704325632 available bytes; 95.27% used; 114165420 free inodes.

server3 `/data`: 161211146240 available bytes; 97.77% used; 225803036 free inodes.

server3 `/tmp`: 84704325632 available bytes; 95.27% used; 114165420 free inodes.

server3 `/var/tmp`: 84704325632 available bytes; 95.27% used; 114165420 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761083392 available bytes; 94.10% used; 114348737 free inodes.

server4 `/home`: 105761083392 available bytes; 94.10% used; 114348737 free inodes.

server4 `/data`: 90038841344 available bytes; 98.76% used; 225257176 free inodes.

server4 `/tmp`: 105761083392 available bytes; 94.10% used; 114348737 free inodes.

server4 `/var/tmp`: 105761083392 available bytes; 94.10% used; 114348737 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
