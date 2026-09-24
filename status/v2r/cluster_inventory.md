# V2R cluster inventory

2026-09-24T08:19:17.044351+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324405288960 available bytes; 81.90% used; 112490569 free inodes.

server1 `/home`: 324405288960 available bytes; 81.90% used; 112490569 free inodes.

server1 `/tmp`: 324405288960 available bytes; 81.90% used; 112490569 free inodes.

server1 `/var/tmp`: 324405288960 available bytes; 81.90% used; 112490569 free inodes.

server1 `/mnt/raid5`: 510287126528 available bytes; 97.66% used; 337721319 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57816641536 available bytes; 96.77% used; 110431026 free inodes.

server2 `/home`: 57816641536 available bytes; 96.77% used; 110431026 free inodes.

server2 `/tmp`: 57816641536 available bytes; 96.77% used; 110431026 free inodes.

server2 `/var/tmp`: 57816641536 available bytes; 96.77% used; 110431026 free inodes.

server2 `/mnt/raid5`: 516489404416 available bytes; 96.43% used; 445179950 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85901271040 available bytes; 95.21% used; 114200261 free inodes.

server3 `/home`: 85901271040 available bytes; 95.21% used; 114200261 free inodes.

server3 `/data`: 175153680384 available bytes; 97.58% used; 225823200 free inodes.

server3 `/tmp`: 85901271040 available bytes; 95.21% used; 114200261 free inodes.

server3 `/var/tmp`: 85901271040 available bytes; 95.21% used; 114200261 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778335744 available bytes; 94.10% used; 114349149 free inodes.

server4 `/home`: 105778335744 available bytes; 94.10% used; 114349149 free inodes.

server4 `/data`: 280475979776 available bytes; 96.12% used; 225350826 free inodes.

server4 `/tmp`: 105778335744 available bytes; 94.10% used; 114349149 free inodes.

server4 `/var/tmp`: 105778335744 available bytes; 94.10% used; 114349149 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
