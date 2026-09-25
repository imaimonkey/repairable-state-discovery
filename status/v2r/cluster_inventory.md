# V2R cluster inventory

2026-09-25T19:23:04.922621+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318736674816 available bytes; 82.22% used; 112476348 free inodes.

server1 `/home`: 318736674816 available bytes; 82.22% used; 112476348 free inodes.

server1 `/tmp`: 318736674816 available bytes; 82.22% used; 112476348 free inodes.

server1 `/var/tmp`: 318736674816 available bytes; 82.22% used; 112476348 free inodes.

server1 `/mnt/raid5`: 350230474752 available bytes; 98.39% used; 337540824 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23094468608 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23094468608 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23094468608 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23094468608 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 311731957760 available bytes; 97.85% used; 445064489 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381941760 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84381941760 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 129284599808 available bytes; 98.21% used; 225808715 free inodes.

server3 `/tmp`: 84381941760 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84381941760 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105675018240 available bytes; 94.10% used; 114349586 free inodes.

server4 `/home`: 105675018240 available bytes; 94.10% used; 114349586 free inodes.

server4 `/data`: 229634297856 available bytes; 96.83% used; 224930305 free inodes.

server4 `/tmp`: 105675018240 available bytes; 94.10% used; 114349586 free inodes.

server4 `/var/tmp`: 105675018240 available bytes; 94.10% used; 114349586 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
