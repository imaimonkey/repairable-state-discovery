# V2R cluster inventory

2026-09-25T16:50:09.539162+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318681251840 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318681251840 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318681251840 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318681251840 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 364372615168 available bytes; 98.33% used; 337544098 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23108718592 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23108718592 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23108718592 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23108718592 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 317232078848 available bytes; 97.81% used; 445069556 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84396138496 available bytes; 95.29% used; 114152627 free inodes.

server3 `/home`: 84396138496 available bytes; 95.29% used; 114152627 free inodes.

server3 `/data`: 133785124864 available bytes; 98.15% used; 225805337 free inodes.

server3 `/tmp`: 84396138496 available bytes; 95.29% used; 114152627 free inodes.

server3 `/var/tmp`: 84396138496 available bytes; 95.29% used; 114152627 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105635553280 available bytes; 94.11% used; 114349641 free inodes.

server4 `/home`: 105635553280 available bytes; 94.11% used; 114349641 free inodes.

server4 `/data`: 229990584320 available bytes; 96.82% used; 224933590 free inodes.

server4 `/tmp`: 105635553280 available bytes; 94.11% used; 114349641 free inodes.

server4 `/var/tmp`: 105635553280 available bytes; 94.11% used; 114349641 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
