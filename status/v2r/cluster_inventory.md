# V2R cluster inventory

2026-09-24T16:37:51.206209+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026908672 available bytes; 81.92% used; 112481458 free inodes.

server1 `/home`: 324026908672 available bytes; 81.92% used; 112481458 free inodes.

server1 `/tmp`: 324026908672 available bytes; 81.92% used; 112481458 free inodes.

server1 `/var/tmp`: 324026908672 available bytes; 81.92% used; 112481458 free inodes.

server1 `/mnt/raid5`: 416561246208 available bytes; 98.09% used; 337652478 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57314349056 available bytes; 96.80% used; 110426808 free inodes.

server2 `/home`: 57314349056 available bytes; 96.80% used; 110426808 free inodes.

server2 `/tmp`: 57314349056 available bytes; 96.80% used; 110426808 free inodes.

server2 `/var/tmp`: 57314349056 available bytes; 96.80% used; 110426808 free inodes.

server2 `/mnt/raid5`: 500713058304 available bytes; 96.54% used; 445164322 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83509366784 available bytes; 95.34% used; 114101342 free inodes.

server3 `/home`: 83509366784 available bytes; 95.34% used; 114101342 free inodes.

server3 `/data`: 159298797568 available bytes; 97.80% used; 225787524 free inodes.

server3 `/tmp`: 83509366784 available bytes; 95.34% used; 114101342 free inodes.

server3 `/var/tmp`: 83509366784 available bytes; 95.34% used; 114101342 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105683251200 available bytes; 94.10% used; 114348574 free inodes.

server4 `/home`: 105683251200 available bytes; 94.10% used; 114348574 free inodes.

server4 `/data`: 89272066048 available bytes; 98.77% used; 225255638 free inodes.

server4 `/tmp`: 105683251200 available bytes; 94.10% used; 114348574 free inodes.

server4 `/var/tmp`: 105683251200 available bytes; 94.10% used; 114348574 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
