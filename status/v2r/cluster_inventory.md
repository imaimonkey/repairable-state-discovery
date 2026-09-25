# V2R cluster inventory

2026-09-25T08:10:35.822046+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318840623104 available bytes; 82.21% used; 112480355 free inodes.

server1 `/home`: 318840623104 available bytes; 82.21% used; 112480355 free inodes.

server1 `/tmp`: 318840623104 available bytes; 82.21% used; 112480355 free inodes.

server1 `/var/tmp`: 318840623104 available bytes; 82.21% used; 112480355 free inodes.

server1 `/mnt/raid5`: 380966498304 available bytes; 98.25% used; 337557660 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22842355712 available bytes; 98.73% used; 110410483 free inodes.

server2 `/home`: 22842355712 available bytes; 98.73% used; 110410483 free inodes.

server2 `/tmp`: 22842355712 available bytes; 98.73% used; 110410483 free inodes.

server2 `/var/tmp`: 22842355712 available bytes; 98.73% used; 110410483 free inodes.

server2 `/mnt/raid5`: 333874638848 available bytes; 97.69% used; 445094821 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436594688 available bytes; 95.29% used; 114156049 free inodes.

server3 `/home`: 84436594688 available bytes; 95.29% used; 114156049 free inodes.

server3 `/data`: 142387593216 available bytes; 98.03% used; 225812031 free inodes.

server3 `/tmp`: 84436594688 available bytes; 95.29% used; 114156049 free inodes.

server3 `/var/tmp`: 84436594688 available bytes; 95.29% used; 114156049 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105625227264 available bytes; 94.11% used; 114350335 free inodes.

server4 `/home`: 105625227264 available bytes; 94.11% used; 114350335 free inodes.

server4 `/data`: 249012412416 available bytes; 96.56% used; 225008263 free inodes.

server4 `/tmp`: 105625227264 available bytes; 94.11% used; 114350335 free inodes.

server4 `/var/tmp`: 105625227264 available bytes; 94.11% used; 114350335 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
