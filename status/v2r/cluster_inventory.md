# V2R cluster inventory

2026-09-25T04:55:14.003694+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318906142720 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318906142720 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318906142720 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318906142720 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 408662253568 available bytes; 98.13% used; 337588623 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939193344 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22939193344 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22939193344 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22939193344 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462258221056 available bytes; 96.81% used; 445109031 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84344377344 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84344377344 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143043457024 available bytes; 98.02% used; 225815643 free inodes.

server3 `/tmp`: 84344377344 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84344377344 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105659527168 available bytes; 94.10% used; 114350406 free inodes.

server4 `/home`: 105659527168 available bytes; 94.10% used; 114350406 free inodes.

server4 `/data`: 27943022592 available bytes; 99.61% used; 224961511 free inodes.

server4 `/tmp`: 105659527168 available bytes; 94.10% used; 114350406 free inodes.

server4 `/var/tmp`: 105659527168 available bytes; 94.10% used; 114350406 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
