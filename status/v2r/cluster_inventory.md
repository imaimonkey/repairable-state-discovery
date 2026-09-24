# V2R cluster inventory

2026-09-24T07:59:03.611460+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324413165568 available bytes; 81.90% used; 112490776 free inodes.

server1 `/home`: 324413165568 available bytes; 81.90% used; 112490776 free inodes.

server1 `/tmp`: 324413165568 available bytes; 81.90% used; 112490776 free inodes.

server1 `/var/tmp`: 324413165568 available bytes; 81.90% used; 112490776 free inodes.

server1 `/mnt/raid5`: 483195404288 available bytes; 97.78% used; 337722149 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57828044800 available bytes; 96.77% used; 110431076 free inodes.

server2 `/home`: 57828044800 available bytes; 96.77% used; 110431076 free inodes.

server2 `/tmp`: 57828044800 available bytes; 96.77% used; 110431076 free inodes.

server2 `/var/tmp`: 57828044800 available bytes; 96.77% used; 110431076 free inodes.

server2 `/mnt/raid5`: 517403844608 available bytes; 96.42% used; 445180705 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85485219840 available bytes; 95.23% used; 114175163 free inodes.

server3 `/home`: 85485219840 available bytes; 95.23% used; 114175163 free inodes.

server3 `/data`: 177846845440 available bytes; 97.54% used; 225838947 free inodes.

server3 `/tmp`: 85485219840 available bytes; 95.23% used; 114175163 free inodes.

server3 `/var/tmp`: 85485219840 available bytes; 95.23% used; 114175163 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779339264 available bytes; 94.10% used; 114349165 free inodes.

server4 `/home`: 105779339264 available bytes; 94.10% used; 114349165 free inodes.

server4 `/data`: 284244860928 available bytes; 96.07% used; 225366060 free inodes.

server4 `/tmp`: 105779339264 available bytes; 94.10% used; 114349165 free inodes.

server4 `/var/tmp`: 105779339264 available bytes; 94.10% used; 114349165 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
