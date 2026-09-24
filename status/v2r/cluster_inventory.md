# V2R cluster inventory

2026-09-24T21:31:29.635548+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323954302976 available bytes; 81.93% used; 112481417 free inodes.

server1 `/home`: 323954302976 available bytes; 81.93% used; 112481417 free inodes.

server1 `/tmp`: 323954302976 available bytes; 81.93% used; 112481417 free inodes.

server1 `/var/tmp`: 323954302976 available bytes; 81.93% used; 112481417 free inodes.

server1 `/mnt/raid5`: 415494823936 available bytes; 98.09% used; 337627305 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30140104704 available bytes; 98.32% used; 110411342 free inodes.

server2 `/home`: 30140104704 available bytes; 98.32% used; 110411342 free inodes.

server2 `/tmp`: 30140104704 available bytes; 98.32% used; 110411342 free inodes.

server2 `/var/tmp`: 30140104704 available bytes; 98.32% used; 110411342 free inodes.

server2 `/mnt/raid5`: 490354991104 available bytes; 96.61% used; 445154827 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84383367168 available bytes; 95.29% used; 114156095 free inodes.

server3 `/home`: 84383367168 available bytes; 95.29% used; 114156095 free inodes.

server3 `/data`: 150269980672 available bytes; 97.92% used; 225803165 free inodes.

server3 `/tmp`: 84383367168 available bytes; 95.29% used; 114156095 free inodes.

server3 `/var/tmp`: 84383367168 available bytes; 95.29% used; 114156095 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105630146560 available bytes; 94.11% used; 114348350 free inodes.

server4 `/home`: 105630146560 available bytes; 94.11% used; 114348350 free inodes.

server4 `/data`: 83457548288 available bytes; 98.85% used; 225252840 free inodes.

server4 `/tmp`: 105630146560 available bytes; 94.11% used; 114348350 free inodes.

server4 `/var/tmp`: 105630146560 available bytes; 94.11% used; 114348350 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
