# V2R cluster inventory

2026-09-24T05:13:18.053199+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324593258496 available bytes; 81.89% used; 112492554 free inodes.

server1 `/home`: 324593258496 available bytes; 81.89% used; 112492554 free inodes.

server1 `/tmp`: 324593258496 available bytes; 81.89% used; 112492554 free inodes.

server1 `/var/tmp`: 324593258496 available bytes; 81.89% used; 112492554 free inodes.

server1 `/mnt/raid5`: 497796956160 available bytes; 97.72% used; 337724539 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40748920832 available bytes; 97.73% used; 110430362 free inodes.

server2 `/home`: 40748920832 available bytes; 97.73% used; 110430362 free inodes.

server2 `/tmp`: 40748920832 available bytes; 97.73% used; 110430362 free inodes.

server2 `/var/tmp`: 40748920832 available bytes; 97.73% used; 110430362 free inodes.

server2 `/mnt/raid5`: 522903322624 available bytes; 96.39% used; 445194420 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 291745083392 available bytes; 83.72% used; 114167336 free inodes.

server3 `/home`: 291745083392 available bytes; 83.72% used; 114167336 free inodes.

server3 `/data`: 23280607232 available bytes; 99.68% used; 225840201 free inodes.

server3 `/tmp`: 291745083392 available bytes; 83.72% used; 114167336 free inodes.

server3 `/var/tmp`: 291745083392 available bytes; 83.72% used; 114167336 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105826353152 available bytes; 94.09% used; 114349379 free inodes.

server4 `/home`: 105826353152 available bytes; 94.09% used; 114349379 free inodes.

server4 `/data`: 252594446336 available bytes; 96.51% used; 225366776 free inodes.

server4 `/tmp`: 105826353152 available bytes; 94.09% used; 114349379 free inodes.

server4 `/var/tmp`: 105826353152 available bytes; 94.09% used; 114349379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
