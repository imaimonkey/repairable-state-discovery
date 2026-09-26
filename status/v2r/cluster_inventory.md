# V2R cluster inventory

2026-09-26T12:39:18.998635+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318162460672 available bytes; 82.25% used; 112474481 free inodes.

server1 `/home`: 318162460672 available bytes; 82.25% used; 112474481 free inodes.

server1 `/tmp`: 318162460672 available bytes; 82.25% used; 112474481 free inodes.

server1 `/var/tmp`: 318162460672 available bytes; 82.25% used; 112474481 free inodes.

server1 `/mnt/raid5`: 218547220480 available bytes; 99.00% used; 337537707 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 19273342976 available bytes; 98.92% used; 110381976 free inodes.

server2 `/home`: 19273342976 available bytes; 98.92% used; 110381976 free inodes.

server2 `/tmp`: 19273342976 available bytes; 98.92% used; 110381976 free inodes.

server2 `/var/tmp`: 19273342976 available bytes; 98.92% used; 110381976 free inodes.

server2 `/mnt/raid5`: 240022663168 available bytes; 98.34% used; 444978888 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82649841664 available bytes; 95.39% used; 114110831 free inodes.

server3 `/home`: 82649841664 available bytes; 95.39% used; 114110831 free inodes.

server3 `/data`: 123398586368 available bytes; 98.29% used; 225823495 free inodes.

server3 `/tmp`: 82649841664 available bytes; 95.39% used; 114110831 free inodes.

server3 `/var/tmp`: 82649841664 available bytes; 95.39% used; 114110831 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899528192 available bytes; 94.09% used; 114347942 free inodes.

server4 `/home`: 105899528192 available bytes; 94.09% used; 114347942 free inodes.

server4 `/data`: 88533299200 available bytes; 98.78% used; 224878836 free inodes.

server4 `/tmp`: 105899528192 available bytes; 94.09% used; 114347942 free inodes.

server4 `/var/tmp`: 105899528192 available bytes; 94.09% used; 114347942 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
