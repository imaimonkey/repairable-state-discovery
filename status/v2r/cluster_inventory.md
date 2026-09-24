# V2R cluster inventory

2026-09-24T13:48:16.862213+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324030963712 available bytes; 81.92% used; 112481504 free inodes.

server1 `/home`: 324030963712 available bytes; 81.92% used; 112481504 free inodes.

server1 `/tmp`: 324030963712 available bytes; 81.92% used; 112481504 free inodes.

server1 `/var/tmp`: 324030963712 available bytes; 81.92% used; 112481504 free inodes.

server1 `/mnt/raid5`: 416989044736 available bytes; 98.09% used; 337673092 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57504067584 available bytes; 96.79% used; 110428533 free inodes.

server2 `/home`: 57504067584 available bytes; 96.79% used; 110428533 free inodes.

server2 `/tmp`: 57504067584 available bytes; 96.79% used; 110428533 free inodes.

server2 `/var/tmp`: 57504067584 available bytes; 96.79% used; 110428533 free inodes.

server2 `/mnt/raid5`: 506067972096 available bytes; 96.50% used; 445169053 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85064179712 available bytes; 95.25% used; 114187597 free inodes.

server3 `/home`: 85064179712 available bytes; 95.25% used; 114187597 free inodes.

server3 `/data`: 161129189376 available bytes; 97.77% used; 225802810 free inodes.

server3 `/tmp`: 85064179712 available bytes; 95.25% used; 114187597 free inodes.

server3 `/var/tmp`: 85064179712 available bytes; 95.25% used; 114187597 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105760608256 available bytes; 94.10% used; 114348727 free inodes.

server4 `/home`: 105760608256 available bytes; 94.10% used; 114348727 free inodes.

server4 `/data`: 90039164928 available bytes; 98.76% used; 225257168 free inodes.

server4 `/tmp`: 105760608256 available bytes; 94.10% used; 114348727 free inodes.

server4 `/var/tmp`: 105760608256 available bytes; 94.10% used; 114348727 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
