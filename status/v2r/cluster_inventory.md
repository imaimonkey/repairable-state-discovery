# V2R cluster inventory

2026-09-25T19:33:46.549206+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318724190208 available bytes; 82.22% used; 112476323 free inodes.

server1 `/home`: 318724190208 available bytes; 82.22% used; 112476323 free inodes.

server1 `/tmp`: 318724190208 available bytes; 82.22% used; 112476323 free inodes.

server1 `/var/tmp`: 318724190208 available bytes; 82.22% used; 112476323 free inodes.

server1 `/mnt/raid5`: 370855329792 available bytes; 98.30% used; 337540783 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23095611392 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23095611392 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23095611392 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23095611392 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 311951003648 available bytes; 97.84% used; 445064450 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381519872 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84381519872 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 128230395904 available bytes; 98.23% used; 225808509 free inodes.

server3 `/tmp`: 84381519872 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84381519872 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674653696 available bytes; 94.10% used; 114349579 free inodes.

server4 `/home`: 105674653696 available bytes; 94.10% used; 114349579 free inodes.

server4 `/data`: 229593505792 available bytes; 96.83% used; 224929782 free inodes.

server4 `/tmp`: 105674653696 available bytes; 94.10% used; 114349579 free inodes.

server4 `/var/tmp`: 105674653696 available bytes; 94.10% used; 114349579 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
