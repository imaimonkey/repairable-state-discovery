# V2R cluster inventory

2026-09-24T13:20:06.662215+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324023947264 available bytes; 81.92% used; 112481545 free inodes.

server1 `/home`: 324023947264 available bytes; 81.92% used; 112481545 free inodes.

server1 `/tmp`: 324023947264 available bytes; 81.92% used; 112481545 free inodes.

server1 `/var/tmp`: 324023947264 available bytes; 81.92% used; 112481545 free inodes.

server1 `/mnt/raid5`: 417048588288 available bytes; 98.09% used; 337676369 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57541263360 available bytes; 96.79% used; 110428837 free inodes.

server2 `/home`: 57541263360 available bytes; 96.79% used; 110428837 free inodes.

server2 `/tmp`: 57541263360 available bytes; 96.79% used; 110428837 free inodes.

server2 `/var/tmp`: 57541263360 available bytes; 96.79% used; 110428837 free inodes.

server2 `/mnt/raid5`: 506946568192 available bytes; 96.50% used; 445170146 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 84752117760 available bytes; 95.27% used; 114174954 free inodes.

server3 `/home`: 84752117760 available bytes; 95.27% used; 114174954 free inodes.

server3 `/data`: 161404481536 available bytes; 97.77% used; 225809481 free inodes.

server3 `/tmp`: 84752117760 available bytes; 95.27% used; 114174954 free inodes.

server3 `/var/tmp`: 84752117760 available bytes; 95.27% used; 114174954 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105770139648 available bytes; 94.10% used; 114348748 free inodes.

server4 `/home`: 105770139648 available bytes; 94.10% used; 114348748 free inodes.

server4 `/data`: 90034577408 available bytes; 98.76% used; 225257183 free inodes.

server4 `/tmp`: 105770139648 available bytes; 94.10% used; 114348748 free inodes.

server4 `/var/tmp`: 105770139648 available bytes; 94.10% used; 114348748 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
