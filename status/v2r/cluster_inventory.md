# V2R cluster inventory

2026-09-26T03:47:24.477705+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416830464 available bytes; 82.24% used; 112476261 free inodes.

server1 `/home`: 318416830464 available bytes; 82.24% used; 112476261 free inodes.

server1 `/tmp`: 318416830464 available bytes; 82.24% used; 112476261 free inodes.

server1 `/var/tmp`: 318416830464 available bytes; 82.24% used; 112476261 free inodes.

server1 `/mnt/raid5`: 330981261312 available bytes; 98.48% used; 337545716 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939308032 available bytes; 98.72% used; 110406210 free inodes.

server2 `/home`: 22939308032 available bytes; 98.72% used; 110406210 free inodes.

server2 `/tmp`: 22939308032 available bytes; 98.72% used; 110406210 free inodes.

server2 `/var/tmp`: 22939308032 available bytes; 98.72% used; 110406210 free inodes.

server2 `/mnt/raid5`: 286735749120 available bytes; 98.02% used; 445051873 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84312813568 available bytes; 95.30% used; 114152362 free inodes.

server3 `/home`: 84312813568 available bytes; 95.30% used; 114152362 free inodes.

server3 `/data`: 125357162496 available bytes; 98.27% used; 225830303 free inodes.

server3 `/tmp`: 84312813568 available bytes; 95.30% used; 114152362 free inodes.

server3 `/var/tmp`: 84312813568 available bytes; 95.30% used; 114152362 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105766170624 available bytes; 94.10% used; 114346783 free inodes.

server4 `/home`: 105766170624 available bytes; 94.10% used; 114346783 free inodes.

server4 `/data`: 108863217664 available bytes; 98.50% used; 224914682 free inodes.

server4 `/tmp`: 105766170624 available bytes; 94.10% used; 114346783 free inodes.

server4 `/var/tmp`: 105766170624 available bytes; 94.10% used; 114346783 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
