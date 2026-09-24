# V2R cluster inventory

2026-09-24T04:22:34.377394+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324708622336 available bytes; 81.89% used; 112493315 free inodes.

server1 `/home`: 324708622336 available bytes; 81.89% used; 112493315 free inodes.

server1 `/tmp`: 324708622336 available bytes; 81.89% used; 112493315 free inodes.

server1 `/var/tmp`: 324708622336 available bytes; 81.89% used; 112493315 free inodes.

server1 `/mnt/raid5`: 435980935168 available bytes; 98.00% used; 337724699 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 40786771968 available bytes; 97.72% used; 110430666 free inodes.

server2 `/home`: 40786771968 available bytes; 97.72% used; 110430666 free inodes.

server2 `/tmp`: 40786771968 available bytes; 97.72% used; 110430666 free inodes.

server2 `/var/tmp`: 40786771968 available bytes; 97.72% used; 110430666 free inodes.

server2 `/mnt/raid5`: 525600374784 available bytes; 96.37% used; 445196072 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292031877120 available bytes; 83.70% used; 114177116 free inodes.

server3 `/home`: 292031877120 available bytes; 83.70% used; 114177116 free inodes.

server3 `/data`: 31690694656 available bytes; 99.56% used; 225841548 free inodes.

server3 `/tmp`: 292031877120 available bytes; 83.70% used; 114177116 free inodes.

server3 `/var/tmp`: 292031877120 available bytes; 83.70% used; 114177116 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105845395456 available bytes; 94.09% used; 114349448 free inodes.

server4 `/home`: 105845395456 available bytes; 94.09% used; 114349448 free inodes.

server4 `/data`: 256716804096 available bytes; 96.45% used; 225381790 free inodes.

server4 `/tmp`: 105845395456 available bytes; 94.09% used; 114349448 free inodes.

server4 `/var/tmp`: 105845395456 available bytes; 94.09% used; 114349448 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
