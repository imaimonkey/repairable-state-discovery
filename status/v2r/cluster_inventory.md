# V2R cluster inventory

2026-09-25T02:27:20.962195+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318969401344 available bytes; 82.21% used; 112480501 free inodes.

server1 `/home`: 318969401344 available bytes; 82.21% used; 112480501 free inodes.

server1 `/tmp`: 318969401344 available bytes; 82.21% used; 112480501 free inodes.

server1 `/var/tmp`: 318969401344 available bytes; 82.21% used; 112480501 free inodes.

server1 `/mnt/raid5`: 416222216192 available bytes; 98.09% used; 337606262 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23017541632 available bytes; 98.72% used; 110410439 free inodes.

server2 `/home`: 23017541632 available bytes; 98.72% used; 110410439 free inodes.

server2 `/tmp`: 23017541632 available bytes; 98.72% used; 110410439 free inodes.

server2 `/var/tmp`: 23017541632 available bytes; 98.72% used; 110410439 free inodes.

server2 `/mnt/raid5`: 483502395392 available bytes; 96.66% used; 445113822 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351856640 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84351856640 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145648787456 available bytes; 97.99% used; 225811109 free inodes.

server3 `/tmp`: 84351856640 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84351856640 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['1', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105895931904 available bytes; 94.09% used; 114350978 free inodes.

server4 `/home`: 105895931904 available bytes; 94.09% used; 114350978 free inodes.

server4 `/data`: 27682455552 available bytes; 99.62% used; 224969566 free inodes.

server4 `/tmp`: 105895931904 available bytes; 94.09% used; 114350978 free inodes.

server4 `/var/tmp`: 105895931904 available bytes; 94.09% used; 114350978 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
