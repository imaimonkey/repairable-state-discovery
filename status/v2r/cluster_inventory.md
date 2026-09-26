# V2R cluster inventory

2026-09-26T14:53:31.381602+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318120386560 available bytes; 82.25% used; 112474347 free inodes.

server1 `/home`: 318120386560 available bytes; 82.25% used; 112474347 free inodes.

server1 `/tmp`: 318120386560 available bytes; 82.25% used; 112474347 free inodes.

server1 `/var/tmp`: 318120386560 available bytes; 82.25% used; 112474347 free inodes.

server1 `/mnt/raid5`: 660209262592 available bytes; 96.97% used; 337531883 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 12216598528 available bytes; 99.32% used; 110367705 free inodes.

server2 `/home`: 12216598528 available bytes; 99.32% used; 110367705 free inodes.

server2 `/tmp`: 12216598528 available bytes; 99.32% used; 110367705 free inodes.

server2 `/var/tmp`: 12216598528 available bytes; 99.32% used; 110367705 free inodes.

server2 `/mnt/raid5`: 633440907264 available bytes; 95.62% used; 444974032 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82630811648 available bytes; 95.39% used; 114110773 free inodes.

server3 `/home`: 82630811648 available bytes; 95.39% used; 114110773 free inodes.

server3 `/data`: 1346846547968 available bytes; 81.39% used; 225804947 free inodes.

server3 `/tmp`: 82630811648 available bytes; 95.39% used; 114110773 free inodes.

server3 `/var/tmp`: 82630811648 available bytes; 95.39% used; 114110773 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886416896 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105886416896 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410830114816 available bytes; 94.32% used; 224826277 free inodes.

server4 `/tmp`: 105886416896 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105886416896 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
