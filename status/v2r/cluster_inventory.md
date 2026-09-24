# V2R cluster inventory

2026-09-24T23:47:07.702649+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319018082304 available bytes; 82.20% used; 112480777 free inodes.

server1 `/home`: 319018082304 available bytes; 82.20% used; 112480777 free inodes.

server1 `/tmp`: 319018082304 available bytes; 82.20% used; 112480777 free inodes.

server1 `/var/tmp`: 319018082304 available bytes; 82.20% used; 112480777 free inodes.

server1 `/mnt/raid5`: 415192137728 available bytes; 98.10% used; 337611228 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23102337024 available bytes; 98.71% used; 110410796 free inodes.

server2 `/home`: 23102337024 available bytes; 98.71% used; 110410796 free inodes.

server2 `/tmp`: 23102337024 available bytes; 98.71% used; 110410796 free inodes.

server2 `/var/tmp`: 23102337024 available bytes; 98.71% used; 110410796 free inodes.

server2 `/mnt/raid5`: 485951582208 available bytes; 96.64% used; 445150788 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84365541376 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84365541376 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 147917942784 available bytes; 97.96% used; 225800603 free inodes.

server3 `/tmp`: 84365541376 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84365541376 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799102464 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799102464 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 60971950080 available bytes; 99.16% used; 225122399 free inodes.

server4 `/tmp`: 105799102464 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799102464 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
