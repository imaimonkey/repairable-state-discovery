# V2R cluster inventory

2026-09-23T20:30:41.983396+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325734977536 available bytes; 81.83% used; 112501748 free inodes.

server1 `/home`: 325734977536 available bytes; 81.83% used; 112501748 free inodes.

server1 `/tmp`: 325734977536 available bytes; 81.83% used; 112501748 free inodes.

server1 `/var/tmp`: 325734977536 available bytes; 81.83% used; 112501748 free inodes.

server1 `/mnt/raid5`: 1388268552192 available bytes; 93.63% used; 337740943 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 41140633600 available bytes; 97.70% used; 110432801 free inodes.

server2 `/home`: 41140633600 available bytes; 97.70% used; 110432801 free inodes.

server2 `/tmp`: 41140633600 available bytes; 97.70% used; 110432801 free inodes.

server2 `/var/tmp`: 41140633600 available bytes; 97.70% used; 110432801 free inodes.

server2 `/mnt/raid5`: 540346834944 available bytes; 96.27% used; 445210701 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292916121600 available bytes; 83.65% used; 114207425 free inodes.

server3 `/home`: 292916121600 available bytes; 83.65% used; 114207425 free inodes.

server3 `/data`: 52588879872 available bytes; 99.27% used; 225843353 free inodes.

server3 `/tmp`: 292916121600 available bytes; 83.65% used; 114207425 free inodes.

server3 `/var/tmp`: 292916121600 available bytes; 83.65% used; 114207425 free inodes.
| server4 | True | ['1', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106527199232 available bytes; 94.06% used; 114356161 free inodes.

server4 `/home`: 106527199232 available bytes; 94.06% used; 114356161 free inodes.

server4 `/data`: 1912832 available bytes; 100.00% used; 225457595 free inodes.

server4 `/tmp`: 106527199232 available bytes; 94.06% used; 114356161 free inodes.

server4 `/var/tmp`: 106527199232 available bytes; 94.06% used; 114356161 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
