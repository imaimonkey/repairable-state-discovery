# V2R cluster inventory

2026-09-24T11:43:22.110950+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324349255680 available bytes; 81.91% used; 112488830 free inodes.

server1 `/home`: 324349255680 available bytes; 81.91% used; 112488830 free inodes.

server1 `/tmp`: 324349255680 available bytes; 81.91% used; 112488830 free inodes.

server1 `/var/tmp`: 324349255680 available bytes; 81.91% used; 112488830 free inodes.

server1 `/mnt/raid5`: 429943296000 available bytes; 98.03% used; 337687836 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57653481472 available bytes; 96.78% used; 110429872 free inodes.

server2 `/home`: 57653481472 available bytes; 96.78% used; 110429872 free inodes.

server2 `/tmp`: 57653481472 available bytes; 96.78% used; 110429872 free inodes.

server2 `/var/tmp`: 57653481472 available bytes; 96.78% used; 110429872 free inodes.

server2 `/mnt/raid5`: 510225477632 available bytes; 96.47% used; 445173052 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85248557056 available bytes; 95.24% used; 114166924 free inodes.

server3 `/home`: 85248557056 available bytes; 95.24% used; 114166924 free inodes.

server3 `/data`: 163703275520 available bytes; 97.74% used; 225816011 free inodes.

server3 `/tmp`: 85248557056 available bytes; 95.24% used; 114166924 free inodes.

server3 `/var/tmp`: 85248557056 available bytes; 95.24% used; 114166924 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105729728512 available bytes; 94.10% used; 114348863 free inodes.

server4 `/home`: 105729728512 available bytes; 94.10% used; 114348863 free inodes.

server4 `/data`: 115394019328 available bytes; 98.41% used; 225257975 free inodes.

server4 `/tmp`: 105729728512 available bytes; 94.10% used; 114348863 free inodes.

server4 `/var/tmp`: 105729728512 available bytes; 94.10% used; 114348863 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
