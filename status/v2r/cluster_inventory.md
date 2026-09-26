# V2R cluster inventory

2026-09-26T08:09:15.853692+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318751608832 available bytes; 82.22% used; 112476264 free inodes.

server1 `/home`: 318751608832 available bytes; 82.22% used; 112476264 free inodes.

server1 `/tmp`: 318751608832 available bytes; 82.22% used; 112476264 free inodes.

server1 `/var/tmp`: 318751608832 available bytes; 82.22% used; 112476264 free inodes.

server1 `/mnt/raid5`: 219153539072 available bytes; 98.99% used; 337539053 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22314364928 available bytes; 98.76% used; 110403907 free inodes.

server2 `/home`: 22314364928 available bytes; 98.76% used; 110403907 free inodes.

server2 `/tmp`: 22314364928 available bytes; 98.76% used; 110403907 free inodes.

server2 `/var/tmp`: 22314364928 available bytes; 98.76% used; 110403907 free inodes.

server2 `/mnt/raid5`: 256326053888 available bytes; 98.23% used; 445025509 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82679971840 available bytes; 95.39% used; 114110821 free inodes.

server3 `/home`: 82679971840 available bytes; 95.39% used; 114110821 free inodes.

server3 `/data`: 123918196736 available bytes; 98.29% used; 225829393 free inodes.

server3 `/tmp`: 82679971840 available bytes; 95.39% used; 114110821 free inodes.

server3 `/var/tmp`: 82679971840 available bytes; 95.39% used; 114110821 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106064822272 available bytes; 94.08% used; 114348149 free inodes.

server4 `/home`: 106064822272 available bytes; 94.08% used; 114348149 free inodes.

server4 `/data`: 89419931648 available bytes; 98.76% used; 224885078 free inodes.

server4 `/tmp`: 106064822272 available bytes; 94.08% used; 114348149 free inodes.

server4 `/var/tmp`: 106064822272 available bytes; 94.08% used; 114348149 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
