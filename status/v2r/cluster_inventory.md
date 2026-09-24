# V2R cluster inventory

2026-09-24T13:46:42.702275+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324031393792 available bytes; 81.92% used; 112481506 free inodes.

server1 `/home`: 324031393792 available bytes; 81.92% used; 112481506 free inodes.

server1 `/tmp`: 324031393792 available bytes; 81.92% used; 112481506 free inodes.

server1 `/var/tmp`: 324031393792 available bytes; 81.92% used; 112481506 free inodes.

server1 `/mnt/raid5`: 416991301632 available bytes; 98.09% used; 337673269 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57504206848 available bytes; 96.79% used; 110428548 free inodes.

server2 `/home`: 57504206848 available bytes; 96.79% used; 110428548 free inodes.

server2 `/tmp`: 57504206848 available bytes; 96.79% used; 110428548 free inodes.

server2 `/var/tmp`: 57504206848 available bytes; 96.79% used; 110428548 free inodes.

server2 `/mnt/raid5`: 506111684608 available bytes; 96.50% used; 445169161 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85075726336 available bytes; 95.25% used; 114188028 free inodes.

server3 `/home`: 85075726336 available bytes; 95.25% used; 114188028 free inodes.

server3 `/data`: 161141018624 available bytes; 97.77% used; 225802842 free inodes.

server3 `/tmp`: 85075726336 available bytes; 95.25% used; 114188028 free inodes.

server3 `/var/tmp`: 85075726336 available bytes; 95.25% used; 114188028 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105760710656 available bytes; 94.10% used; 114348729 free inodes.

server4 `/home`: 105760710656 available bytes; 94.10% used; 114348729 free inodes.

server4 `/data`: 90040270848 available bytes; 98.76% used; 225257170 free inodes.

server4 `/tmp`: 105760710656 available bytes; 94.10% used; 114348729 free inodes.

server4 `/var/tmp`: 105760710656 available bytes; 94.10% used; 114348729 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
