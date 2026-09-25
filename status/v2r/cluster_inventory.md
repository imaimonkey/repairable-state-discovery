# V2R cluster inventory

2026-09-25T22:56:39.576060+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318695116800 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318695116800 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318695116800 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318695116800 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 360188157952 available bytes; 98.35% used; 337538815 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22945595392 available bytes; 98.72% used; 110406228 free inodes.

server2 `/home`: 22945595392 available bytes; 98.72% used; 110406228 free inodes.

server2 `/tmp`: 22945595392 available bytes; 98.72% used; 110406228 free inodes.

server2 `/var/tmp`: 22945595392 available bytes; 98.72% used; 110406228 free inodes.

server2 `/mnt/raid5`: 298205937664 available bytes; 97.94% used; 445052028 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84351700992 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84351700992 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124822310912 available bytes; 98.27% used; 225805509 free inodes.

server3 `/tmp`: 84351700992 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84351700992 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105201491968 available bytes; 94.13% used; 114346837 free inodes.

server4 `/home`: 105201491968 available bytes; 94.13% used; 114346837 free inodes.

server4 `/data`: 185228513280 available bytes; 97.44% used; 224917660 free inodes.

server4 `/tmp`: 105201491968 available bytes; 94.13% used; 114346837 free inodes.

server4 `/var/tmp`: 105201491968 available bytes; 94.13% used; 114346837 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
