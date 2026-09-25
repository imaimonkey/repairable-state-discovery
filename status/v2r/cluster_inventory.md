# V2R cluster inventory

2026-09-25T01:05:41.773741+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319077953536 available bytes; 82.20% used; 112480777 free inodes.

server1 `/home`: 319077953536 available bytes; 82.20% used; 112480777 free inodes.

server1 `/tmp`: 319077953536 available bytes; 82.20% used; 112480777 free inodes.

server1 `/var/tmp`: 319077953536 available bytes; 82.20% used; 112480777 free inodes.

server1 `/mnt/raid5`: 416783683584 available bytes; 98.09% used; 337615810 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23066136576 available bytes; 98.71% used; 110410768 free inodes.

server2 `/home`: 23066136576 available bytes; 98.71% used; 110410768 free inodes.

server2 `/tmp`: 23066136576 available bytes; 98.71% used; 110410768 free inodes.

server2 `/var/tmp`: 23066136576 available bytes; 98.71% used; 110410768 free inodes.

server2 `/mnt/raid5`: 497783967744 available bytes; 96.56% used; 445162376 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84354002944 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84354002944 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148293914624 available bytes; 97.95% used; 225812778 free inodes.

server3 `/tmp`: 84354002944 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84354002944 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105787998208 available bytes; 94.10% used; 114348301 free inodes.

server4 `/home`: 105787998208 available bytes; 94.10% used; 114348301 free inodes.

server4 `/data`: 53845200896 available bytes; 99.26% used; 225030897 free inodes.

server4 `/tmp`: 105787998208 available bytes; 94.10% used; 114348301 free inodes.

server4 `/var/tmp`: 105787998208 available bytes; 94.10% used; 114348301 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
