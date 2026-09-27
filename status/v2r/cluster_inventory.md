# V2R cluster inventory

2026-09-27T13:19:57.537952+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304672526336 available bytes; 83.00% used; 112401381 free inodes.

server1 `/home`: 304672526336 available bytes; 83.00% used; 112401381 free inodes.

server1 `/tmp`: 304672526336 available bytes; 83.00% used; 112401381 free inodes.

server1 `/var/tmp`: 304672526336 available bytes; 83.00% used; 112401381 free inodes.

server1 `/mnt/raid5`: 634602852352 available bytes; 97.09% used; 337424234 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 13417394176 available bytes; 99.25% used; 110351834 free inodes.

server2 `/home`: 13417394176 available bytes; 99.25% used; 110351834 free inodes.

server2 `/tmp`: 13417394176 available bytes; 99.25% used; 110351834 free inodes.

server2 `/var/tmp`: 13417394176 available bytes; 99.25% used; 110351834 free inodes.

server2 `/mnt/raid5`: 529033408512 available bytes; 96.34% used; 444733621 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78568611840 available bytes; 95.62% used; 114062843 free inodes.

server3 `/home`: 78568611840 available bytes; 95.62% used; 114062843 free inodes.

server3 `/data`: 1331280326656 available bytes; 81.60% used; 225757626 free inodes.

server3 `/tmp`: 78568611840 available bytes; 95.62% used; 114062843 free inodes.

server3 `/var/tmp`: 78568611840 available bytes; 95.62% used; 114062843 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111010705408 available bytes; 93.81% used; 114372796 free inodes.

server4 `/home`: 111010705408 available bytes; 93.81% used; 114372796 free inodes.

server4 `/data`: 351447252992 available bytes; 95.14% used; 224727749 free inodes.

server4 `/tmp`: 111010705408 available bytes; 93.81% used; 114372796 free inodes.

server4 `/var/tmp`: 111010705408 available bytes; 93.81% used; 114372796 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
