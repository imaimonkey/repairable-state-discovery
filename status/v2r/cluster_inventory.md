# V2R cluster inventory

2026-09-26T21:05:34.302191+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315487154176 available bytes; 82.40% used; 112445684 free inodes.

server1 `/home`: 315487154176 available bytes; 82.40% used; 112445684 free inodes.

server1 `/tmp`: 315487154176 available bytes; 82.40% used; 112445684 free inodes.

server1 `/var/tmp`: 315487154176 available bytes; 82.40% used; 112445684 free inodes.

server1 `/mnt/raid5`: 645855064064 available bytes; 97.04% used; 337467121 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17938767872 available bytes; 99.00% used; 110367525 free inodes.

server2 `/home`: 17938767872 available bytes; 99.00% used; 110367525 free inodes.

server2 `/tmp`: 17938767872 available bytes; 99.00% used; 110367525 free inodes.

server2 `/var/tmp`: 17938767872 available bytes; 99.00% used; 110367525 free inodes.

server2 `/mnt/raid5`: 598854942720 available bytes; 95.86% used; 444963676 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81267441664 available bytes; 95.46% used; 114065310 free inodes.

server3 `/home`: 81267441664 available bytes; 95.46% used; 114065310 free inodes.

server3 `/data`: 1351152721920 available bytes; 81.33% used; 225832125 free inodes.

server3 `/tmp`: 81267441664 available bytes; 95.46% used; 114065310 free inodes.

server3 `/var/tmp`: 81267441664 available bytes; 95.46% used; 114065310 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918111744 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105918111744 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409921085440 available bytes; 94.33% used; 224823843 free inodes.

server4 `/tmp`: 105918111744 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105918111744 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
