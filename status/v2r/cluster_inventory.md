# V2R cluster inventory

2026-09-24T11:33:52.846978+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324346830848 available bytes; 81.91% used; 112488843 free inodes.

server1 `/home`: 324346830848 available bytes; 81.91% used; 112488843 free inodes.

server1 `/tmp`: 324346830848 available bytes; 81.91% used; 112488843 free inodes.

server1 `/var/tmp`: 324346830848 available bytes; 81.91% used; 112488843 free inodes.

server1 `/mnt/raid5`: 440722259968 available bytes; 97.98% used; 337689017 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57661267968 available bytes; 96.78% used; 110429962 free inodes.

server2 `/home`: 57661267968 available bytes; 96.78% used; 110429962 free inodes.

server2 `/tmp`: 57661267968 available bytes; 96.78% used; 110429962 free inodes.

server2 `/var/tmp`: 57661267968 available bytes; 96.78% used; 110429962 free inodes.

server2 `/mnt/raid5`: 510522843136 available bytes; 96.47% used; 445173473 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85770252288 available bytes; 95.21% used; 114198913 free inodes.

server3 `/home`: 85770252288 available bytes; 95.21% used; 114198913 free inodes.

server3 `/data`: 163772583936 available bytes; 97.74% used; 225816577 free inodes.

server3 `/tmp`: 85770252288 available bytes; 95.21% used; 114198913 free inodes.

server3 `/var/tmp`: 85770252288 available bytes; 95.21% used; 114198913 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105730727936 available bytes; 94.10% used; 114348873 free inodes.

server4 `/home`: 105730727936 available bytes; 94.10% used; 114348873 free inodes.

server4 `/data`: 115634081792 available bytes; 98.40% used; 225258055 free inodes.

server4 `/tmp`: 105730727936 available bytes; 94.10% used; 114348873 free inodes.

server4 `/var/tmp`: 105730727936 available bytes; 94.10% used; 114348873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
