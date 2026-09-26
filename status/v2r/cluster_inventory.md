# V2R cluster inventory

2026-09-26T06:03:30.106540+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318778736640 available bytes; 82.22% used; 112476283 free inodes.

server1 `/home`: 318778736640 available bytes; 82.22% used; 112476283 free inodes.

server1 `/tmp`: 318778736640 available bytes; 82.22% used; 112476283 free inodes.

server1 `/var/tmp`: 318778736640 available bytes; 82.22% used; 112476283 free inodes.

server1 `/mnt/raid5`: 227156144128 available bytes; 98.96% used; 337539963 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22736310272 available bytes; 98.73% used; 110405648 free inodes.

server2 `/home`: 22736310272 available bytes; 98.73% used; 110405648 free inodes.

server2 `/tmp`: 22736310272 available bytes; 98.73% used; 110405648 free inodes.

server2 `/var/tmp`: 22736310272 available bytes; 98.73% used; 110405648 free inodes.

server2 `/mnt/raid5`: 274465251328 available bytes; 98.10% used; 445033343 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82439671808 available bytes; 95.40% used; 114110902 free inodes.

server3 `/home`: 82439671808 available bytes; 95.40% used; 114110902 free inodes.

server3 `/data`: 123990880256 available bytes; 98.29% used; 225822738 free inodes.

server3 `/tmp`: 82439671808 available bytes; 95.40% used; 114110902 free inodes.

server3 `/var/tmp`: 82439671808 available bytes; 95.40% used; 114110902 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094002176 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094002176 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106988351488 available bytes; 98.52% used; 224929125 free inodes.

server4 `/tmp`: 106094002176 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094002176 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
