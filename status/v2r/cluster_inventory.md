# V2R cluster inventory

2026-09-24T21:14:18.086304+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323971276800 available bytes; 81.93% used; 112481421 free inodes.

server1 `/home`: 323971276800 available bytes; 81.93% used; 112481421 free inodes.

server1 `/tmp`: 323971276800 available bytes; 81.93% used; 112481421 free inodes.

server1 `/var/tmp`: 323971276800 available bytes; 81.93% used; 112481421 free inodes.

server1 `/mnt/raid5`: 394891702272 available bytes; 98.19% used; 337629311 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30135279616 available bytes; 98.32% used; 110411372 free inodes.

server2 `/home`: 30135279616 available bytes; 98.32% used; 110411372 free inodes.

server2 `/tmp`: 30135279616 available bytes; 98.32% used; 110411372 free inodes.

server2 `/var/tmp`: 30135279616 available bytes; 98.32% used; 110411372 free inodes.

server2 `/mnt/raid5`: 490899312640 available bytes; 96.61% used; 445155493 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84384174080 available bytes; 95.29% used; 114156097 free inodes.

server3 `/home`: 84384174080 available bytes; 95.29% used; 114156097 free inodes.

server3 `/data`: 150632382464 available bytes; 97.92% used; 225803496 free inodes.

server3 `/tmp`: 84384174080 available bytes; 95.29% used; 114156097 free inodes.

server3 `/var/tmp`: 84384174080 available bytes; 95.29% used; 114156097 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632731136 available bytes; 94.11% used; 114348357 free inodes.

server4 `/home`: 105632731136 available bytes; 94.11% used; 114348357 free inodes.

server4 `/data`: 72486707200 available bytes; 99.00% used; 225253797 free inodes.

server4 `/tmp`: 105632731136 available bytes; 94.11% used; 114348357 free inodes.

server4 `/var/tmp`: 105632731136 available bytes; 94.11% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
