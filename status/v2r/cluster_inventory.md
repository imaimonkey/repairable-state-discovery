# V2R cluster inventory

2026-09-23T20:56:40.142763+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325723975680 available bytes; 81.83% used; 112501591 free inodes.

server1 `/home`: 325723975680 available bytes; 81.83% used; 112501591 free inodes.

server1 `/tmp`: 325723975680 available bytes; 81.83% used; 112501591 free inodes.

server1 `/var/tmp`: 325723975680 available bytes; 81.83% used; 112501591 free inodes.

server1 `/mnt/raid5`: 1388142243840 available bytes; 93.63% used; 337740006 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41124724736 available bytes; 97.71% used; 110432725 free inodes.

server2 `/home`: 41124724736 available bytes; 97.71% used; 110432725 free inodes.

server2 `/tmp`: 41124724736 available bytes; 97.71% used; 110432725 free inodes.

server2 `/var/tmp`: 41124724736 available bytes; 97.71% used; 110432725 free inodes.

server2 `/mnt/raid5`: 518906630144 available bytes; 96.41% used; 445209508 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293468151808 available bytes; 83.62% used; 114237633 free inodes.

server3 `/home`: 293468151808 available bytes; 83.62% used; 114237633 free inodes.

server3 `/data`: 52613074944 available bytes; 99.27% used; 225850566 free inodes.

server3 `/tmp`: 293468151808 available bytes; 83.62% used; 114237633 free inodes.

server3 `/var/tmp`: 293468151808 available bytes; 83.62% used; 114237633 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106501935104 available bytes; 94.06% used; 114356071 free inodes.

server4 `/home`: 106501935104 available bytes; 94.06% used; 114356071 free inodes.

server4 `/data`: 300600299520 available bytes; 95.85% used; 225457641 free inodes.

server4 `/tmp`: 106501935104 available bytes; 94.06% used; 114356071 free inodes.

server4 `/var/tmp`: 106501935104 available bytes; 94.06% used; 114356071 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
