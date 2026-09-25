# V2R cluster inventory

2026-09-25T17:43:40.573383+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318669635584 available bytes; 82.22% used; 112476348 free inodes.

server1 `/home`: 318669635584 available bytes; 82.22% used; 112476348 free inodes.

server1 `/tmp`: 318669635584 available bytes; 82.22% used; 112476348 free inodes.

server1 `/var/tmp`: 318669635584 available bytes; 82.22% used; 112476348 free inodes.

server1 `/mnt/raid5`: 371252998144 available bytes; 98.30% used; 337542872 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23097016320 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23097016320 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23097016320 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23097016320 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 315619983360 available bytes; 97.82% used; 445067513 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84391124992 available bytes; 95.29% used; 114152617 free inodes.

server3 `/home`: 84391124992 available bytes; 95.29% used; 114152617 free inodes.

server3 `/data`: 132537647104 available bytes; 98.17% used; 225810905 free inodes.

server3 `/tmp`: 84391124992 available bytes; 95.29% used; 114152617 free inodes.

server3 `/var/tmp`: 84391124992 available bytes; 95.29% used; 114152617 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105617190912 available bytes; 94.11% used; 114349623 free inodes.

server4 `/home`: 105617190912 available bytes; 94.11% used; 114349623 free inodes.

server4 `/data`: 229797875712 available bytes; 96.82% used; 224932668 free inodes.

server4 `/tmp`: 105617190912 available bytes; 94.11% used; 114349623 free inodes.

server4 `/var/tmp`: 105617190912 available bytes; 94.11% used; 114349623 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
