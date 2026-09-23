# V2R cluster inventory

2026-09-23T20:49:01.602166+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325734866944 available bytes; 81.83% used; 112501673 free inodes.

server1 `/home`: 325734866944 available bytes; 81.83% used; 112501673 free inodes.

server1 `/tmp`: 325734866944 available bytes; 81.83% used; 112501673 free inodes.

server1 `/var/tmp`: 325734866944 available bytes; 81.83% used; 112501673 free inodes.

server1 `/mnt/raid5`: 1388166508544 available bytes; 93.63% used; 337740035 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 41130913792 available bytes; 97.71% used; 110432734 free inodes.

server2 `/home`: 41130913792 available bytes; 97.71% used; 110432734 free inodes.

server2 `/tmp`: 41130913792 available bytes; 97.71% used; 110432734 free inodes.

server2 `/var/tmp`: 41130913792 available bytes; 97.71% used; 110432734 free inodes.

server2 `/mnt/raid5`: 539788480512 available bytes; 96.27% used; 445209989 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293471944704 available bytes; 83.62% used; 114238168 free inodes.

server3 `/home`: 293471944704 available bytes; 83.62% used; 114238168 free inodes.

server3 `/data`: 52570996736 available bytes; 99.27% used; 225843002 free inodes.

server3 `/tmp`: 293471944704 available bytes; 83.62% used; 114238168 free inodes.

server3 `/var/tmp`: 293471944704 available bytes; 83.62% used; 114238168 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106513227776 available bytes; 94.06% used; 114356100 free inodes.

server4 `/home`: 106513227776 available bytes; 94.06% used; 114356100 free inodes.

server4 `/data`: 300630474752 available bytes; 95.85% used; 225459133 free inodes.

server4 `/tmp`: 106513227776 available bytes; 94.06% used; 114356100 free inodes.

server4 `/var/tmp`: 106513227776 available bytes; 94.06% used; 114356100 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
