# V2R cluster inventory

2026-09-25T23:58:11.446224+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672330752 available bytes; 82.22% used; 112476306 free inodes.

server1 `/home`: 318672330752 available bytes; 82.22% used; 112476306 free inodes.

server1 `/tmp`: 318672330752 available bytes; 82.22% used; 112476306 free inodes.

server1 `/var/tmp`: 318672330752 available bytes; 82.22% used; 112476306 free inodes.

server1 `/mnt/raid5`: 360040341504 available bytes; 98.35% used; 337538510 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22943977472 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22943977472 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22943977472 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22943977472 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 296209858560 available bytes; 97.95% used; 445050164 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84348010496 available bytes; 95.29% used; 114152432 free inodes.

server3 `/home`: 84348010496 available bytes; 95.29% used; 114152432 free inodes.

server3 `/data`: 124802699264 available bytes; 98.28% used; 225810950 free inodes.

server3 `/tmp`: 84348010496 available bytes; 95.29% used; 114152432 free inodes.

server3 `/var/tmp`: 84348010496 available bytes; 95.29% used; 114152432 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105082273792 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082273792 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178214969344 available bytes; 97.54% used; 224917578 free inodes.

server4 `/tmp`: 105082273792 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082273792 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
