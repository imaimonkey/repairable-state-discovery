# V2R cluster inventory

2026-09-27T02:19:37.048054+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315159379968 available bytes; 82.42% used; 112443332 free inodes.

server1 `/home`: 315159379968 available bytes; 82.42% used; 112443332 free inodes.

server1 `/tmp`: 315159379968 available bytes; 82.42% used; 112443332 free inodes.

server1 `/var/tmp`: 315159379968 available bytes; 82.42% used; 112443332 free inodes.

server1 `/mnt/raid5`: 637264322560 available bytes; 97.08% used; 337401673 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17636515840 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17636515840 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17636515840 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17636515840 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 580738060288 available bytes; 95.99% used; 444884821 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78710517760 available bytes; 95.61% used; 114062955 free inodes.

server3 `/home`: 78710517760 available bytes; 95.61% used; 114062955 free inodes.

server3 `/data`: 1337719672832 available bytes; 81.51% used; 225762481 free inodes.

server3 `/tmp`: 78710517760 available bytes; 95.61% used; 114062955 free inodes.

server3 `/var/tmp`: 78710517760 available bytes; 95.61% used; 114062955 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111036723200 available bytes; 93.80% used; 114373265 free inodes.

server4 `/home`: 111036723200 available bytes; 93.80% used; 114373265 free inodes.

server4 `/data`: 400384864256 available bytes; 94.47% used; 224781757 free inodes.

server4 `/tmp`: 111036723200 available bytes; 93.80% used; 114373265 free inodes.

server4 `/var/tmp`: 111036723200 available bytes; 93.80% used; 114373265 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
