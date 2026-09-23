# V2R cluster inventory

2026-09-23T21:05:50.765606+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325721939968 available bytes; 81.83% used; 112501610 free inodes.

server1 `/home`: 325721939968 available bytes; 81.83% used; 112501610 free inodes.

server1 `/tmp`: 325721939968 available bytes; 81.83% used; 112501610 free inodes.

server1 `/var/tmp`: 325721939968 available bytes; 81.83% used; 112501610 free inodes.

server1 `/mnt/raid5`: 1388135223296 available bytes; 93.63% used; 337739985 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41121669120 available bytes; 97.71% used; 110432711 free inodes.

server2 `/home`: 41121669120 available bytes; 97.71% used; 110432711 free inodes.

server2 `/tmp`: 41121669120 available bytes; 97.71% used; 110432711 free inodes.

server2 `/var/tmp`: 41121669120 available bytes; 97.71% used; 110432711 free inodes.

server2 `/mnt/raid5`: 539266338816 available bytes; 96.27% used; 445209720 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293464068096 available bytes; 83.62% used; 114236959 free inodes.

server3 `/home`: 293464068096 available bytes; 83.62% used; 114236959 free inodes.

server3 `/data`: 52322398208 available bytes; 99.28% used; 225849662 free inodes.

server3 `/tmp`: 293464068096 available bytes; 83.62% used; 114236959 free inodes.

server3 `/var/tmp`: 293464068096 available bytes; 83.62% used; 114236959 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106496417792 available bytes; 94.06% used; 114356052 free inodes.

server4 `/home`: 106496417792 available bytes; 94.06% used; 114356052 free inodes.

server4 `/data`: 300526088192 available bytes; 95.85% used; 225455861 free inodes.

server4 `/tmp`: 106496417792 available bytes; 94.06% used; 114356052 free inodes.

server4 `/var/tmp`: 106496417792 available bytes; 94.06% used; 114356052 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
