# V2R cluster inventory

2026-09-24T04:40:07.042483+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324626374656 available bytes; 81.89% used; 112492903 free inodes.

server1 `/home`: 324626374656 available bytes; 81.89% used; 112492903 free inodes.

server1 `/tmp`: 324626374656 available bytes; 81.89% used; 112492903 free inodes.

server1 `/var/tmp`: 324626374656 available bytes; 81.89% used; 112492903 free inodes.

server1 `/mnt/raid5`: 460148060160 available bytes; 97.89% used; 337724645 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40770879488 available bytes; 97.73% used; 110430482 free inodes.

server2 `/home`: 40770879488 available bytes; 97.73% used; 110430482 free inodes.

server2 `/tmp`: 40770879488 available bytes; 97.73% used; 110430482 free inodes.

server2 `/var/tmp`: 40770879488 available bytes; 97.73% used; 110430482 free inodes.

server2 `/mnt/raid5`: 524760047616 available bytes; 96.37% used; 445195510 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292409081856 available bytes; 83.68% used; 114200444 free inodes.

server3 `/home`: 292409081856 available bytes; 83.68% used; 114200444 free inodes.

server3 `/data`: 24368283648 available bytes; 99.66% used; 225840755 free inodes.

server3 `/tmp`: 292409081856 available bytes; 83.68% used; 114200444 free inodes.

server3 `/var/tmp`: 292409081856 available bytes; 83.68% used; 114200444 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105836609536 available bytes; 94.09% used; 114349415 free inodes.

server4 `/home`: 105836609536 available bytes; 94.09% used; 114349415 free inodes.

server4 `/data`: 253388132352 available bytes; 96.50% used; 225366872 free inodes.

server4 `/tmp`: 105836609536 available bytes; 94.09% used; 114349415 free inodes.

server4 `/var/tmp`: 105836609536 available bytes; 94.09% used; 114349415 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
