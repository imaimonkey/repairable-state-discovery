# V2R cluster inventory

2026-09-24T16:34:46.024560+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324024086528 available bytes; 81.92% used; 112481456 free inodes.

server1 `/home`: 324024086528 available bytes; 81.92% used; 112481456 free inodes.

server1 `/tmp`: 324024086528 available bytes; 81.92% used; 112481456 free inodes.

server1 `/var/tmp`: 324024086528 available bytes; 81.92% used; 112481456 free inodes.

server1 `/mnt/raid5`: 416566603776 available bytes; 98.09% used; 337652833 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57317015552 available bytes; 96.80% used; 110426840 free inodes.

server2 `/home`: 57317015552 available bytes; 96.80% used; 110426840 free inodes.

server2 `/tmp`: 57317015552 available bytes; 96.80% used; 110426840 free inodes.

server2 `/var/tmp`: 57317015552 available bytes; 96.80% used; 110426840 free inodes.

server2 `/mnt/raid5`: 500796399616 available bytes; 96.54% used; 445164293 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83943288832 available bytes; 95.32% used; 114128460 free inodes.

server3 `/home`: 83943288832 available bytes; 95.32% used; 114128460 free inodes.

server3 `/data`: 159324344320 available bytes; 97.80% used; 225787951 free inodes.

server3 `/tmp`: 83943288832 available bytes; 95.32% used; 114128460 free inodes.

server3 `/var/tmp`: 83943288832 available bytes; 95.32% used; 114128460 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105688489984 available bytes; 94.10% used; 114348593 free inodes.

server4 `/home`: 105688489984 available bytes; 94.10% used; 114348593 free inodes.

server4 `/data`: 89277644800 available bytes; 98.77% used; 225255738 free inodes.

server4 `/tmp`: 105688489984 available bytes; 94.10% used; 114348593 free inodes.

server4 `/var/tmp`: 105688489984 available bytes; 94.10% used; 114348593 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
