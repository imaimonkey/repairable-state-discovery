# V2R cluster inventory

2026-09-24T10:04:59.385915+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324426051584 available bytes; 81.90% used; 112489497 free inodes.

server1 `/home`: 324426051584 available bytes; 81.90% used; 112489497 free inodes.

server1 `/tmp`: 324426051584 available bytes; 81.90% used; 112489497 free inodes.

server1 `/var/tmp`: 324426051584 available bytes; 81.90% used; 112489497 free inodes.

server1 `/mnt/raid5`: 500685402112 available bytes; 97.70% used; 337700789 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57747668992 available bytes; 96.78% used; 110430727 free inodes.

server2 `/home`: 57747668992 available bytes; 96.78% used; 110430727 free inodes.

server2 `/tmp`: 57747668992 available bytes; 96.78% used; 110430727 free inodes.

server2 `/var/tmp`: 57747668992 available bytes; 96.78% used; 110430727 free inodes.

server2 `/mnt/raid5`: 513515053056 available bytes; 96.45% used; 445176530 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85381599232 available bytes; 95.24% used; 114173536 free inodes.

server3 `/home`: 85381599232 available bytes; 95.24% used; 114173536 free inodes.

server3 `/data`: 164466446336 available bytes; 97.73% used; 225819172 free inodes.

server3 `/tmp`: 85381599232 available bytes; 95.24% used; 114173536 free inodes.

server3 `/var/tmp`: 85381599232 available bytes; 95.24% used; 114173536 free inodes.
| server4 | True | ['0'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747673088 available bytes; 94.10% used; 114349014 free inodes.

server4 `/home`: 105747673088 available bytes; 94.10% used; 114349014 free inodes.

server4 `/data`: 154006790144 available bytes; 97.87% used; 225273373 free inodes.

server4 `/tmp`: 105747673088 available bytes; 94.10% used; 114349014 free inodes.

server4 `/var/tmp`: 105747673088 available bytes; 94.10% used; 114349014 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
