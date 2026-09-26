# V2R cluster inventory

2026-09-26T15:02:40.562942+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318171783168 available bytes; 82.25% used; 112474002 free inodes.

server1 `/home`: 318171783168 available bytes; 82.25% used; 112474002 free inodes.

server1 `/tmp`: 318171783168 available bytes; 82.25% used; 112474002 free inodes.

server1 `/var/tmp`: 318171783168 available bytes; 82.25% used; 112474002 free inodes.

server1 `/mnt/raid5`: 654686760960 available bytes; 97.00% used; 337531867 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 42442752 available bytes; 100.00% used; 110367054 free inodes.

server2 `/home`: 42442752 available bytes; 100.00% used; 110367054 free inodes.

server2 `/tmp`: 42442752 available bytes; 100.00% used; 110367054 free inodes.

server2 `/var/tmp`: 42442752 available bytes; 100.00% used; 110367054 free inodes.

server2 `/mnt/raid5`: 622348353536 available bytes; 95.70% used; 444973496 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82737156096 available bytes; 95.38% used; 114110773 free inodes.

server3 `/home`: 82737156096 available bytes; 95.38% used; 114110773 free inodes.

server3 `/data`: 1346836729856 available bytes; 81.39% used; 225804828 free inodes.

server3 `/tmp`: 82737156096 available bytes; 95.38% used; 114110773 free inodes.

server3 `/var/tmp`: 82737156096 available bytes; 95.38% used; 114110773 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953067008 available bytes; 94.09% used; 114347839 free inodes.

server4 `/home`: 105953067008 available bytes; 94.09% used; 114347839 free inodes.

server4 `/data`: 410816999424 available bytes; 94.32% used; 224826197 free inodes.

server4 `/tmp`: 105953067008 available bytes; 94.09% used; 114347839 free inodes.

server4 `/var/tmp`: 105953067008 available bytes; 94.09% used; 114347839 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
