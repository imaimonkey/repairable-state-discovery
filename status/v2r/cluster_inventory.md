# V2R cluster inventory

2026-09-23T22:04:24.473726+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325708976128 available bytes; 81.83% used; 112501409 free inodes.

server1 `/home`: 325708976128 available bytes; 81.83% used; 112501409 free inodes.

server1 `/tmp`: 325708976128 available bytes; 81.83% used; 112501409 free inodes.

server1 `/var/tmp`: 325708976128 available bytes; 81.83% used; 112501409 free inodes.

server1 `/mnt/raid5`: 1388120907776 available bytes; 93.63% used; 337739890 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41104482304 available bytes; 97.71% used; 110432658 free inodes.

server2 `/home`: 41104482304 available bytes; 97.71% used; 110432658 free inodes.

server2 `/tmp`: 41104482304 available bytes; 97.71% used; 110432658 free inodes.

server2 `/var/tmp`: 41104482304 available bytes; 97.71% used; 110432658 free inodes.

server2 `/mnt/raid5`: 537447088128 available bytes; 96.29% used; 445207372 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292786393088 available bytes; 83.66% used; 114210701 free inodes.

server3 `/home`: 292786393088 available bytes; 83.66% used; 114210701 free inodes.

server3 `/data`: 82451402752 available bytes; 98.86% used; 225847787 free inodes.

server3 `/tmp`: 292786393088 available bytes; 83.66% used; 114210701 free inodes.

server3 `/var/tmp`: 292786393088 available bytes; 83.66% used; 114210701 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106440278016 available bytes; 94.06% used; 114355467 free inodes.

server4 `/home`: 106440278016 available bytes; 94.06% used; 114355467 free inodes.

server4 `/data`: 300193468416 available bytes; 95.85% used; 225444045 free inodes.

server4 `/tmp`: 106440278016 available bytes; 94.06% used; 114355467 free inodes.

server4 `/var/tmp`: 106440278016 available bytes; 94.06% used; 114355467 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
