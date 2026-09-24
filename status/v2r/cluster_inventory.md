# V2R cluster inventory

2026-09-24T13:35:43.342736+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324030742528 available bytes; 81.92% used; 112481513 free inodes.

server1 `/home`: 324030742528 available bytes; 81.92% used; 112481513 free inodes.

server1 `/tmp`: 324030742528 available bytes; 81.92% used; 112481513 free inodes.

server1 `/var/tmp`: 324030742528 available bytes; 81.92% used; 112481513 free inodes.

server1 `/mnt/raid5`: 417021579264 available bytes; 98.09% used; 337674550 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57520304128 available bytes; 96.79% used; 110428669 free inodes.

server2 `/home`: 57520304128 available bytes; 96.79% used; 110428669 free inodes.

server2 `/tmp`: 57520304128 available bytes; 96.79% used; 110428669 free inodes.

server2 `/var/tmp`: 57520304128 available bytes; 96.79% used; 110428669 free inodes.

server2 `/mnt/raid5`: 506462068736 available bytes; 96.50% used; 445169755 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84703105024 available bytes; 95.27% used; 114165420 free inodes.

server3 `/home`: 84703105024 available bytes; 95.27% used; 114165420 free inodes.

server3 `/data`: 161225486336 available bytes; 97.77% used; 225803071 free inodes.

server3 `/tmp`: 84703105024 available bytes; 95.27% used; 114165420 free inodes.

server3 `/var/tmp`: 84703105024 available bytes; 95.27% used; 114165420 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105769517056 available bytes; 94.10% used; 114348737 free inodes.

server4 `/home`: 105769517056 available bytes; 94.10% used; 114348737 free inodes.

server4 `/data`: 90043056128 available bytes; 98.76% used; 225257176 free inodes.

server4 `/tmp`: 105769517056 available bytes; 94.10% used; 114348737 free inodes.

server4 `/var/tmp`: 105769517056 available bytes; 94.10% used; 114348737 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
