# V2R cluster inventory

2026-09-24T09:37:01.489205+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324452536320 available bytes; 81.90% used; 112489791 free inodes.

server1 `/home`: 324452536320 available bytes; 81.90% used; 112489791 free inodes.

server1 `/tmp`: 324452536320 available bytes; 81.90% used; 112489791 free inodes.

server1 `/var/tmp`: 324452536320 available bytes; 81.90% used; 112489791 free inodes.

server1 `/mnt/raid5`: 501829103616 available bytes; 97.70% used; 337712546 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57765138432 available bytes; 96.78% used; 110430799 free inodes.

server2 `/home`: 57765138432 available bytes; 96.78% used; 110430799 free inodes.

server2 `/tmp`: 57765138432 available bytes; 96.78% used; 110430799 free inodes.

server2 `/var/tmp`: 57765138432 available bytes; 96.78% used; 110430799 free inodes.

server2 `/mnt/raid5`: 514393825280 available bytes; 96.45% used; 445177460 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85430480896 available bytes; 95.23% used; 114174450 free inodes.

server3 `/home`: 85430480896 available bytes; 95.23% used; 114174450 free inodes.

server3 `/data`: 165741465600 available bytes; 97.71% used; 225820410 free inodes.

server3 `/tmp`: 85430480896 available bytes; 95.23% used; 114174450 free inodes.

server3 `/var/tmp`: 85430480896 available bytes; 95.23% used; 114174450 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757454336 available bytes; 94.10% used; 114349042 free inodes.

server4 `/home`: 105757454336 available bytes; 94.10% used; 114349042 free inodes.

server4 `/data`: 154577489920 available bytes; 97.86% used; 225273235 free inodes.

server4 `/tmp`: 105757454336 available bytes; 94.10% used; 114349042 free inodes.

server4 `/var/tmp`: 105757454336 available bytes; 94.10% used; 114349042 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
