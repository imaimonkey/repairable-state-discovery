# V2R cluster inventory

2026-09-26T01:34:25.666273+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318650380288 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318650380288 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318650380288 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318650380288 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 345490272256 available bytes; 98.42% used; 337546525 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938939392 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22938939392 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22938939392 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22938939392 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 290586918912 available bytes; 97.99% used; 445055869 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84334555136 available bytes; 95.29% used; 114152364 free inodes.

server3 `/home`: 84334555136 available bytes; 95.29% used; 114152364 free inodes.

server3 `/data`: 124868542464 available bytes; 98.27% used; 225817944 free inodes.

server3 `/tmp`: 84334555136 available bytes; 95.29% used; 114152364 free inodes.

server3 `/var/tmp`: 84334555136 available bytes; 95.29% used; 114152364 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105196859392 available bytes; 94.13% used; 114346905 free inodes.

server4 `/home`: 105196859392 available bytes; 94.13% used; 114346905 free inodes.

server4 `/data`: 134748622848 available bytes; 98.14% used; 224917024 free inodes.

server4 `/tmp`: 105196859392 available bytes; 94.13% used; 114346905 free inodes.

server4 `/var/tmp`: 105196859392 available bytes; 94.13% used; 114346905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
