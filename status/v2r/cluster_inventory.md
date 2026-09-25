# V2R cluster inventory

2026-09-25T16:08:48.678459+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672121856 available bytes; 82.22% used; 112476319 free inodes.

server1 `/home`: 318672121856 available bytes; 82.22% used; 112476319 free inodes.

server1 `/tmp`: 318672121856 available bytes; 82.22% used; 112476319 free inodes.

server1 `/var/tmp`: 318672121856 available bytes; 82.22% used; 112476319 free inodes.

server1 `/mnt/raid5`: 367523520512 available bytes; 98.31% used; 337545197 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23115665408 available bytes; 98.71% used; 110407944 free inodes.

server2 `/home`: 23115665408 available bytes; 98.71% used; 110407944 free inodes.

server2 `/tmp`: 23115665408 available bytes; 98.71% used; 110407944 free inodes.

server2 `/var/tmp`: 23115665408 available bytes; 98.71% used; 110407944 free inodes.

server2 `/mnt/raid5`: 318968283136 available bytes; 97.80% used; 445071085 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84401958912 available bytes; 95.29% used; 114152674 free inodes.

server3 `/home`: 84401958912 available bytes; 95.29% used; 114152674 free inodes.

server3 `/data`: 134937743360 available bytes; 98.14% used; 225806337 free inodes.

server3 `/tmp`: 84401958912 available bytes; 95.29% used; 114152674 free inodes.

server3 `/var/tmp`: 84401958912 available bytes; 95.29% used; 114152674 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636777984 available bytes; 94.11% used; 114349663 free inodes.

server4 `/home`: 105636777984 available bytes; 94.11% used; 114349663 free inodes.

server4 `/data`: 231288832000 available bytes; 96.80% used; 224943186 free inodes.

server4 `/tmp`: 105636777984 available bytes; 94.11% used; 114349663 free inodes.

server4 `/var/tmp`: 105636777984 available bytes; 94.11% used; 114349663 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
