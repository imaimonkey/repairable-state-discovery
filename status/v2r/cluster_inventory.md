# V2R cluster inventory

2026-09-25T00:10:18.286707+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319089016832 available bytes; 82.20% used; 112480789 free inodes.

server1 `/home`: 319089016832 available bytes; 82.20% used; 112480789 free inodes.

server1 `/tmp`: 319089016832 available bytes; 82.20% used; 112480789 free inodes.

server1 `/var/tmp`: 319089016832 available bytes; 82.20% used; 112480789 free inodes.

server1 `/mnt/raid5`: 416891469824 available bytes; 98.09% used; 337622184 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23094460416 available bytes; 98.71% used; 110410785 free inodes.

server2 `/home`: 23094460416 available bytes; 98.71% used; 110410785 free inodes.

server2 `/tmp`: 23094460416 available bytes; 98.71% used; 110410785 free inodes.

server2 `/var/tmp`: 23094460416 available bytes; 98.71% used; 110410785 free inodes.

server2 `/mnt/raid5`: 486565560320 available bytes; 96.64% used; 445163473 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84354015232 available bytes; 95.29% used; 114156082 free inodes.

server3 `/home`: 84354015232 available bytes; 95.29% used; 114156082 free inodes.

server3 `/data`: 149234544640 available bytes; 97.94% used; 225813812 free inodes.

server3 `/tmp`: 84354015232 available bytes; 95.29% used; 114156082 free inodes.

server3 `/var/tmp`: 84354015232 available bytes; 95.29% used; 114156082 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105797865472 available bytes; 94.10% used; 114348297 free inodes.

server4 `/home`: 105797865472 available bytes; 94.10% used; 114348297 free inodes.

server4 `/data`: 57705496576 available bytes; 99.20% used; 225086860 free inodes.

server4 `/tmp`: 105797865472 available bytes; 94.10% used; 114348297 free inodes.

server4 `/var/tmp`: 105797865472 available bytes; 94.10% used; 114348297 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
