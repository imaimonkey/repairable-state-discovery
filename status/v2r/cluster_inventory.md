# V2R cluster inventory

2026-09-26T21:39:06.701958+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315478790144 available bytes; 82.40% used; 112445692 free inodes.

server1 `/home`: 315478790144 available bytes; 82.40% used; 112445692 free inodes.

server1 `/tmp`: 315478790144 available bytes; 82.40% used; 112445692 free inodes.

server1 `/var/tmp`: 315478790144 available bytes; 82.40% used; 112445692 free inodes.

server1 `/mnt/raid5`: 645855903744 available bytes; 97.04% used; 337467239 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17949741056 available bytes; 99.00% used; 110367527 free inodes.

server2 `/home`: 17949741056 available bytes; 99.00% used; 110367527 free inodes.

server2 `/tmp`: 17949741056 available bytes; 99.00% used; 110367527 free inodes.

server2 `/var/tmp`: 17949741056 available bytes; 99.00% used; 110367527 free inodes.

server2 `/mnt/raid5`: 598510854144 available bytes; 95.86% used; 444962762 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81094873088 available bytes; 95.47% used; 114069867 free inodes.

server3 `/home`: 81094873088 available bytes; 95.47% used; 114069867 free inodes.

server3 `/data`: 1349626920960 available bytes; 81.35% used; 225827615 free inodes.

server3 `/tmp`: 81094873088 available bytes; 95.47% used; 114069867 free inodes.

server3 `/var/tmp`: 81094873088 available bytes; 95.47% used; 114069867 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105900498944 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105900498944 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409891479552 available bytes; 94.34% used; 224823845 free inodes.

server4 `/tmp`: 105900498944 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105900498944 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
