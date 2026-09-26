# V2R cluster inventory

2026-09-26T10:55:21.681838+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318212833280 available bytes; 82.25% used; 112474831 free inodes.

server1 `/home`: 318212833280 available bytes; 82.25% used; 112474831 free inodes.

server1 `/tmp`: 318212833280 available bytes; 82.25% used; 112474831 free inodes.

server1 `/var/tmp`: 318212833280 available bytes; 82.25% used; 112474831 free inodes.

server1 `/mnt/raid5`: 218776408064 available bytes; 99.00% used; 337538242 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19844321280 available bytes; 98.89% used; 110384887 free inodes.

server2 `/home`: 19844321280 available bytes; 98.89% used; 110384887 free inodes.

server2 `/tmp`: 19844321280 available bytes; 98.89% used; 110384887 free inodes.

server2 `/var/tmp`: 19844321280 available bytes; 98.89% used; 110384887 free inodes.

server2 `/mnt/raid5`: 242490769408 available bytes; 98.32% used; 444979512 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82662866944 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82662866944 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123573063680 available bytes; 98.29% used; 225826092 free inodes.

server3 `/tmp`: 82662866944 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82662866944 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105926762496 available bytes; 94.09% used; 114347962 free inodes.

server4 `/home`: 105926762496 available bytes; 94.09% used; 114347962 free inodes.

server4 `/data`: 88904540160 available bytes; 98.77% used; 224880565 free inodes.

server4 `/tmp`: 105926762496 available bytes; 94.09% used; 114347962 free inodes.

server4 `/var/tmp`: 105926762496 available bytes; 94.09% used; 114347962 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
