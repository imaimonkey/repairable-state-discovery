# V2R cluster inventory

2026-09-26T10:26:19.974298+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318234464256 available bytes; 82.25% used; 112474862 free inodes.

server1 `/home`: 318234464256 available bytes; 82.25% used; 112474862 free inodes.

server1 `/tmp`: 318234464256 available bytes; 82.25% used; 112474862 free inodes.

server1 `/var/tmp`: 318234464256 available bytes; 82.25% used; 112474862 free inodes.

server1 `/mnt/raid5`: 218839322624 available bytes; 99.00% used; 337538373 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19851771904 available bytes; 98.89% used; 110384909 free inodes.

server2 `/home`: 19851771904 available bytes; 98.89% used; 110384909 free inodes.

server2 `/tmp`: 19851771904 available bytes; 98.89% used; 110384909 free inodes.

server2 `/var/tmp`: 19851771904 available bytes; 98.89% used; 110384909 free inodes.

server2 `/mnt/raid5`: 243136147456 available bytes; 98.32% used; 444979837 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82662932480 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82662932480 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123588403200 available bytes; 98.29% used; 225826867 free inodes.

server3 `/tmp`: 82662932480 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82662932480 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105927688192 available bytes; 94.09% used; 114347978 free inodes.

server4 `/home`: 105927688192 available bytes; 94.09% used; 114347978 free inodes.

server4 `/data`: 89097867264 available bytes; 98.77% used; 224881463 free inodes.

server4 `/tmp`: 105927688192 available bytes; 94.09% used; 114347978 free inodes.

server4 `/var/tmp`: 105927688192 available bytes; 94.09% used; 114347978 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
