# V2R cluster inventory

2026-09-24T14:34:54.474208+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324052094976 available bytes; 81.92% used; 112481461 free inodes.

server1 `/home`: 324052094976 available bytes; 81.92% used; 112481461 free inodes.

server1 `/tmp`: 324052094976 available bytes; 81.92% used; 112481461 free inodes.

server1 `/var/tmp`: 324052094976 available bytes; 81.92% used; 112481461 free inodes.

server1 `/mnt/raid5`: 416883085312 available bytes; 98.09% used; 337667644 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57451999232 available bytes; 96.79% used; 110428050 free inodes.

server2 `/home`: 57451999232 available bytes; 96.79% used; 110428050 free inodes.

server2 `/tmp`: 57451999232 available bytes; 96.79% used; 110428050 free inodes.

server2 `/var/tmp`: 57451999232 available bytes; 96.79% used; 110428050 free inodes.

server2 `/mnt/raid5`: 504326103040 available bytes; 96.52% used; 445167674 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84483776512 available bytes; 95.29% used; 114158860 free inodes.

server3 `/home`: 84483776512 available bytes; 95.29% used; 114158860 free inodes.

server3 `/data`: 160853200896 available bytes; 97.78% used; 225808071 free inodes.

server3 `/tmp`: 84483776512 available bytes; 95.29% used; 114158860 free inodes.

server3 `/var/tmp`: 84483776512 available bytes; 95.29% used; 114158860 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105758724096 available bytes; 94.10% used; 114348687 free inodes.

server4 `/home`: 105758724096 available bytes; 94.10% used; 114348687 free inodes.

server4 `/data`: 69178400768 available bytes; 99.04% used; 225257007 free inodes.

server4 `/tmp`: 105758724096 available bytes; 94.10% used; 114348687 free inodes.

server4 `/var/tmp`: 105758724096 available bytes; 94.10% used; 114348687 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
