# V2R cluster inventory

2026-09-25T02:22:44.679560+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318970748928 available bytes; 82.21% used; 112480505 free inodes.

server1 `/home`: 318970748928 available bytes; 82.21% used; 112480505 free inodes.

server1 `/tmp`: 318970748928 available bytes; 82.21% used; 112480505 free inodes.

server1 `/var/tmp`: 318970748928 available bytes; 82.21% used; 112480505 free inodes.

server1 `/mnt/raid5`: 416227295232 available bytes; 98.09% used; 337606794 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23016452096 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 23016452096 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 23016452096 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 23016452096 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462998687744 available bytes; 96.80% used; 445114095 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84356026368 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84356026368 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 145722052608 available bytes; 97.99% used; 225811183 free inodes.

server3 `/tmp`: 84356026368 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84356026368 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105896148992 available bytes; 94.09% used; 114351001 free inodes.

server4 `/home`: 105896148992 available bytes; 94.09% used; 114351001 free inodes.

server4 `/data`: 37675016192 available bytes; 99.48% used; 224970316 free inodes.

server4 `/tmp`: 105896148992 available bytes; 94.09% used; 114351001 free inodes.

server4 `/var/tmp`: 105896148992 available bytes; 94.09% used; 114351001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
