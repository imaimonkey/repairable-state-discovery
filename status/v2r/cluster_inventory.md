# V2R cluster inventory

2026-09-26T20:27:27.309191+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315482857472 available bytes; 82.40% used; 112444700 free inodes.

server1 `/home`: 315482857472 available bytes; 82.40% used; 112444700 free inodes.

server1 `/tmp`: 315482857472 available bytes; 82.40% used; 112444700 free inodes.

server1 `/var/tmp`: 315482857472 available bytes; 82.40% used; 112444700 free inodes.

server1 `/mnt/raid5`: 645855199232 available bytes; 97.04% used; 337467119 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17982353408 available bytes; 99.00% used; 110367111 free inodes.

server2 `/home`: 17982353408 available bytes; 99.00% used; 110367111 free inodes.

server2 `/tmp`: 17982353408 available bytes; 99.00% used; 110367111 free inodes.

server2 `/var/tmp`: 17982353408 available bytes; 99.00% used; 110367111 free inodes.

server2 `/mnt/raid5`: 600759214080 available bytes; 95.85% used; 444964468 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81263243264 available bytes; 95.47% used; 114065299 free inodes.

server3 `/home`: 81263243264 available bytes; 95.47% used; 114065299 free inodes.

server3 `/data`: 1348620357632 available bytes; 81.36% used; 225831831 free inodes.

server3 `/tmp`: 81263243264 available bytes; 95.47% used; 114065299 free inodes.

server3 `/var/tmp`: 81263243264 available bytes; 95.47% used; 114065299 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105919111168 available bytes; 94.09% used; 114347833 free inodes.

server4 `/home`: 105919111168 available bytes; 94.09% used; 114347833 free inodes.

server4 `/data`: 410200674304 available bytes; 94.33% used; 224823722 free inodes.

server4 `/tmp`: 105919111168 available bytes; 94.09% used; 114347833 free inodes.

server4 `/var/tmp`: 105919111168 available bytes; 94.09% used; 114347833 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
