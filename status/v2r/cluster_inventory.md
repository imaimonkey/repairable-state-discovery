# V2R cluster inventory

2026-09-24T19:24:45.049750+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323996090368 available bytes; 81.93% used; 112481467 free inodes.

server1 `/home`: 323996090368 available bytes; 81.93% used; 112481467 free inodes.

server1 `/tmp`: 323996090368 available bytes; 81.93% used; 112481467 free inodes.

server1 `/var/tmp`: 323996090368 available bytes; 81.93% used; 112481467 free inodes.

server1 `/mnt/raid5`: 415623380992 available bytes; 98.09% used; 337632982 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54460186624 available bytes; 96.96% used; 110411899 free inodes.

server2 `/home`: 54460186624 available bytes; 96.96% used; 110411899 free inodes.

server2 `/tmp`: 54460186624 available bytes; 96.96% used; 110411899 free inodes.

server2 `/var/tmp`: 54460186624 available bytes; 96.96% used; 110411899 free inodes.

server2 `/mnt/raid5`: 474388295680 available bytes; 96.72% used; 445158683 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84405960704 available bytes; 95.29% used; 114156135 free inodes.

server3 `/home`: 84405960704 available bytes; 95.29% used; 114156135 free inodes.

server3 `/data`: 152318414848 available bytes; 97.89% used; 225799572 free inodes.

server3 `/tmp`: 84405960704 available bytes; 95.29% used; 114156135 free inodes.

server3 `/var/tmp`: 84405960704 available bytes; 95.29% used; 114156135 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105660088320 available bytes; 94.10% used; 114348463 free inodes.

server4 `/home`: 105660088320 available bytes; 94.10% used; 114348463 free inodes.

server4 `/data`: 89885102080 available bytes; 98.76% used; 225266957 free inodes.

server4 `/tmp`: 105660088320 available bytes; 94.10% used; 114348463 free inodes.

server4 `/var/tmp`: 105660088320 available bytes; 94.10% used; 114348463 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
