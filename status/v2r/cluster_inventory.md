# V2R cluster inventory

2026-09-26T09:39:16.492138+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318617989120 available bytes; 82.23% used; 112475085 free inodes.

server1 `/home`: 318617989120 available bytes; 82.23% used; 112475085 free inodes.

server1 `/tmp`: 318617989120 available bytes; 82.23% used; 112475085 free inodes.

server1 `/var/tmp`: 318617989120 available bytes; 82.23% used; 112475085 free inodes.

server1 `/mnt/raid5`: 218945880064 available bytes; 99.00% used; 337538598 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22317719552 available bytes; 98.75% used; 110403896 free inodes.

server2 `/home`: 22317719552 available bytes; 98.75% used; 110403896 free inodes.

server2 `/tmp`: 22317719552 available bytes; 98.75% used; 110403896 free inodes.

server2 `/var/tmp`: 22317719552 available bytes; 98.75% used; 110403896 free inodes.

server2 `/mnt/raid5`: 253919809536 available bytes; 98.25% used; 445022488 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82655907840 available bytes; 95.39% used; 114110791 free inodes.

server3 `/home`: 82655907840 available bytes; 95.39% used; 114110791 free inodes.

server3 `/data`: 123594264576 available bytes; 98.29% used; 225827631 free inodes.

server3 `/tmp`: 82655907840 available bytes; 95.39% used; 114110791 free inodes.

server3 `/var/tmp`: 82655907840 available bytes; 95.39% used; 114110791 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105934127104 available bytes; 94.09% used; 114348049 free inodes.

server4 `/home`: 105934127104 available bytes; 94.09% used; 114348049 free inodes.

server4 `/data`: 89281003520 available bytes; 98.77% used; 224882608 free inodes.

server4 `/tmp`: 105934127104 available bytes; 94.09% used; 114348049 free inodes.

server4 `/var/tmp`: 105934127104 available bytes; 94.09% used; 114348049 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
