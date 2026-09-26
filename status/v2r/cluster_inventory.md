# V2R cluster inventory

2026-09-26T04:56:51.072629+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318399741952 available bytes; 82.24% used; 112476282 free inodes.

server1 `/home`: 318399741952 available bytes; 82.24% used; 112476282 free inodes.

server1 `/tmp`: 318399741952 available bytes; 82.24% used; 112476282 free inodes.

server1 `/var/tmp`: 318399741952 available bytes; 82.24% used; 112476282 free inodes.

server1 `/mnt/raid5`: 309331398656 available bytes; 98.58% used; 337545058 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22937911296 available bytes; 98.72% used; 110406198 free inodes.

server2 `/home`: 22937911296 available bytes; 98.72% used; 110406198 free inodes.

server2 `/tmp`: 22937911296 available bytes; 98.72% used; 110406198 free inodes.

server2 `/var/tmp`: 22937911296 available bytes; 98.72% used; 110406198 free inodes.

server2 `/mnt/raid5`: 276597690368 available bytes; 98.09% used; 445049680 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83811397632 available bytes; 95.32% used; 114139095 free inodes.

server3 `/home`: 83811397632 available bytes; 95.32% used; 114139095 free inodes.

server3 `/data`: 124626731008 available bytes; 98.28% used; 225825719 free inodes.

server3 `/tmp`: 83811397632 available bytes; 95.32% used; 114139095 free inodes.

server3 `/var/tmp`: 83811397632 available bytes; 95.32% used; 114139095 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105993256960 available bytes; 94.09% used; 114348206 free inodes.

server4 `/home`: 105993256960 available bytes; 94.09% used; 114348206 free inodes.

server4 `/data`: 106997465088 available bytes; 98.52% used; 224929241 free inodes.

server4 `/tmp`: 105993256960 available bytes; 94.09% used; 114348206 free inodes.

server4 `/var/tmp`: 105993256960 available bytes; 94.09% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
