# V2R cluster inventory

2026-09-25T19:20:01.550474+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318735163392 available bytes; 82.22% used; 112476341 free inodes.

server1 `/home`: 318735163392 available bytes; 82.22% used; 112476341 free inodes.

server1 `/tmp`: 318735163392 available bytes; 82.22% used; 112476341 free inodes.

server1 `/var/tmp`: 318735163392 available bytes; 82.22% used; 112476341 free inodes.

server1 `/mnt/raid5`: 370882306048 available bytes; 98.30% used; 337540840 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23097606144 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23097606144 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23097606144 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23097606144 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 312362086400 available bytes; 97.84% used; 445064646 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382773248 available bytes; 95.29% used; 114152623 free inodes.

server3 `/home`: 84382773248 available bytes; 95.29% used; 114152623 free inodes.

server3 `/data`: 129288798208 available bytes; 98.21% used; 225808764 free inodes.

server3 `/tmp`: 84382773248 available bytes; 95.29% used; 114152623 free inodes.

server3 `/var/tmp`: 84382773248 available bytes; 95.29% used; 114152623 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105675087872 available bytes; 94.10% used; 114349588 free inodes.

server4 `/home`: 105675087872 available bytes; 94.10% used; 114349588 free inodes.

server4 `/data`: 229639401472 available bytes; 96.83% used; 224930494 free inodes.

server4 `/tmp`: 105675087872 available bytes; 94.10% used; 114349588 free inodes.

server4 `/var/tmp`: 105675087872 available bytes; 94.10% used; 114349588 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
