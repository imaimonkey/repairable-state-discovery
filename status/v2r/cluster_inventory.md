# V2R cluster inventory

2026-09-25T07:32:11.089928+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318869348352 available bytes; 82.21% used; 112480370 free inodes.

server1 `/home`: 318869348352 available bytes; 82.21% used; 112480370 free inodes.

server1 `/tmp`: 318869348352 available bytes; 82.21% used; 112480370 free inodes.

server1 `/var/tmp`: 318869348352 available bytes; 82.21% used; 112480370 free inodes.

server1 `/mnt/raid5`: 385877098496 available bytes; 98.23% used; 337558395 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22860292096 available bytes; 98.72% used; 110410499 free inodes.

server2 `/home`: 22860292096 available bytes; 98.72% used; 110410499 free inodes.

server2 `/tmp`: 22860292096 available bytes; 98.72% used; 110410499 free inodes.

server2 `/var/tmp`: 22860292096 available bytes; 98.72% used; 110410499 free inodes.

server2 `/mnt/raid5`: 343146942464 available bytes; 97.63% used; 445097184 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84445184000 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84445184000 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142397059072 available bytes; 98.03% used; 225812664 free inodes.

server3 `/tmp`: 84445184000 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84445184000 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637773312 available bytes; 94.11% used; 114350353 free inodes.

server4 `/home`: 105637773312 available bytes; 94.11% used; 114350353 free inodes.

server4 `/data`: 249090199552 available bytes; 96.56% used; 225014058 free inodes.

server4 `/tmp`: 105637773312 available bytes; 94.11% used; 114350353 free inodes.

server4 `/var/tmp`: 105637773312 available bytes; 94.11% used; 114350353 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
