# V2R cluster inventory

2026-09-25T18:20:23.255158+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318757462016 available bytes; 82.22% used; 112476348 free inodes.

server1 `/home`: 318757462016 available bytes; 82.22% used; 112476348 free inodes.

server1 `/tmp`: 318757462016 available bytes; 82.22% used; 112476348 free inodes.

server1 `/var/tmp`: 318757462016 available bytes; 82.22% used; 112476348 free inodes.

server1 `/mnt/raid5`: 371199324160 available bytes; 98.30% used; 337542038 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23096684544 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23096684544 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23096684544 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23096684544 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 314263289856 available bytes; 97.83% used; 445066772 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84391297024 available bytes; 95.29% used; 114152615 free inodes.

server3 `/home`: 84391297024 available bytes; 95.29% used; 114152615 free inodes.

server3 `/data`: 131465527296 available bytes; 98.18% used; 225810036 free inodes.

server3 `/tmp`: 84391297024 available bytes; 95.29% used; 114152615 free inodes.

server3 `/var/tmp`: 84391297024 available bytes; 95.29% used; 114152615 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616117760 available bytes; 94.11% used; 114349601 free inodes.

server4 `/home`: 105616117760 available bytes; 94.11% used; 114349601 free inodes.

server4 `/data`: 229706469376 available bytes; 96.83% used; 224931932 free inodes.

server4 `/tmp`: 105616117760 available bytes; 94.11% used; 114349601 free inodes.

server4 `/var/tmp`: 105616117760 available bytes; 94.11% used; 114349601 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
