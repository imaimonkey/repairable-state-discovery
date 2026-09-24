# V2R cluster inventory

2026-09-24T09:49:27.413631+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324446609408 available bytes; 81.90% used; 112489638 free inodes.

server1 `/home`: 324446609408 available bytes; 81.90% used; 112489638 free inodes.

server1 `/tmp`: 324446609408 available bytes; 81.90% used; 112489638 free inodes.

server1 `/var/tmp`: 324446609408 available bytes; 81.90% used; 112489638 free inodes.

server1 `/mnt/raid5`: 500741124096 available bytes; 97.70% used; 337702655 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57754103808 available bytes; 96.78% used; 110430765 free inodes.

server2 `/home`: 57754103808 available bytes; 96.78% used; 110430765 free inodes.

server2 `/tmp`: 57754103808 available bytes; 96.78% used; 110430765 free inodes.

server2 `/var/tmp`: 57754103808 available bytes; 96.78% used; 110430765 free inodes.

server2 `/mnt/raid5`: 514029084672 available bytes; 96.45% used; 445177462 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85832155136 available bytes; 95.21% used; 114199375 free inodes.

server3 `/home`: 85832155136 available bytes; 95.21% used; 114199375 free inodes.

server3 `/data`: 165640212480 available bytes; 97.71% used; 225819822 free inodes.

server3 `/tmp`: 85832155136 available bytes; 95.21% used; 114199375 free inodes.

server3 `/var/tmp`: 85832155136 available bytes; 95.21% used; 114199375 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748537344 available bytes; 94.10% used; 114349035 free inodes.

server4 `/home`: 105748537344 available bytes; 94.10% used; 114349035 free inodes.

server4 `/data`: 154557538304 available bytes; 97.86% used; 225273217 free inodes.

server4 `/tmp`: 105748537344 available bytes; 94.10% used; 114349035 free inodes.

server4 `/var/tmp`: 105748537344 available bytes; 94.10% used; 114349035 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
