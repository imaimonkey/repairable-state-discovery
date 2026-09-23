# V2R cluster inventory

2026-09-23T20:58:11.875551+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325724893184 available bytes; 81.83% used; 112501589 free inodes.

server1 `/home`: 325724893184 available bytes; 81.83% used; 112501589 free inodes.

server1 `/tmp`: 325724893184 available bytes; 81.83% used; 112501589 free inodes.

server1 `/var/tmp`: 325724893184 available bytes; 81.83% used; 112501589 free inodes.

server1 `/mnt/raid5`: 1388147859456 available bytes; 93.63% used; 337740017 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41125572608 available bytes; 97.71% used; 110432727 free inodes.

server2 `/home`: 41125572608 available bytes; 97.71% used; 110432727 free inodes.

server2 `/tmp`: 41125572608 available bytes; 97.71% used; 110432727 free inodes.

server2 `/var/tmp`: 41125572608 available bytes; 97.71% used; 110432727 free inodes.

server2 `/mnt/raid5`: 539502407680 available bytes; 96.27% used; 445209437 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293463592960 available bytes; 83.62% used; 114237304 free inodes.

server3 `/home`: 293463592960 available bytes; 83.62% used; 114237304 free inodes.

server3 `/data`: 52613177344 available bytes; 99.27% used; 225850502 free inodes.

server3 `/tmp`: 293463592960 available bytes; 83.62% used; 114237304 free inodes.

server3 `/var/tmp`: 293463592960 available bytes; 83.62% used; 114237304 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106501296128 available bytes; 94.06% used; 114356068 free inodes.

server4 `/home`: 106501296128 available bytes; 94.06% used; 114356068 free inodes.

server4 `/data`: 300587372544 available bytes; 95.85% used; 225457363 free inodes.

server4 `/tmp`: 106501296128 available bytes; 94.06% used; 114356068 free inodes.

server4 `/var/tmp`: 106501296128 available bytes; 94.06% used; 114356068 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
