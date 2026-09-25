# V2R cluster inventory

2026-09-25T19:52:06.686856+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318712393728 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318712393728 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318712393728 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318712393728 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 370828640256 available bytes; 98.30% used; 337540697 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23099936768 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23099936768 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23099936768 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23099936768 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 310883938304 available bytes; 97.85% used; 445063549 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380553216 available bytes; 95.29% used; 114152628 free inodes.

server3 `/home`: 84380553216 available bytes; 95.29% used; 114152628 free inodes.

server3 `/data`: 128250667008 available bytes; 98.23% used; 225808692 free inodes.

server3 `/tmp`: 84380553216 available bytes; 95.29% used; 114152628 free inodes.

server3 `/var/tmp`: 84380553216 available bytes; 95.29% used; 114152628 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674035200 available bytes; 94.10% used; 114349568 free inodes.

server4 `/home`: 105674035200 available bytes; 94.10% used; 114349568 free inodes.

server4 `/data`: 229540712448 available bytes; 96.83% used; 224929319 free inodes.

server4 `/tmp`: 105674035200 available bytes; 94.10% used; 114349568 free inodes.

server4 `/var/tmp`: 105674035200 available bytes; 94.10% used; 114349568 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
