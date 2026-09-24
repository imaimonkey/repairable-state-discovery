# V2R cluster inventory

2026-09-24T09:54:06.766761+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324442218496 available bytes; 81.90% used; 112489603 free inodes.

server1 `/home`: 324442218496 available bytes; 81.90% used; 112489603 free inodes.

server1 `/tmp`: 324442218496 available bytes; 81.90% used; 112489603 free inodes.

server1 `/var/tmp`: 324442218496 available bytes; 81.90% used; 112489603 free inodes.

server1 `/mnt/raid5`: 500724469760 available bytes; 97.70% used; 337702073 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57756405760 available bytes; 96.78% used; 110430753 free inodes.

server2 `/home`: 57756405760 available bytes; 96.78% used; 110430753 free inodes.

server2 `/tmp`: 57756405760 available bytes; 96.78% used; 110430753 free inodes.

server2 `/var/tmp`: 57756405760 available bytes; 96.78% used; 110430753 free inodes.

server2 `/mnt/raid5`: 513873358848 available bytes; 96.45% used; 445177061 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85811699712 available bytes; 95.21% used; 114198982 free inodes.

server3 `/home`: 85811699712 available bytes; 95.21% used; 114198982 free inodes.

server3 `/data`: 165605486592 available bytes; 97.71% used; 225819724 free inodes.

server3 `/tmp`: 85811699712 available bytes; 95.21% used; 114198982 free inodes.

server3 `/var/tmp`: 85811699712 available bytes; 95.21% used; 114198982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748287488 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748287488 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154560778240 available bytes; 97.86% used; 225273209 free inodes.

server4 `/tmp`: 105748287488 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748287488 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
