# V2R cluster inventory

2026-09-24T18:33:47.337836+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324005654528 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324005654528 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324005654528 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324005654528 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 416315101184 available bytes; 98.09% used; 337638969 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 54485979136 available bytes; 96.96% used; 110411974 free inodes.

server2 `/home`: 54485979136 available bytes; 96.96% used; 110411974 free inodes.

server2 `/tmp`: 54485979136 available bytes; 96.96% used; 110411974 free inodes.

server2 `/var/tmp`: 54485979136 available bytes; 96.96% used; 110411974 free inodes.

server2 `/mnt/raid5`: 496071856128 available bytes; 96.57% used; 445160639 free inodes.
| server3 | True | ['1'] | [] |

server3 `/`: 84407218176 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84407218176 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152850305024 available bytes; 97.89% used; 225800488 free inodes.

server3 `/tmp`: 84407218176 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84407218176 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105662128128 available bytes; 94.10% used; 114348505 free inodes.

server4 `/home`: 105662128128 available bytes; 94.10% used; 114348505 free inodes.

server4 `/data`: 90039984128 available bytes; 98.76% used; 225267882 free inodes.

server4 `/tmp`: 105662128128 available bytes; 94.10% used; 114348505 free inodes.

server4 `/var/tmp`: 105662128128 available bytes; 94.10% used; 114348505 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
