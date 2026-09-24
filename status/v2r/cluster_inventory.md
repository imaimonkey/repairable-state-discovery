# V2R cluster inventory

2026-09-24T03:49:20.782538+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324738863104 available bytes; 81.88% used; 112493692 free inodes.

server1 `/home`: 324738863104 available bytes; 81.88% used; 112493692 free inodes.

server1 `/tmp`: 324738863104 available bytes; 81.88% used; 112493692 free inodes.

server1 `/var/tmp`: 324738863104 available bytes; 81.88% used; 112493692 free inodes.

server1 `/mnt/raid5`: 406965424128 available bytes; 98.13% used; 337724818 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40817225728 available bytes; 97.72% used; 110430952 free inodes.

server2 `/home`: 40817225728 available bytes; 97.72% used; 110430952 free inodes.

server2 `/tmp`: 40817225728 available bytes; 97.72% used; 110430952 free inodes.

server2 `/var/tmp`: 40817225728 available bytes; 97.72% used; 110430952 free inodes.

server2 `/mnt/raid5`: 526629703680 available bytes; 96.36% used; 445197333 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292362645504 available bytes; 83.69% used; 114197805 free inodes.

server3 `/home`: 292362645504 available bytes; 83.69% used; 114197805 free inodes.

server3 `/data`: 33874903040 available bytes; 99.53% used; 225842632 free inodes.

server3 `/tmp`: 292362645504 available bytes; 83.69% used; 114197805 free inodes.

server3 `/var/tmp`: 292362645504 available bytes; 83.69% used; 114197805 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105792634880 available bytes; 94.10% used; 114349566 free inodes.

server4 `/home`: 105792634880 available bytes; 94.10% used; 114349566 free inodes.

server4 `/data`: 275757301760 available bytes; 96.19% used; 225384132 free inodes.

server4 `/tmp`: 105792634880 available bytes; 94.10% used; 114349566 free inodes.

server4 `/var/tmp`: 105792634880 available bytes; 94.10% used; 114349566 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
