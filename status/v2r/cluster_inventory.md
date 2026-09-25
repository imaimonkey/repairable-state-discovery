# V2R cluster inventory

2026-09-25T08:30:36.860407+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318825865216 available bytes; 82.21% used; 112480369 free inodes.

server1 `/home`: 318825865216 available bytes; 82.21% used; 112480369 free inodes.

server1 `/tmp`: 318825865216 available bytes; 82.21% used; 112480369 free inodes.

server1 `/var/tmp`: 318825865216 available bytes; 82.21% used; 112480369 free inodes.

server1 `/mnt/raid5`: 364230594560 available bytes; 98.33% used; 337557098 free inodes.
| server2 | True | ['5', '6'] | [] |

server2 `/`: 22841810944 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22841810944 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22841810944 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22841810944 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 333258313728 available bytes; 97.70% used; 445094463 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436606976 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84436606976 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142380789760 available bytes; 98.03% used; 225811659 free inodes.

server3 `/tmp`: 84436606976 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84436606976 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105634136064 available bytes; 94.11% used; 114350327 free inodes.

server4 `/home`: 105634136064 available bytes; 94.11% used; 114350327 free inodes.

server4 `/data`: 246713331712 available bytes; 96.59% used; 225004244 free inodes.

server4 `/tmp`: 105634136064 available bytes; 94.11% used; 114350327 free inodes.

server4 `/var/tmp`: 105634136064 available bytes; 94.11% used; 114350327 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
