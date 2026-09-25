# V2R cluster inventory

2026-09-25T19:39:53.409442+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318725898240 available bytes; 82.22% used; 112476323 free inodes.

server1 `/home`: 318725898240 available bytes; 82.22% used; 112476323 free inodes.

server1 `/tmp`: 318725898240 available bytes; 82.22% used; 112476323 free inodes.

server1 `/var/tmp`: 318725898240 available bytes; 82.22% used; 112476323 free inodes.

server1 `/mnt/raid5`: 370848903168 available bytes; 98.30% used; 337540757 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23101906944 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23101906944 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23101906944 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23101906944 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 311764422656 available bytes; 97.85% used; 445063995 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382302208 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84382302208 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 128228405248 available bytes; 98.23% used; 225808407 free inodes.

server3 `/tmp`: 84382302208 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84382302208 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674436608 available bytes; 94.10% used; 114349572 free inodes.

server4 `/home`: 105674436608 available bytes; 94.10% used; 114349572 free inodes.

server4 `/data`: 229587537920 available bytes; 96.83% used; 224929714 free inodes.

server4 `/tmp`: 105674436608 available bytes; 94.10% used; 114349572 free inodes.

server4 `/var/tmp`: 105674436608 available bytes; 94.10% used; 114349572 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
