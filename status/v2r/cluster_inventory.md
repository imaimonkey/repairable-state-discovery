# V2R cluster inventory

2026-09-26T10:32:40.929006+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318223302656 available bytes; 82.25% used; 112474820 free inodes.

server1 `/home`: 318223302656 available bytes; 82.25% used; 112474820 free inodes.

server1 `/tmp`: 318223302656 available bytes; 82.25% used; 112474820 free inodes.

server1 `/var/tmp`: 318223302656 available bytes; 82.25% used; 112474820 free inodes.

server1 `/mnt/raid5`: 218825146368 available bytes; 99.00% used; 337538345 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19850989568 available bytes; 98.89% used; 110384909 free inodes.

server2 `/home`: 19850989568 available bytes; 98.89% used; 110384909 free inodes.

server2 `/tmp`: 19850989568 available bytes; 98.89% used; 110384909 free inodes.

server2 `/var/tmp`: 19850989568 available bytes; 98.89% used; 110384909 free inodes.

server2 `/mnt/raid5`: 243472191488 available bytes; 98.32% used; 444979532 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82662457344 available bytes; 95.39% used; 114110827 free inodes.

server3 `/home`: 82662457344 available bytes; 95.39% used; 114110827 free inodes.

server3 `/data`: 123582799872 available bytes; 98.29% used; 225826764 free inodes.

server3 `/tmp`: 82662457344 available bytes; 95.39% used; 114110827 free inodes.

server3 `/var/tmp`: 82662457344 available bytes; 95.39% used; 114110827 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105927475200 available bytes; 94.09% used; 114347978 free inodes.

server4 `/home`: 105927475200 available bytes; 94.09% used; 114347978 free inodes.

server4 `/data`: 89088991232 available bytes; 98.77% used; 224881441 free inodes.

server4 `/tmp`: 105927475200 available bytes; 94.09% used; 114347978 free inodes.

server4 `/var/tmp`: 105927475200 available bytes; 94.09% used; 114347978 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
