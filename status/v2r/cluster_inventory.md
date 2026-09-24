# V2R cluster inventory

2026-09-24T09:40:08.710075+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324454572032 available bytes; 81.90% used; 112489761 free inodes.

server1 `/home`: 324454572032 available bytes; 81.90% used; 112489761 free inodes.

server1 `/tmp`: 324454572032 available bytes; 81.90% used; 112489761 free inodes.

server1 `/var/tmp`: 324454572032 available bytes; 81.90% used; 112489761 free inodes.

server1 `/mnt/raid5`: 501817483264 available bytes; 97.70% used; 337712177 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57763782656 available bytes; 96.78% used; 110430792 free inodes.

server2 `/home`: 57763782656 available bytes; 96.78% used; 110430792 free inodes.

server2 `/tmp`: 57763782656 available bytes; 96.78% used; 110430792 free inodes.

server2 `/var/tmp`: 57763782656 available bytes; 96.78% used; 110430792 free inodes.

server2 `/mnt/raid5`: 514279149568 available bytes; 96.45% used; 445177129 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85836652544 available bytes; 95.21% used; 114199471 free inodes.

server3 `/home`: 85836652544 available bytes; 95.21% used; 114199471 free inodes.

server3 `/data`: 165724925952 available bytes; 97.71% used; 225820323 free inodes.

server3 `/tmp`: 85836652544 available bytes; 95.21% used; 114199471 free inodes.

server3 `/var/tmp`: 85836652544 available bytes; 95.21% used; 114199471 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757184000 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105757184000 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154568155136 available bytes; 97.86% used; 225273218 free inodes.

server4 `/tmp`: 105757184000 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105757184000 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
