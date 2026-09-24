# V2R cluster inventory

2026-09-24T11:00:53.113716+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324376428544 available bytes; 81.90% used; 112489034 free inodes.

server1 `/home`: 324376428544 available bytes; 81.90% used; 112489034 free inodes.

server1 `/tmp`: 324376428544 available bytes; 81.90% used; 112489034 free inodes.

server1 `/var/tmp`: 324376428544 available bytes; 81.90% used; 112489034 free inodes.

server1 `/mnt/raid5`: 489593389056 available bytes; 97.75% used; 337693382 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57697484800 available bytes; 96.78% used; 110430285 free inodes.

server2 `/home`: 57697484800 available bytes; 96.78% used; 110430285 free inodes.

server2 `/tmp`: 57697484800 available bytes; 96.78% used; 110430285 free inodes.

server2 `/var/tmp`: 57697484800 available bytes; 96.78% used; 110430285 free inodes.

server2 `/mnt/raid5`: 511813169152 available bytes; 96.46% used; 445174414 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85770158080 available bytes; 95.21% used; 114196637 free inodes.

server3 `/home`: 85770158080 available bytes; 95.21% used; 114196637 free inodes.

server3 `/data`: 164014678016 available bytes; 97.73% used; 225817586 free inodes.

server3 `/tmp`: 85770158080 available bytes; 95.21% used; 114196637 free inodes.

server3 `/var/tmp`: 85770158080 available bytes; 95.21% used; 114196637 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105734676480 available bytes; 94.10% used; 114348930 free inodes.

server4 `/home`: 105734676480 available bytes; 94.10% used; 114348930 free inodes.

server4 `/data`: 132774875136 available bytes; 98.16% used; 225258252 free inodes.

server4 `/tmp`: 105734676480 available bytes; 94.10% used; 114348930 free inodes.

server4 `/var/tmp`: 105734676480 available bytes; 94.10% used; 114348930 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
