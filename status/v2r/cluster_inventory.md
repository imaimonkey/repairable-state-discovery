# V2R cluster inventory

2026-09-24T11:44:55.226483+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324348780544 available bytes; 81.91% used; 112488824 free inodes.

server1 `/home`: 324348780544 available bytes; 81.91% used; 112488824 free inodes.

server1 `/tmp`: 324348780544 available bytes; 81.91% used; 112488824 free inodes.

server1 `/var/tmp`: 324348780544 available bytes; 81.91% used; 112488824 free inodes.

server1 `/mnt/raid5`: 427976015872 available bytes; 98.04% used; 337687632 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57646010368 available bytes; 96.78% used; 110429854 free inodes.

server2 `/home`: 57646010368 available bytes; 96.78% used; 110429854 free inodes.

server2 `/tmp`: 57646010368 available bytes; 96.78% used; 110429854 free inodes.

server2 `/var/tmp`: 57646010368 available bytes; 96.78% used; 110429854 free inodes.

server2 `/mnt/raid5`: 510176849920 available bytes; 96.47% used; 445172918 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85247209472 available bytes; 95.24% used; 114166915 free inodes.

server3 `/home`: 85247209472 available bytes; 95.24% used; 114166915 free inodes.

server3 `/data`: 163691253760 available bytes; 97.74% used; 225815971 free inodes.

server3 `/tmp`: 85247209472 available bytes; 95.24% used; 114166915 free inodes.

server3 `/var/tmp`: 85247209472 available bytes; 95.24% used; 114166915 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105729560576 available bytes; 94.10% used; 114348852 free inodes.

server4 `/home`: 105729560576 available bytes; 94.10% used; 114348852 free inodes.

server4 `/data`: 115388657664 available bytes; 98.41% used; 225257966 free inodes.

server4 `/tmp`: 105729560576 available bytes; 94.10% used; 114348852 free inodes.

server4 `/var/tmp`: 105729560576 available bytes; 94.10% used; 114348852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
