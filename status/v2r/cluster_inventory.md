# V2R cluster inventory

2026-09-26T05:45:06.898169+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318781497344 available bytes; 82.22% used; 112476275 free inodes.

server1 `/home`: 318781497344 available bytes; 82.22% used; 112476275 free inodes.

server1 `/tmp`: 318781497344 available bytes; 82.22% used; 112476275 free inodes.

server1 `/var/tmp`: 318781497344 available bytes; 82.22% used; 112476275 free inodes.

server1 `/mnt/raid5`: 240005857280 available bytes; 98.90% used; 337540067 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22894870528 available bytes; 98.72% used; 110405874 free inodes.

server2 `/home`: 22894870528 available bytes; 98.72% used; 110405874 free inodes.

server2 `/tmp`: 22894870528 available bytes; 98.72% used; 110405874 free inodes.

server2 `/var/tmp`: 22894870528 available bytes; 98.72% used; 110405874 free inodes.

server2 `/mnt/raid5`: 274973102080 available bytes; 98.10% used; 445034563 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 83170897920 available bytes; 95.36% used; 114149765 free inodes.

server3 `/home`: 83170897920 available bytes; 95.36% used; 114149765 free inodes.

server3 `/data`: 124273958912 available bytes; 98.28% used; 225823986 free inodes.

server3 `/tmp`: 83170897920 available bytes; 95.36% used; 114149765 free inodes.

server3 `/var/tmp`: 83170897920 available bytes; 95.36% used; 114149765 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094510080 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094510080 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106989613056 available bytes; 98.52% used; 224929132 free inodes.

server4 `/tmp`: 106094510080 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094510080 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
