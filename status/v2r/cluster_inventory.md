# V2R cluster inventory

2026-09-25T04:39:51.869819+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318915104768 available bytes; 82.21% used; 112480370 free inodes.

server1 `/home`: 318915104768 available bytes; 82.21% used; 112480370 free inodes.

server1 `/tmp`: 318915104768 available bytes; 82.21% used; 112480370 free inodes.

server1 `/var/tmp`: 318915104768 available bytes; 82.21% used; 112480370 free inodes.

server1 `/mnt/raid5`: 408702668800 available bytes; 98.13% used; 337590517 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22946783232 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22946783232 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22946783232 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22946783232 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462727897088 available bytes; 96.80% used; 445109620 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340830208 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84340830208 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 143350689792 available bytes; 98.02% used; 225815968 free inodes.

server3 `/tmp`: 84340830208 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84340830208 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105664114688 available bytes; 94.10% used; 114350617 free inodes.

server4 `/home`: 105664114688 available bytes; 94.10% used; 114350617 free inodes.

server4 `/data`: 31178014720 available bytes; 99.57% used; 224962428 free inodes.

server4 `/tmp`: 105664114688 available bytes; 94.10% used; 114350617 free inodes.

server4 `/var/tmp`: 105664114688 available bytes; 94.10% used; 114350617 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
