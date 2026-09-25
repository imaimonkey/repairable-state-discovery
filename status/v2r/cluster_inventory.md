# V2R cluster inventory

2026-09-25T15:18:21.061442+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318829522944 available bytes; 82.21% used; 112476396 free inodes.

server1 `/home`: 318829522944 available bytes; 82.21% used; 112476396 free inodes.

server1 `/tmp`: 318829522944 available bytes; 82.21% used; 112476396 free inodes.

server1 `/var/tmp`: 318829522944 available bytes; 82.21% used; 112476396 free inodes.

server1 `/mnt/raid5`: 363952640000 available bytes; 98.33% used; 337545904 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23108120576 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23108120576 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23108120576 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23108120576 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 320298627072 available bytes; 97.79% used; 445073373 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84425527296 available bytes; 95.29% used; 114153463 free inodes.

server3 `/home`: 84425527296 available bytes; 95.29% used; 114153463 free inodes.

server3 `/data`: 142177873920 available bytes; 98.04% used; 225807931 free inodes.

server3 `/tmp`: 84425527296 available bytes; 95.29% used; 114153463 free inodes.

server3 `/var/tmp`: 84425527296 available bytes; 95.29% used; 114153463 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638191104 available bytes; 94.11% used; 114349680 free inodes.

server4 `/home`: 105638191104 available bytes; 94.11% used; 114349680 free inodes.

server4 `/data`: 231287881728 available bytes; 96.80% used; 224944701 free inodes.

server4 `/tmp`: 105638191104 available bytes; 94.11% used; 114349680 free inodes.

server4 `/var/tmp`: 105638191104 available bytes; 94.11% used; 114349680 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
