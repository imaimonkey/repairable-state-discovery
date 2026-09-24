# V2R cluster inventory

2026-09-24T05:38:55.738830+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324531818496 available bytes; 81.90% used; 112492178 free inodes.

server1 `/home`: 324531818496 available bytes; 81.90% used; 112492178 free inodes.

server1 `/tmp`: 324531818496 available bytes; 81.90% used; 112492178 free inodes.

server1 `/var/tmp`: 324531818496 available bytes; 81.90% used; 112492178 free inodes.

server1 `/mnt/raid5`: 517631614976 available bytes; 97.63% used; 337723984 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57915265024 available bytes; 96.77% used; 110431346 free inodes.

server2 `/home`: 57915265024 available bytes; 96.77% used; 110431346 free inodes.

server2 `/tmp`: 57915265024 available bytes; 96.77% used; 110431346 free inodes.

server2 `/var/tmp`: 57915265024 available bytes; 96.77% used; 110431346 free inodes.

server2 `/mnt/raid5`: 522102587392 available bytes; 96.39% used; 445193746 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126801948672 available bytes; 92.92% used; 114175412 free inodes.

server3 `/home`: 126801948672 available bytes; 92.92% used; 114175412 free inodes.

server3 `/data`: 185259405312 available bytes; 97.44% used; 225839214 free inodes.

server3 `/tmp`: 126801948672 available bytes; 92.92% used; 114175412 free inodes.

server3 `/var/tmp`: 126801948672 available bytes; 92.92% used; 114175412 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816567808 available bytes; 94.10% used; 114349357 free inodes.

server4 `/home`: 105816567808 available bytes; 94.10% used; 114349357 free inodes.

server4 `/data`: 251506565120 available bytes; 96.52% used; 225358056 free inodes.

server4 `/tmp`: 105816567808 available bytes; 94.10% used; 114349357 free inodes.

server4 `/var/tmp`: 105816567808 available bytes; 94.10% used; 114349357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
