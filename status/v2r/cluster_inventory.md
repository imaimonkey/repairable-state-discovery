# V2R cluster inventory

2026-09-25T22:57:02.686323+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318695108608 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318695108608 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318695108608 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318695108608 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 360189509632 available bytes; 98.35% used; 337538818 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22946623488 available bytes; 98.72% used; 110406228 free inodes.

server2 `/home`: 22946623488 available bytes; 98.72% used; 110406228 free inodes.

server2 `/tmp`: 22946623488 available bytes; 98.72% used; 110406228 free inodes.

server2 `/var/tmp`: 22946623488 available bytes; 98.72% used; 110406228 free inodes.

server2 `/mnt/raid5`: 298202841088 available bytes; 97.94% used; 445052115 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351692800 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84351692800 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124822708224 available bytes; 98.27% used; 225805494 free inodes.

server3 `/tmp`: 84351692800 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84351692800 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105168101376 available bytes; 94.13% used; 114346790 free inodes.

server4 `/home`: 105168101376 available bytes; 94.13% used; 114346790 free inodes.

server4 `/data`: 185228488704 available bytes; 97.44% used; 224917660 free inodes.

server4 `/tmp`: 105168101376 available bytes; 94.13% used; 114346790 free inodes.

server4 `/var/tmp`: 105168101376 available bytes; 94.13% used; 114346790 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
