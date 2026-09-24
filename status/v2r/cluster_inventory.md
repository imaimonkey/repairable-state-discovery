# V2R cluster inventory

2026-09-24T23:10:08.042092+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 320269041664 available bytes; 82.13% used; 112480842 free inodes.

server1 `/home`: 320269041664 available bytes; 82.13% used; 112480842 free inodes.

server1 `/tmp`: 320269041664 available bytes; 82.13% used; 112480842 free inodes.

server1 `/var/tmp`: 320269041664 available bytes; 82.13% used; 112480842 free inodes.

server1 `/mnt/raid5`: 415279415296 available bytes; 98.09% used; 337615549 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23121473536 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23121473536 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23121473536 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23121473536 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 487306567680 available bytes; 96.63% used; 445152073 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84372525056 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84372525056 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 148608827392 available bytes; 97.95% used; 225801295 free inodes.

server3 `/tmp`: 84372525056 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84372525056 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800302592 available bytes; 94.10% used; 114348309 free inodes.

server4 `/home`: 105800302592 available bytes; 94.10% used; 114348309 free inodes.

server4 `/data`: 61820715008 available bytes; 99.15% used; 225176626 free inodes.

server4 `/tmp`: 105800302592 available bytes; 94.10% used; 114348309 free inodes.

server4 `/var/tmp`: 105800302592 available bytes; 94.10% used; 114348309 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
