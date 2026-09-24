# V2R cluster inventory

2026-09-24T13:38:56.310180+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324029329408 available bytes; 81.92% used; 112481515 free inodes.

server1 `/home`: 324029329408 available bytes; 81.92% used; 112481515 free inodes.

server1 `/tmp`: 324029329408 available bytes; 81.92% used; 112481515 free inodes.

server1 `/var/tmp`: 324029329408 available bytes; 81.92% used; 112481515 free inodes.

server1 `/mnt/raid5`: 417010802688 available bytes; 98.09% used; 337674180 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57516060672 available bytes; 96.79% used; 110428635 free inodes.

server2 `/home`: 57516060672 available bytes; 96.79% used; 110428635 free inodes.

server2 `/tmp`: 57516060672 available bytes; 96.79% used; 110428635 free inodes.

server2 `/var/tmp`: 57516060672 available bytes; 96.79% used; 110428635 free inodes.

server2 `/mnt/raid5`: 506362867712 available bytes; 96.50% used; 445169533 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84701966336 available bytes; 95.27% used; 114165411 free inodes.

server3 `/home`: 84701966336 available bytes; 95.27% used; 114165411 free inodes.

server3 `/data`: 161201180672 available bytes; 97.77% used; 225803009 free inodes.

server3 `/tmp`: 84701966336 available bytes; 95.27% used; 114165411 free inodes.

server3 `/var/tmp`: 84701966336 available bytes; 95.27% used; 114165411 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761030144 available bytes; 94.10% used; 114348737 free inodes.

server4 `/home`: 105761030144 available bytes; 94.10% used; 114348737 free inodes.

server4 `/data`: 90038284288 available bytes; 98.76% used; 225257170 free inodes.

server4 `/tmp`: 105761030144 available bytes; 94.10% used; 114348737 free inodes.

server4 `/var/tmp`: 105761030144 available bytes; 94.10% used; 114348737 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
