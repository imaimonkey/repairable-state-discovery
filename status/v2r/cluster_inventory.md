# V2R cluster inventory

2026-09-26T08:07:44.286719+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318751977472 available bytes; 82.22% used; 112476264 free inodes.

server1 `/home`: 318751977472 available bytes; 82.22% used; 112476264 free inodes.

server1 `/tmp`: 318751977472 available bytes; 82.22% used; 112476264 free inodes.

server1 `/var/tmp`: 318751977472 available bytes; 82.22% used; 112476264 free inodes.

server1 `/mnt/raid5`: 219152756736 available bytes; 98.99% used; 337539048 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22316105728 available bytes; 98.76% used; 110403907 free inodes.

server2 `/home`: 22316105728 available bytes; 98.76% used; 110403907 free inodes.

server2 `/tmp`: 22316105728 available bytes; 98.76% used; 110403907 free inodes.

server2 `/var/tmp`: 22316105728 available bytes; 98.76% used; 110403907 free inodes.

server2 `/mnt/raid5`: 256372518912 available bytes; 98.23% used; 445025563 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 82680442880 available bytes; 95.39% used; 114110839 free inodes.

server3 `/home`: 82680442880 available bytes; 95.39% used; 114110839 free inodes.

server3 `/data`: 123919605760 available bytes; 98.29% used; 225829434 free inodes.

server3 `/tmp`: 82680442880 available bytes; 95.39% used; 114110839 free inodes.

server3 `/var/tmp`: 82680442880 available bytes; 95.39% used; 114110839 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106064859136 available bytes; 94.08% used; 114348147 free inodes.

server4 `/home`: 106064859136 available bytes; 94.08% used; 114348147 free inodes.

server4 `/data`: 90731204608 available bytes; 98.75% used; 224900756 free inodes.

server4 `/tmp`: 106064859136 available bytes; 94.08% used; 114348147 free inodes.

server4 `/var/tmp`: 106064859136 available bytes; 94.08% used; 114348147 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
