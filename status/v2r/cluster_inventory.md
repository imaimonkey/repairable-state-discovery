# V2R cluster inventory

2026-09-26T10:18:41.657937+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318241841152 available bytes; 82.25% used; 112474926 free inodes.

server1 `/home`: 318241841152 available bytes; 82.25% used; 112474926 free inodes.

server1 `/tmp`: 318241841152 available bytes; 82.25% used; 112474926 free inodes.

server1 `/var/tmp`: 318241841152 available bytes; 82.25% used; 112474926 free inodes.

server1 `/mnt/raid5`: 218855047168 available bytes; 99.00% used; 337538414 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19846623232 available bytes; 98.89% used; 110384906 free inodes.

server2 `/home`: 19846623232 available bytes; 98.89% used; 110384906 free inodes.

server2 `/tmp`: 19846623232 available bytes; 98.89% used; 110384906 free inodes.

server2 `/var/tmp`: 19846623232 available bytes; 98.89% used; 110384906 free inodes.

server2 `/mnt/raid5`: 243354402816 available bytes; 98.32% used; 444979947 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82659135488 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82659135488 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123588694016 available bytes; 98.29% used; 225826986 free inodes.

server3 `/tmp`: 82659135488 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82659135488 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105930743808 available bytes; 94.09% used; 114348032 free inodes.

server4 `/home`: 105930743808 available bytes; 94.09% used; 114348032 free inodes.

server4 `/data`: 89113817088 available bytes; 98.77% used; 224881911 free inodes.

server4 `/tmp`: 105930743808 available bytes; 94.09% used; 114348032 free inodes.

server4 `/var/tmp`: 105930743808 available bytes; 94.09% used; 114348032 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
