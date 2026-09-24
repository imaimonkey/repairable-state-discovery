# V2R cluster inventory

2026-09-24T11:35:27.114411+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324346601472 available bytes; 81.91% used; 112488844 free inodes.

server1 `/home`: 324346601472 available bytes; 81.91% used; 112488844 free inodes.

server1 `/tmp`: 324346601472 available bytes; 81.91% used; 112488844 free inodes.

server1 `/var/tmp`: 324346601472 available bytes; 81.91% used; 112488844 free inodes.

server1 `/mnt/raid5`: 438568546304 available bytes; 97.99% used; 337688822 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57661145088 available bytes; 96.78% used; 110429946 free inodes.

server2 `/home`: 57661145088 available bytes; 96.78% used; 110429946 free inodes.

server2 `/tmp`: 57661145088 available bytes; 96.78% used; 110429946 free inodes.

server2 `/var/tmp`: 57661145088 available bytes; 96.78% used; 110429946 free inodes.

server2 `/mnt/raid5`: 510480834560 available bytes; 96.47% used; 445173309 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85413367808 available bytes; 95.23% used; 114183478 free inodes.

server3 `/home`: 85413367808 available bytes; 95.23% used; 114183478 free inodes.

server3 `/data`: 163762216960 available bytes; 97.74% used; 225816529 free inodes.

server3 `/tmp`: 85413367808 available bytes; 95.23% used; 114183478 free inodes.

server3 `/var/tmp`: 85413367808 available bytes; 95.23% used; 114183478 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105730686976 available bytes; 94.10% used; 114348873 free inodes.

server4 `/home`: 105730686976 available bytes; 94.10% used; 114348873 free inodes.

server4 `/data`: 115509714944 available bytes; 98.40% used; 225258040 free inodes.

server4 `/tmp`: 105730686976 available bytes; 94.10% used; 114348873 free inodes.

server4 `/var/tmp`: 105730686976 available bytes; 94.10% used; 114348873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
