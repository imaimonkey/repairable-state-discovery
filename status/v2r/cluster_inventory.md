# V2R cluster inventory

2026-09-23T23:55:21.533910+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325583863808 available bytes; 81.84% used; 112500967 free inodes.

server1 `/home`: 325583863808 available bytes; 81.84% used; 112500967 free inodes.

server1 `/tmp`: 325583863808 available bytes; 81.84% used; 112500967 free inodes.

server1 `/var/tmp`: 325583863808 available bytes; 81.84% used; 112500967 free inodes.

server1 `/mnt/raid5`: 1286826307584 available bytes; 94.10% used; 337735508 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41021431808 available bytes; 97.71% used; 110432465 free inodes.

server2 `/home`: 41021431808 available bytes; 97.71% used; 110432465 free inodes.

server2 `/tmp`: 41021431808 available bytes; 97.71% used; 110432465 free inodes.

server2 `/var/tmp`: 41021431808 available bytes; 97.71% used; 110432465 free inodes.

server2 `/mnt/raid5`: 533672300544 available bytes; 96.31% used; 445204389 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292791975936 available bytes; 83.66% used; 114208756 free inodes.

server3 `/home`: 292791975936 available bytes; 83.66% used; 114208756 free inodes.

server3 `/data`: 82277384192 available bytes; 98.86% used; 225844933 free inodes.

server3 `/tmp`: 292791975936 available bytes; 83.66% used; 114208756 free inodes.

server3 `/var/tmp`: 292791975936 available bytes; 83.66% used; 114208756 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106149363712 available bytes; 94.08% used; 114351443 free inodes.

server4 `/home`: 106149363712 available bytes; 94.08% used; 114351443 free inodes.

server4 `/data`: 292951961600 available bytes; 95.95% used; 225416487 free inodes.

server4 `/tmp`: 106149363712 available bytes; 94.08% used; 114351443 free inodes.

server4 `/var/tmp`: 106149363712 available bytes; 94.08% used; 114351443 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
