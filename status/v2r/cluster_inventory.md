# V2R cluster inventory

2026-09-23T23:21:24.742019+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325662572544 available bytes; 81.83% used; 112501609 free inodes.

server1 `/home`: 325662572544 available bytes; 81.83% used; 112501609 free inodes.

server1 `/tmp`: 325662572544 available bytes; 81.83% used; 112501609 free inodes.

server1 `/var/tmp`: 325662572544 available bytes; 81.83% used; 112501609 free inodes.

server1 `/mnt/raid5`: 1375613976576 available bytes; 93.69% used; 337739743 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41047760896 available bytes; 97.71% used; 110432603 free inodes.

server2 `/home`: 41047760896 available bytes; 97.71% used; 110432603 free inodes.

server2 `/tmp`: 41047760896 available bytes; 97.71% used; 110432603 free inodes.

server2 `/var/tmp`: 41047760896 available bytes; 97.71% used; 110432603 free inodes.

server2 `/mnt/raid5`: 534764019712 available bytes; 96.30% used; 445205862 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292245983232 available bytes; 83.69% used; 114171233 free inodes.

server3 `/home`: 292245983232 available bytes; 83.69% used; 114171233 free inodes.

server3 `/data`: 82320171008 available bytes; 98.86% used; 225845945 free inodes.

server3 `/tmp`: 292245983232 available bytes; 83.69% used; 114171233 free inodes.

server3 `/var/tmp`: 292245983232 available bytes; 83.69% used; 114171233 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106248749056 available bytes; 94.07% used; 114352668 free inodes.

server4 `/home`: 106248749056 available bytes; 94.07% used; 114352668 free inodes.

server4 `/data`: 293630971904 available bytes; 95.94% used; 225426447 free inodes.

server4 `/tmp`: 106248749056 available bytes; 94.07% used; 114352668 free inodes.

server4 `/var/tmp`: 106248749056 available bytes; 94.07% used; 114352668 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
