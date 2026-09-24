# V2R cluster inventory

2026-09-24T05:54:41.814386+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324526731264 available bytes; 81.90% used; 112492010 free inodes.

server1 `/home`: 324526731264 available bytes; 81.90% used; 112492010 free inodes.

server1 `/tmp`: 324526731264 available bytes; 81.90% used; 112492010 free inodes.

server1 `/var/tmp`: 324526731264 available bytes; 81.90% used; 112492010 free inodes.

server1 `/mnt/raid5`: 517609459712 available bytes; 97.63% used; 337723872 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57905680384 available bytes; 96.77% used; 110431308 free inodes.

server2 `/home`: 57905680384 available bytes; 96.77% used; 110431308 free inodes.

server2 `/tmp`: 57905680384 available bytes; 96.77% used; 110431308 free inodes.

server2 `/var/tmp`: 57905680384 available bytes; 96.77% used; 110431308 free inodes.

server2 `/mnt/raid5`: 521624252416 available bytes; 96.40% used; 445193133 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127206481920 available bytes; 92.90% used; 114198523 free inodes.

server3 `/home`: 127206481920 available bytes; 92.90% used; 114198523 free inodes.

server3 `/data`: 185873211392 available bytes; 97.43% used; 225838596 free inodes.

server3 `/tmp`: 127206481920 available bytes; 92.90% used; 114198523 free inodes.

server3 `/var/tmp`: 127206481920 available bytes; 92.90% used; 114198523 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105815810048 available bytes; 94.10% used; 114349341 free inodes.

server4 `/home`: 105815810048 available bytes; 94.10% used; 114349341 free inodes.

server4 `/data`: 252140961792 available bytes; 96.52% used; 225357916 free inodes.

server4 `/tmp`: 105815810048 available bytes; 94.10% used; 114349341 free inodes.

server4 `/var/tmp`: 105815810048 available bytes; 94.10% used; 114349341 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
