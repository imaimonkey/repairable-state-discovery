# V2R cluster inventory

2026-09-25T03:05:15.007671+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318941822976 available bytes; 82.21% used; 112480388 free inodes.

server1 `/home`: 318941822976 available bytes; 82.21% used; 112480388 free inodes.

server1 `/tmp`: 318941822976 available bytes; 82.21% used; 112480388 free inodes.

server1 `/var/tmp`: 318941822976 available bytes; 82.21% used; 112480388 free inodes.

server1 `/mnt/raid5`: 416136163328 available bytes; 98.09% used; 337601827 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22999506944 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 22999506944 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 22999506944 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 22999506944 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 465955409920 available bytes; 96.78% used; 445112780 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84344971264 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84344971264 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144934019072 available bytes; 98.00% used; 225810375 free inodes.

server3 `/tmp`: 84344971264 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84344971264 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105693118464 available bytes; 94.10% used; 114350903 free inodes.

server4 `/home`: 105693118464 available bytes; 94.10% used; 114350903 free inodes.

server4 `/data`: 50260643840 available bytes; 99.31% used; 224967432 free inodes.

server4 `/tmp`: 105693118464 available bytes; 94.10% used; 114350903 free inodes.

server4 `/var/tmp`: 105693118464 available bytes; 94.10% used; 114350903 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
