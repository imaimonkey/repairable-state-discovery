# V2R cluster inventory

2026-09-25T07:22:59.554946+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871044096 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318871044096 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318871044096 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318871044096 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 385916649472 available bytes; 98.23% used; 337558473 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22860345344 available bytes; 98.72% used; 110410500 free inodes.

server2 `/home`: 22860345344 available bytes; 98.72% used; 110410500 free inodes.

server2 `/tmp`: 22860345344 available bytes; 98.72% used; 110410500 free inodes.

server2 `/var/tmp`: 22860345344 available bytes; 98.72% used; 110410500 free inodes.

server2 `/mnt/raid5`: 343390453760 available bytes; 97.63% used; 445097566 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 84446687232 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84446687232 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142396739584 available bytes; 98.03% used; 225812826 free inodes.

server3 `/tmp`: 84446687232 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84446687232 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638092800 available bytes; 94.11% used; 114350361 free inodes.

server4 `/home`: 105638092800 available bytes; 94.11% used; 114350361 free inodes.

server4 `/data`: 249110622208 available bytes; 96.56% used; 225015189 free inodes.

server4 `/tmp`: 105638092800 available bytes; 94.11% used; 114350361 free inodes.

server4 `/var/tmp`: 105638092800 available bytes; 94.11% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
