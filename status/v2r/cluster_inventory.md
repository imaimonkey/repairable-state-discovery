# V2R cluster inventory

2026-09-24T11:37:01.521333+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324345929728 available bytes; 81.91% used; 112488840 free inodes.

server1 `/home`: 324345929728 available bytes; 81.91% used; 112488840 free inodes.

server1 `/tmp`: 324345929728 available bytes; 81.91% used; 112488840 free inodes.

server1 `/var/tmp`: 324345929728 available bytes; 81.91% used; 112488840 free inodes.

server1 `/mnt/raid5`: 436764385280 available bytes; 98.00% used; 337688629 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57659523072 available bytes; 96.78% used; 110429936 free inodes.

server2 `/home`: 57659523072 available bytes; 96.78% used; 110429936 free inodes.

server2 `/tmp`: 57659523072 available bytes; 96.78% used; 110429936 free inodes.

server2 `/var/tmp`: 57659523072 available bytes; 96.78% used; 110429936 free inodes.

server2 `/mnt/raid5`: 510423224320 available bytes; 96.47% used; 445173263 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85347848192 available bytes; 95.24% used; 114173485 free inodes.

server3 `/home`: 85347848192 available bytes; 95.24% used; 114173485 free inodes.

server3 `/data`: 163745697792 available bytes; 97.74% used; 225816500 free inodes.

server3 `/tmp`: 85347848192 available bytes; 95.24% used; 114173485 free inodes.

server3 `/var/tmp`: 85347848192 available bytes; 95.24% used; 114173485 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105730666496 available bytes; 94.10% used; 114348873 free inodes.

server4 `/home`: 105730666496 available bytes; 94.10% used; 114348873 free inodes.

server4 `/data`: 115439804416 available bytes; 98.40% used; 225258024 free inodes.

server4 `/tmp`: 105730666496 available bytes; 94.10% used; 114348873 free inodes.

server4 `/var/tmp`: 105730666496 available bytes; 94.10% used; 114348873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
