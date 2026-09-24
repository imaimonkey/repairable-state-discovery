# V2R cluster inventory

2026-09-24T23:05:28.881533+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 321124044800 available bytes; 82.09% used; 112480861 free inodes.

server1 `/home`: 321124044800 available bytes; 82.09% used; 112480861 free inodes.

server1 `/tmp`: 321124044800 available bytes; 82.09% used; 112480861 free inodes.

server1 `/var/tmp`: 321124044800 available bytes; 82.09% used; 112480861 free inodes.

server1 `/mnt/raid5`: 415287128064 available bytes; 98.09% used; 337616103 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23129563136 available bytes; 98.71% used; 110410806 free inodes.

server2 `/home`: 23129563136 available bytes; 98.71% used; 110410806 free inodes.

server2 `/tmp`: 23129563136 available bytes; 98.71% used; 110410806 free inodes.

server2 `/var/tmp`: 23129563136 available bytes; 98.71% used; 110410806 free inodes.

server2 `/mnt/raid5`: 487431380992 available bytes; 96.63% used; 445152065 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84370100224 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84370100224 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 148692885504 available bytes; 97.95% used; 225801386 free inodes.

server3 `/tmp`: 84370100224 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84370100224 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800679424 available bytes; 94.10% used; 114348311 free inodes.

server4 `/home`: 105800679424 available bytes; 94.10% used; 114348311 free inodes.

server4 `/data`: 61912289280 available bytes; 99.14% used; 225183692 free inodes.

server4 `/tmp`: 105800679424 available bytes; 94.10% used; 114348311 free inodes.

server4 `/var/tmp`: 105800679424 available bytes; 94.10% used; 114348311 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
