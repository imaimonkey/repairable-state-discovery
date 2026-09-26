# V2R cluster inventory

2026-09-26T10:25:03.043035+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318237753344 available bytes; 82.25% used; 112474874 free inodes.

server1 `/home`: 318237753344 available bytes; 82.25% used; 112474874 free inodes.

server1 `/tmp`: 318237753344 available bytes; 82.25% used; 112474874 free inodes.

server1 `/var/tmp`: 318237753344 available bytes; 82.25% used; 112474874 free inodes.

server1 `/mnt/raid5`: 218842677248 available bytes; 99.00% used; 337538382 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19853242368 available bytes; 98.89% used; 110384909 free inodes.

server2 `/home`: 19853242368 available bytes; 98.89% used; 110384909 free inodes.

server2 `/tmp`: 19853242368 available bytes; 98.89% used; 110384909 free inodes.

server2 `/var/tmp`: 19853242368 available bytes; 98.89% used; 110384909 free inodes.

server2 `/mnt/raid5`: 243705888768 available bytes; 98.32% used; 444979989 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82663075840 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82663075840 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123585871872 available bytes; 98.29% used; 225826886 free inodes.

server3 `/tmp`: 82663075840 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82663075840 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105927716864 available bytes; 94.09% used; 114347978 free inodes.

server4 `/home`: 105927716864 available bytes; 94.09% used; 114347978 free inodes.

server4 `/data`: 89103450112 available bytes; 98.77% used; 224881466 free inodes.

server4 `/tmp`: 105927716864 available bytes; 94.09% used; 114347978 free inodes.

server4 `/var/tmp`: 105927716864 available bytes; 94.09% used; 114347978 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
