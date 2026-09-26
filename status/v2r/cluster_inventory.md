# V2R cluster inventory

2026-09-26T20:51:50.713961+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315481747456 available bytes; 82.40% used; 112444680 free inodes.

server1 `/home`: 315481747456 available bytes; 82.40% used; 112444680 free inodes.

server1 `/tmp`: 315481747456 available bytes; 82.40% used; 112444680 free inodes.

server1 `/var/tmp`: 315481747456 available bytes; 82.40% used; 112444680 free inodes.

server1 `/mnt/raid5`: 645855055872 available bytes; 97.04% used; 337467121 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17973792768 available bytes; 99.00% used; 110367103 free inodes.

server2 `/home`: 17973792768 available bytes; 99.00% used; 110367103 free inodes.

server2 `/tmp`: 17973792768 available bytes; 99.00% used; 110367103 free inodes.

server2 `/var/tmp`: 17973792768 available bytes; 99.00% used; 110367103 free inodes.

server2 `/mnt/raid5`: 600068112384 available bytes; 95.85% used; 444963932 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81262465024 available bytes; 95.47% used; 114065289 free inodes.

server3 `/home`: 81262465024 available bytes; 95.47% used; 114065289 free inodes.

server3 `/data`: 1348594864128 available bytes; 81.36% used; 225831073 free inodes.

server3 `/tmp`: 81262465024 available bytes; 95.47% used; 114065289 free inodes.

server3 `/var/tmp`: 81262465024 available bytes; 95.47% used; 114065289 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918529536 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105918529536 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409969037312 available bytes; 94.33% used; 224823708 free inodes.

server4 `/tmp`: 105918529536 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105918529536 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
