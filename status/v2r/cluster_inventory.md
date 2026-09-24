# V2R cluster inventory

2026-09-24T13:30:57.298027+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324027346944 available bytes; 81.92% used; 112481477 free inodes.

server1 `/home`: 324027346944 available bytes; 81.92% used; 112481477 free inodes.

server1 `/tmp`: 324027346944 available bytes; 81.92% used; 112481477 free inodes.

server1 `/var/tmp`: 324027346944 available bytes; 81.92% used; 112481477 free inodes.

server1 `/mnt/raid5`: 417030967296 available bytes; 98.09% used; 337675104 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 57524707328 available bytes; 96.79% used; 110428721 free inodes.

server2 `/home`: 57524707328 available bytes; 96.79% used; 110428721 free inodes.

server2 `/tmp`: 57524707328 available bytes; 96.79% used; 110428721 free inodes.

server2 `/var/tmp`: 57524707328 available bytes; 96.79% used; 110428721 free inodes.

server2 `/mnt/raid5`: 506601893888 available bytes; 96.50% used; 445169669 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84705488896 available bytes; 95.27% used; 114165439 free inodes.

server3 `/home`: 84705488896 available bytes; 95.27% used; 114165439 free inodes.

server3 `/data`: 161261330432 available bytes; 97.77% used; 225803153 free inodes.

server3 `/tmp`: 84705488896 available bytes; 95.27% used; 114165439 free inodes.

server3 `/var/tmp`: 84705488896 available bytes; 95.27% used; 114165439 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105769709568 available bytes; 94.10% used; 114348741 free inodes.

server4 `/home`: 105769709568 available bytes; 94.10% used; 114348741 free inodes.

server4 `/data`: 90036604928 available bytes; 98.76% used; 225257176 free inodes.

server4 `/tmp`: 105769709568 available bytes; 94.10% used; 114348741 free inodes.

server4 `/var/tmp`: 105769709568 available bytes; 94.10% used; 114348741 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
