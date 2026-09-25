# V2R cluster inventory

2026-09-25T01:30:24.133964+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319077429248 available bytes; 82.20% used; 112480757 free inodes.

server1 `/home`: 319077429248 available bytes; 82.20% used; 112480757 free inodes.

server1 `/tmp`: 319077429248 available bytes; 82.20% used; 112480757 free inodes.

server1 `/var/tmp`: 319077429248 available bytes; 82.20% used; 112480757 free inodes.

server1 `/mnt/raid5`: 416481959936 available bytes; 98.09% used; 337612911 free inodes.
| server2 | True | ['2', '6'] | [] |

server2 `/`: 23051137024 available bytes; 98.71% used; 110410768 free inodes.

server2 `/home`: 23051137024 available bytes; 98.71% used; 110410768 free inodes.

server2 `/tmp`: 23051137024 available bytes; 98.71% used; 110410768 free inodes.

server2 `/var/tmp`: 23051137024 available bytes; 98.71% used; 110410768 free inodes.

server2 `/mnt/raid5`: 490551853056 available bytes; 96.61% used; 445161379 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84355383296 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84355383296 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 146685702144 available bytes; 97.97% used; 225812294 free inodes.

server3 `/tmp`: 84355383296 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84355383296 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105778855936 available bytes; 94.10% used; 114348289 free inodes.

server4 `/home`: 105778855936 available bytes; 94.10% used; 114348289 free inodes.

server4 `/data`: 53317672960 available bytes; 99.26% used; 225030629 free inodes.

server4 `/tmp`: 105778855936 available bytes; 94.10% used; 114348289 free inodes.

server4 `/var/tmp`: 105778855936 available bytes; 94.10% used; 114348289 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
