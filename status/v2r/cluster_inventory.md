# V2R cluster inventory

2026-09-25T04:35:11.874078+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318929199104 available bytes; 82.21% used; 112480382 free inodes.

server1 `/home`: 318929199104 available bytes; 82.21% used; 112480382 free inodes.

server1 `/tmp`: 318929199104 available bytes; 82.21% used; 112480382 free inodes.

server1 `/var/tmp`: 318929199104 available bytes; 82.21% used; 112480382 free inodes.

server1 `/mnt/raid5`: 408724017152 available bytes; 98.13% used; 337591098 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22946988032 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22946988032 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22946988032 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22946988032 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462875250688 available bytes; 96.80% used; 445109772 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340527104 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84340527104 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143427768320 available bytes; 98.02% used; 225816043 free inodes.

server3 `/tmp`: 84340527104 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84340527104 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105667764224 available bytes; 94.10% used; 114350744 free inodes.

server4 `/home`: 105667764224 available bytes; 94.10% used; 114350744 free inodes.

server4 `/data`: 32787816448 available bytes; 99.55% used; 224962697 free inodes.

server4 `/tmp`: 105667764224 available bytes; 94.10% used; 114350744 free inodes.

server4 `/var/tmp`: 105667764224 available bytes; 94.10% used; 114350744 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
