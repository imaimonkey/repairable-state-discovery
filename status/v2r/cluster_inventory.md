# V2R cluster inventory

2026-09-24T03:17:43.750707+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325362081792 available bytes; 81.85% used; 112498279 free inodes.

server1 `/home`: 325362081792 available bytes; 81.85% used; 112498279 free inodes.

server1 `/tmp`: 325362081792 available bytes; 81.85% used; 112498279 free inodes.

server1 `/var/tmp`: 325362081792 available bytes; 81.85% used; 112498279 free inodes.

server1 `/mnt/raid5`: 432468299776 available bytes; 98.02% used; 337732189 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40846278656 available bytes; 97.72% used; 110431186 free inodes.

server2 `/home`: 40846278656 available bytes; 97.72% used; 110431186 free inodes.

server2 `/tmp`: 40846278656 available bytes; 97.72% used; 110431186 free inodes.

server2 `/var/tmp`: 40846278656 available bytes; 97.72% used; 110431186 free inodes.

server2 `/mnt/raid5`: 527529848832 available bytes; 96.35% used; 445198042 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292125945856 available bytes; 83.70% used; 114180819 free inodes.

server3 `/home`: 292125945856 available bytes; 83.70% used; 114180819 free inodes.

server3 `/data`: 39642681344 available bytes; 99.45% used; 225844451 free inodes.

server3 `/tmp`: 292125945856 available bytes; 83.70% used; 114180819 free inodes.

server3 `/var/tmp`: 292125945856 available bytes; 83.70% used; 114180819 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105987563520 available bytes; 94.09% used; 114349612 free inodes.

server4 `/home`: 105987563520 available bytes; 94.09% used; 114349612 free inodes.

server4 `/data`: 289542193152 available bytes; 96.00% used; 225386612 free inodes.

server4 `/tmp`: 105987563520 available bytes; 94.09% used; 114349612 free inodes.

server4 `/var/tmp`: 105987563520 available bytes; 94.09% used; 114349612 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
