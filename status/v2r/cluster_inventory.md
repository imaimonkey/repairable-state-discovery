# V2R cluster inventory

2026-09-25T18:44:50.289890+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318743650304 available bytes; 82.22% used; 112476344 free inodes.

server1 `/home`: 318743650304 available bytes; 82.22% used; 112476344 free inodes.

server1 `/tmp`: 318743650304 available bytes; 82.22% used; 112476344 free inodes.

server1 `/var/tmp`: 318743650304 available bytes; 82.22% used; 112476344 free inodes.

server1 `/mnt/raid5`: 371161726976 available bytes; 98.30% used; 337541431 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23095779328 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23095779328 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23095779328 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23095779328 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 313522413568 available bytes; 97.83% used; 445065830 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380909568 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84380909568 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 131382976512 available bytes; 98.18% used; 225809447 free inodes.

server3 `/tmp`: 84380909568 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84380909568 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105607073792 available bytes; 94.11% used; 114349599 free inodes.

server4 `/home`: 105607073792 available bytes; 94.11% used; 114349599 free inodes.

server4 `/data`: 229694414848 available bytes; 96.83% used; 224931547 free inodes.

server4 `/tmp`: 105607073792 available bytes; 94.11% used; 114349599 free inodes.

server4 `/var/tmp`: 105607073792 available bytes; 94.11% used; 114349599 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
