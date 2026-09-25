# V2R cluster inventory

2026-09-25T18:24:58.526121+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318749655040 available bytes; 82.22% used; 112476345 free inodes.

server1 `/home`: 318749655040 available bytes; 82.22% used; 112476345 free inodes.

server1 `/tmp`: 318749655040 available bytes; 82.22% used; 112476345 free inodes.

server1 `/var/tmp`: 318749655040 available bytes; 82.22% used; 112476345 free inodes.

server1 `/mnt/raid5`: 371195047936 available bytes; 98.30% used; 337541937 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23096340480 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23096340480 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23096340480 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23096340480 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 314135576576 available bytes; 97.83% used; 445066815 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84391628800 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84391628800 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 131457294336 available bytes; 98.18% used; 225809938 free inodes.

server3 `/tmp`: 84391628800 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84391628800 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616007168 available bytes; 94.11% used; 114349601 free inodes.

server4 `/home`: 105616007168 available bytes; 94.11% used; 114349601 free inodes.

server4 `/data`: 229704904704 available bytes; 96.83% used; 224931862 free inodes.

server4 `/tmp`: 105616007168 available bytes; 94.11% used; 114349601 free inodes.

server4 `/var/tmp`: 105616007168 available bytes; 94.11% used; 114349601 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
