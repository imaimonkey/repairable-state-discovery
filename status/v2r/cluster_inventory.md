# V2R cluster inventory

2026-09-24T11:58:59.030598+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324278583296 available bytes; 81.91% used; 112488415 free inodes.

server1 `/home`: 324278583296 available bytes; 81.91% used; 112488415 free inodes.

server1 `/tmp`: 324278583296 available bytes; 81.91% used; 112488415 free inodes.

server1 `/var/tmp`: 324278583296 available bytes; 81.91% used; 112488415 free inodes.

server1 `/mnt/raid5`: 411685322752 available bytes; 98.11% used; 337686085 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57632239616 available bytes; 96.78% used; 110429712 free inodes.

server2 `/home`: 57632239616 available bytes; 96.78% used; 110429712 free inodes.

server2 `/tmp`: 57632239616 available bytes; 96.78% used; 110429712 free inodes.

server2 `/var/tmp`: 57632239616 available bytes; 96.78% used; 110429712 free inodes.

server2 `/mnt/raid5`: 509494153216 available bytes; 96.48% used; 445172986 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85748211712 available bytes; 95.21% used; 114198091 free inodes.

server3 `/home`: 85748211712 available bytes; 95.21% used; 114198091 free inodes.

server3 `/data`: 163597107200 available bytes; 97.74% used; 225815703 free inodes.

server3 `/tmp`: 85748211712 available bytes; 95.21% used; 114198091 free inodes.

server3 `/var/tmp`: 85748211712 available bytes; 95.21% used; 114198091 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105727197184 available bytes; 94.10% used; 114348830 free inodes.

server4 `/home`: 105727197184 available bytes; 94.10% used; 114348830 free inodes.

server4 `/data`: 115361304576 available bytes; 98.41% used; 225257840 free inodes.

server4 `/tmp`: 105727197184 available bytes; 94.10% used; 114348830 free inodes.

server4 `/var/tmp`: 105727197184 available bytes; 94.10% used; 114348830 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
