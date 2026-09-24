# V2R cluster inventory

2026-09-24T22:56:14.014134+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323533189120 available bytes; 81.95% used; 112481227 free inodes.

server1 `/home`: 323533189120 available bytes; 81.95% used; 112481227 free inodes.

server1 `/tmp`: 323533189120 available bytes; 81.95% used; 112481227 free inodes.

server1 `/var/tmp`: 323533189120 available bytes; 81.95% used; 112481227 free inodes.

server1 `/mnt/raid5`: 415304462336 available bytes; 98.09% used; 337617246 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23131287552 available bytes; 98.71% used; 110410897 free inodes.

server2 `/home`: 23131287552 available bytes; 98.71% used; 110410897 free inodes.

server2 `/tmp`: 23131287552 available bytes; 98.71% used; 110410897 free inodes.

server2 `/var/tmp`: 23131287552 available bytes; 98.71% used; 110410897 free inodes.

server2 `/mnt/raid5`: 487208443904 available bytes; 96.63% used; 445152386 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84371394560 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84371394560 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 148843397120 available bytes; 97.94% used; 225801582 free inodes.

server3 `/tmp`: 84371394560 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84371394560 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800994816 available bytes; 94.10% used; 114348319 free inodes.

server4 `/home`: 105800994816 available bytes; 94.10% used; 114348319 free inodes.

server4 `/data`: 62661881856 available bytes; 99.13% used; 225197123 free inodes.

server4 `/tmp`: 105800994816 available bytes; 94.10% used; 114348319 free inodes.

server4 `/var/tmp`: 105800994816 available bytes; 94.10% used; 114348319 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
