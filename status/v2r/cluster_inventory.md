# V2R cluster inventory

2026-09-26T08:03:09.605542+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318751555584 available bytes; 82.22% used; 112476273 free inodes.

server1 `/home`: 318751555584 available bytes; 82.22% used; 112476273 free inodes.

server1 `/tmp`: 318751555584 available bytes; 82.22% used; 112476273 free inodes.

server1 `/var/tmp`: 318751555584 available bytes; 82.22% used; 112476273 free inodes.

server1 `/mnt/raid5`: 211574697984 available bytes; 99.03% used; 337539081 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22322647040 available bytes; 98.75% used; 110403909 free inodes.

server2 `/home`: 22322647040 available bytes; 98.75% used; 110403909 free inodes.

server2 `/tmp`: 22322647040 available bytes; 98.75% used; 110403909 free inodes.

server2 `/var/tmp`: 22322647040 available bytes; 98.75% used; 110403909 free inodes.

server2 `/mnt/raid5`: 255966371840 available bytes; 98.23% used; 445025700 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82678460416 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82678460416 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123888123904 available bytes; 98.29% used; 225820479 free inodes.

server3 `/tmp`: 82678460416 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82678460416 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106073403392 available bytes; 94.08% used; 114348153 free inodes.

server4 `/home`: 106073403392 available bytes; 94.08% used; 114348153 free inodes.

server4 `/data`: 105378099200 available bytes; 98.54% used; 224922240 free inodes.

server4 `/tmp`: 106073403392 available bytes; 94.08% used; 114348153 free inodes.

server4 `/var/tmp`: 106073403392 available bytes; 94.08% used; 114348153 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
