# V2R cluster inventory

2026-09-26T08:56:11.677164+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318745468928 available bytes; 82.22% used; 112475806 free inodes.

server1 `/home`: 318745468928 available bytes; 82.22% used; 112475806 free inodes.

server1 `/tmp`: 318745468928 available bytes; 82.22% used; 112475806 free inodes.

server1 `/var/tmp`: 318745468928 available bytes; 82.22% used; 112475806 free inodes.

server1 `/mnt/raid5`: 219045142528 available bytes; 99.00% used; 337538815 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22322614272 available bytes; 98.75% used; 110403909 free inodes.

server2 `/home`: 22322614272 available bytes; 98.75% used; 110403909 free inodes.

server2 `/tmp`: 22322614272 available bytes; 98.75% used; 110403909 free inodes.

server2 `/var/tmp`: 22322614272 available bytes; 98.75% used; 110403909 free inodes.

server2 `/mnt/raid5`: 255208755200 available bytes; 98.24% used; 445024033 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82662412288 available bytes; 95.39% used; 114110812 free inodes.

server3 `/home`: 82662412288 available bytes; 95.39% used; 114110812 free inodes.

server3 `/data`: 123903143936 available bytes; 98.29% used; 225828347 free inodes.

server3 `/tmp`: 82662412288 available bytes; 95.39% used; 114110812 free inodes.

server3 `/var/tmp`: 82662412288 available bytes; 95.39% used; 114110812 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106054967296 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106054967296 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89350807552 available bytes; 98.77% used; 224883351 free inodes.

server4 `/tmp`: 106054967296 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106054967296 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
