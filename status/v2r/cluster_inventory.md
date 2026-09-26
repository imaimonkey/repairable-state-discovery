# V2R cluster inventory

2026-09-26T21:25:23.243192+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315481477120 available bytes; 82.40% used; 112445689 free inodes.

server1 `/home`: 315481477120 available bytes; 82.40% used; 112445689 free inodes.

server1 `/tmp`: 315481477120 available bytes; 82.40% used; 112445689 free inodes.

server1 `/var/tmp`: 315481477120 available bytes; 82.40% used; 112445689 free inodes.

server1 `/mnt/raid5`: 645855936512 available bytes; 97.04% used; 337467239 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17942323200 available bytes; 99.00% used; 110367525 free inodes.

server2 `/home`: 17942323200 available bytes; 99.00% used; 110367525 free inodes.

server2 `/tmp`: 17942323200 available bytes; 99.00% used; 110367525 free inodes.

server2 `/var/tmp`: 17942323200 available bytes; 99.00% used; 110367525 free inodes.

server2 `/mnt/raid5`: 598910148608 available bytes; 95.86% used; 444963009 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81389940736 available bytes; 95.46% used; 114084664 free inodes.

server3 `/home`: 81389940736 available bytes; 95.46% used; 114084664 free inodes.

server3 `/data`: 1349671333888 available bytes; 81.35% used; 225828619 free inodes.

server3 `/tmp`: 81389940736 available bytes; 95.46% used; 114084664 free inodes.

server3 `/var/tmp`: 81389940736 available bytes; 95.46% used; 114084664 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105909211136 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105909211136 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409902211072 available bytes; 94.33% used; 224823845 free inodes.

server4 `/tmp`: 105909211136 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105909211136 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
