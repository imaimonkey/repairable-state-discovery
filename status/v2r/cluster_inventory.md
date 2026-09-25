# V2R cluster inventory

2026-09-25T01:16:32.343959+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319078760448 available bytes; 82.20% used; 112480772 free inodes.

server1 `/home`: 319078760448 available bytes; 82.20% used; 112480772 free inodes.

server1 `/tmp`: 319078760448 available bytes; 82.20% used; 112480772 free inodes.

server1 `/var/tmp`: 319078760448 available bytes; 82.20% used; 112480772 free inodes.

server1 `/mnt/raid5`: 416516063232 available bytes; 98.09% used; 337614539 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23059107840 available bytes; 98.71% used; 110410770 free inodes.

server2 `/home`: 23059107840 available bytes; 98.71% used; 110410770 free inodes.

server2 `/tmp`: 23059107840 available bytes; 98.71% used; 110410770 free inodes.

server2 `/var/tmp`: 23059107840 available bytes; 98.71% used; 110410770 free inodes.

server2 `/mnt/raid5`: 497976139776 available bytes; 96.56% used; 445161748 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84358164480 available bytes; 95.29% used; 114156089 free inodes.

server3 `/home`: 84358164480 available bytes; 95.29% used; 114156089 free inodes.

server3 `/data`: 146922196992 available bytes; 97.97% used; 225812577 free inodes.

server3 `/tmp`: 84358164480 available bytes; 95.29% used; 114156089 free inodes.

server3 `/var/tmp`: 84358164480 available bytes; 95.29% used; 114156089 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105779294208 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105779294208 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 53326032896 available bytes; 99.26% used; 225030751 free inodes.

server4 `/tmp`: 105779294208 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105779294208 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
