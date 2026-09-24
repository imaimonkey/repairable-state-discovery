# V2R cluster inventory

2026-09-24T02:11:48.565608+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325445218304 available bytes; 81.84% used; 112499225 free inodes.

server1 `/home`: 325445218304 available bytes; 81.84% used; 112499225 free inodes.

server1 `/tmp`: 325445218304 available bytes; 81.84% used; 112499225 free inodes.

server1 `/var/tmp`: 325445218304 available bytes; 81.84% used; 112499225 free inodes.

server1 `/mnt/raid5`: 725262385152 available bytes; 96.67% used; 337733505 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40906600448 available bytes; 97.72% used; 110431664 free inodes.

server2 `/home`: 40906600448 available bytes; 97.72% used; 110431664 free inodes.

server2 `/tmp`: 40906600448 available bytes; 97.72% used; 110431664 free inodes.

server2 `/var/tmp`: 40906600448 available bytes; 97.72% used; 110431664 free inodes.

server2 `/mnt/raid5`: 529583407104 available bytes; 96.34% used; 445200065 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292685062144 available bytes; 83.67% used; 114210523 free inodes.

server3 `/home`: 292685062144 available bytes; 83.67% used; 114210523 free inodes.

server3 `/data`: 18082553856 available bytes; 99.75% used; 225841304 free inodes.

server3 `/tmp`: 292685062144 available bytes; 83.67% used; 114210523 free inodes.

server3 `/var/tmp`: 292685062144 available bytes; 83.67% used; 114210523 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105932419072 available bytes; 94.09% used; 114348278 free inodes.

server4 `/home`: 105932419072 available bytes; 94.09% used; 114348278 free inodes.

server4 `/data`: 289761374208 available bytes; 96.00% used; 225388462 free inodes.

server4 `/tmp`: 105932419072 available bytes; 94.09% used; 114348278 free inodes.

server4 `/var/tmp`: 105932419072 available bytes; 94.09% used; 114348278 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
